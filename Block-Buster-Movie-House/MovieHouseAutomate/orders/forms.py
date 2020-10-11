from django import forms
from .models import *

class OrdersForm(forms.ModelForm):
	
	class Meta:
		model = Order
		fields = ('customer_first','customer_last')
