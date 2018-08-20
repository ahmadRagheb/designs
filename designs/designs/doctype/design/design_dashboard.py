from frappe import _

def get_data():
	return {
		# 'heatmap': True,
		'heatmap_message': _('This is based on the Time Sheets created against this project'),
		'fieldname': 'design_project',
		'transactions': [
			{
				'label': _('Design'),
				'items': ['Task']
			},
			{
				'label': _('Sales'),
				'items': ['Sales Order', 'Delivery Note', 'Sales Invoice']
			},
		]
	}
