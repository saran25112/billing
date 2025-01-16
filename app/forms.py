from django import forms
from .models import Bill,Supplier

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['supplier_name', 'item_name', 'payment_method', 'customer_name', 'number_of_products', 'weight_in_kg', 'rate']
    
    supplier_name = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        empty_label="Select a supplier"
    )
   
    payment_method = forms.ChoiceField(
        choices=Bill.PAYMENT_METHOD_CHOICES,
        initial='cash'  # Automatically select 'cash' by default
    )