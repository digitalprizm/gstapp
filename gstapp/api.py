import frappe
from erpnext.controllers.taxes_and_totals import get_itemised_tax_breakup_data
def get_item_wise_tax(self, method):
	frappe.flags.country = "UAE"
	tax_breakup=get_itemised_tax_breakup_data(self)
	import json
	self.tax_breakup = json.dumps(tax_breakup[0])