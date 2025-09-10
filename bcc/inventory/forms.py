# forms.py
from django import forms
from .models import *
from .dependency import *

from datetime import date

class TireTransactionForm(forms.ModelForm):
    class Meta:
        model = Tire
        fields = ['invoice_number', 'sold_to', 'date', 'salesperson', 'location',
                  'transaction_type', 'qty', 'brand', 'size', 'model', 'specs', 'load', 'remarks', 'supplier', 'notes']
        
class MagwheelTransactionForm(forms.ModelForm):
    class Meta:
        model = Magwheel
        fields = ['invoice_number', 'sold_to', 'date', 'salesperson', 'location',
                  'transaction_type', 'qty', 'brand', 'size', 'model', 'pcd1', 'pcd2', 'offset', 'bore', 'color', 'supplier', 'notes']

class FullTransactionForm(forms.Form):
    # No fields yet
    pass

# Version 2.0 Below

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['amount']

class TireForm(forms.Form):
    qty = forms.IntegerField(min_value=1)
    brand = forms.ChoiceField(choices=get_tires_brand_choices(), required=True)

    size = forms.CharField(max_length=255, required=True)
    model = forms.CharField(max_length=255, required=True)
    specs = forms.CharField(max_length=255, required=True)
    load = forms.CharField(max_length=255, required=False)
    remarks = forms.CharField(max_length=255, required=False)

    SUPPLIER_CHOICES = [
        (supplier, supplier) for supplier in suppliers
    ]
    supplier = forms.ChoiceField(choices=SUPPLIER_CHOICES, required=False)

    notes = forms.CharField(widget=forms.Textarea, required=False)

class MagwheelForm(forms.Form):
    qty = forms.IntegerField(min_value = 1)
    brand = forms.ChoiceField(choices = get_magwheels_brand_choices(), required=True)
    size = forms.CharField(max_length=255, required=True)
    model = forms.CharField(max_length=255, required=True)
    pcd1 = forms.CharField(max_length=255, required=True)
    pcd2 = forms.CharField(max_length=255, required=False)
    offset = forms.CharField(max_length=255, required=True)
    bore = forms.CharField(max_length=255, required=False)
    color = forms.CharField(max_length=255, required=True)
    SUPPLIER_CHOICES = [
        (supplier, supplier) for supplier in suppliers
    ]
    supplier = forms.ChoiceField(choices = SUPPLIER_CHOICES, required = False)
    notes = forms.CharField(widget = forms.Textarea, required = False)

class SavedTireForm(forms.ModelForm):
    class Meta:
        model = TireModel
        exclude = ['transaction']

class SavedMagwheelForm(forms.ModelForm):
    class Meta:
        model = MagwheelModel
        exclude = ['transaction']

class TransactionPaymentForm(forms.Form):
    PAYMENT_METHOD_CHOICES = [
        (method, method) for method in payment_method_choices
    ]

    CREDIT_CARD_CHOICES = [
        (cc[0], cc[0]) for cc in cc_discount_rates
    ]

    DEBIT_CARD_CHOICES = [
        (dc[0], dc[0]) for dc in dc_discount_rates
    ]

    method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, required=True)
    amount = forms.DecimalField(max_digits=12, required=False)
    status = forms.BooleanField(required=False)
    credit_card_type = forms.ChoiceField(choices=CREDIT_CARD_CHOICES, required=False)
    debit_card_bank = forms.ChoiceField(choices=DEBIT_CARD_CHOICES, required=False)
    cheque_on_date = forms.IntegerField(required=False, min_value=0)
    notes = forms.CharField(widget=forms.Textarea, required=False)

    def clean(self):
        cleaned_data = super().clean()
        method = cleaned_data.get("method")

        # Enforce conditional fields
        if method == "Credit Card" and not cleaned_data.get("credit_card_type"):
            self.add_error("credit_card_type", "This field is required for Credit Card payments.")
        if method == "Debit Card" and not cleaned_data.get("debit_card_bank"):
            self.add_error("debit_card_bank", "This field is required for Debit Card payments.")
        if method == "Cheque" and not cleaned_data.get("cheque_on_date"):
            self.add_error("cheque_on_date", "This field is required for Cheque payments.")

        return cleaned_data

class SavedPaymentForm(forms.ModelForm):
    class Meta:
        model = TransactionPayment
        exclude = ['transaction']

    def clean(self):
        cleaned_data = super().clean()
        method = cleaned_data.get("method")

        if method == "Credit Card" and not cleaned_data.get("credit_card_type"):
            self.add_error("credit_card_type", "This field is required for Credit Card payments.")
        if method == "Debit Card" and not cleaned_data.get("debit_card_bank"):
            self.add_error("debit_card_bank", "This field is required for Debit Card payments.")
        if method == "Cheque" and not cleaned_data.get("cheque_on_date"):
            self.add_error("cheque_on_date", "This field is required for Cheque payments.")

        return cleaned_data

class PaymentReportForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    LOCATION_CHOICES = [
        (location, location) for location in all_locations
    ]

    locations = forms.MultipleChoiceField(choices=LOCATION_CHOICES, widget=forms.CheckboxSelectMultiple)
