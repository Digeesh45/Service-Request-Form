import frappe
from frappe.model.document import Document
from frappe.utils import now

class ServiceRequestForm(Document):
    def before_insert(self):
        self.workflow_state = "Draft"
        self.created_by = frappe.session.user
        self.created_on = now()
    
    def validate(self):
        for item in self.get("service_form_item") or []:
            if not item.item_price and item.item:
                price_data = get_item_price(item.item)
                if isinstance(price_data, dict):
                    item.item_price = price_data.get("price_list_rate") or 0
                    item.valid_from = price_data.get("valid_from")
                    item.valid_upto = price_data.get("valid_upto")

    def on_submit(self):
        if self.create_issue:
            self.create_linked_issue()
    
    def create_linked_issue(self):
        issue_doc = frappe.get_doc({
            'doctype': 'Issue',
            'subject': f'Service request: {self.name}',
            'customer': self.customer,
            'description': self.description,
            'priority': self.priority,
            'reference_doctype': 'Service Request Form',
            'reference_name': self.name
        })
        issue_doc.insert()
        frappe.msgprint(f'Issue {issue_doc.name} created successfully')

@frappe.whitelist()
def get_item_price(item_code):
    if not item_code:
        return {}

    item_price_doc = frappe.db.get_value(
        'Item Price',
        {
            'item_code': item_code,
            'price_list': 'Standard Buying'  # Change to 'Standard Selling' if needed
        },
        ['price_list_rate', 'valid_from', 'valid_upto'],
        as_dict=True
    )

    if not item_price_doc:
        item_price_doc = frappe.db.get_value(
            'Item Price',
            {'item_code': item_code},
            ['price_list_rate', 'valid_from', 'valid_upto'],
            as_dict=True
        )

    if not item_price_doc:
        item = frappe.get_value('Item', item_code, ['standard_rate', 'valuation_rate'], as_dict=True)
        price = item.standard_rate or item.valuation_rate or 0
        return {
            'price_list_rate': price,
            'valid_from': None,
            'valid_upto': None
        }

    return item_price_doc or {}

@frappe.whitelist()
def debug_item_price(item_code):
    if not item_code:
        return "No item code provided"
    
    result = {}
    item_doc = frappe.get_doc('Item', item_code)
    result['item_exists'] = True
    result['standard_rate'] = item_doc.standard_rate
    result['valuation_rate'] = item_doc.valuation_rate
    
    item_prices = frappe.get_all('Item Price', 
        filters={'item_code': item_code}, 
        fields=['price_list', 'price_list_rate', 'selling', 'buying'])
    
    result['item_prices'] = item_prices
    return result

def has_permission(doc, ptype, user):
    if ptype == "read" and doc.docstatus == 1:
        for item in doc.service_form_item:
            if item.assigned_technician == user:
                return True
        return False
    return True
