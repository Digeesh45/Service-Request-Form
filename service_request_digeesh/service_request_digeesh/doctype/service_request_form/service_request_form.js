frappe.ui.form.on('Service Request Form', {
    onload(frm) {
        if (frm.is_new()) {
            frm.set_value('created_by', frappe.session.user);
        }
    },

    refresh(frm) {
        if (frm.doc.docstatus === 0) {
            frm.page.set_primary_action(__('Submit'), function () {
                show_confirmation_dialog(frm);
            });
        }
        calculate_form_totals(frm);
    },

    before_save(frm) {
        calculate_form_totals(frm);
    },

    after_save(frm) {
        calculate_form_totals(frm);
    }
});

frappe.ui.form.on('Service Form Item', {
    item(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.item) {
            frappe.call({
                method: "service_request_digeesh.service_request_digeesh.doctype.service_request_form.service_request_form.get_item_price",
                args: {
                    item_code: row.item
                },
                callback(r) {
                    if (r.message) {
                        frappe.model.set_value(cdt, cdn, 'item_price', r.message.price_list_rate || 0);
                        frappe.model.set_value(cdt, cdn, 'valid_from', r.message.valid_from || null);
                        frappe.model.set_value(cdt, cdn, 'valid_upto', r.message.valid_upto || null);
                    } else {
                        frappe.msgprint(`No price found for item: ${row.item}. Please set it manually.`);
                        frappe.model.set_value(cdt, cdn, 'item_price', 0);
                    }
                    setTimeout(() => {
                        calculate_row_total(frm, cdt, cdn);
                    }, 200);
                }
            });
        }
    },

    estimated_hours(frm, cdt, cdn) {
        calculate_row_total(frm, cdt, cdn);
    },

    item_price(frm, cdt, cdn) {
        calculate_row_total(frm, cdt, cdn);
    },

    service_form_item_remove(frm) {
        setTimeout(() => {
            calculate_form_totals(frm);
        }, 100);
    }
});

function calculate_row_total(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    let cost = (row.estimated_hours || 0) * (row.item_price || 0);
    frappe.model.set_value(cdt, cdn, 'estimated_cost', cost);
    setTimeout(() => {
        calculate_form_totals(frm);
    }, 100);
}

function calculate_form_totals(frm) {
    let total_hours = 0;
    let total_cost = 0;

    (frm.doc.service_form_item || []).forEach(row => {
        total_hours += row.estimated_hours || 0;
        total_cost += row.estimated_cost || 0;
    });

    frm.set_value('total_estimated_hours', total_hours);
    frm.set_value('total_estimated_cost', total_cost);

    frm.refresh_field('total_estimated_hours');
    frm.refresh_field('total_estimated_cost');
}

function show_confirmation_dialog(frm) {
    calculate_form_totals(frm);

    const dialog = new frappe.ui.Dialog({
        title: 'Confirm Submission',
        fields: [
            {
                label: 'Customer',
                fieldname: 'customer',
                fieldtype: 'Data',
                default: frm.doc.customer,
                read_only: 1
            },
            {
                label: 'Request Type',
                fieldname: 'request_type',
                fieldtype: 'Data',
                default: frm.doc.request_type,
                read_only: 1
            },
            {
                label: 'Priority',
                fieldname: 'priority',
                fieldtype: 'Data',
                default: frm.doc.priority,
                read_only: 1
            },
            {
                label: 'Total Estimated Hours',
                fieldname: 'total_hours',
                fieldtype: 'Float',
                default: frm.doc.total_estimated_hours,
                read_only: 1
            },
            {
                label: 'Total Estimated Cost',
                fieldname: 'total_cost',
                fieldtype: 'Currency',
                default: frm.doc.total_estimated_cost,
                read_only: 1
            }
        ],
        primary_action_label: 'Confirm',
        primary_action() {
            dialog.hide();
            setTimeout(() => {
                frm.save('Submit');
            }, 300);
        },
        secondary_action_label: 'Edit',
        secondary_action() {
            dialog.hide();
        }
    });

    dialog.show();
}
