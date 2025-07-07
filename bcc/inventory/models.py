from django.db import models
# from .dependency import TIRES_BRAND_CHOICES, MAGWHEELS_BRAND_CHOICES
from .dependency import *

class Tire(models.Model):
    # Invoice Number - Integer field
    invoice_number = models.IntegerField(blank=True, null=True, default="")

    # Sold to - Char field (can be empty)
    sold_to = models.CharField(max_length=255, blank=True, null=True, default="")

    # Date - DateTimeField
    date = models.DateField()

    # Salesperson - Char field (can be empty)
    salesperson = models.CharField(max_length=255, blank=True, null=True, default="")

    # Location - Char field with choices
    LOCATION_CHOICES = [
        ('Armada', 'Armada'),
        ('Legacy', 'Legacy'),
        ('Main', 'Main'),
        ('Premiere', 'Premiere'),
    ]
    location = models.CharField(max_length=255, choices=LOCATION_CHOICES)

    # Transaction Type - Char field with choices
    TRANSACTION_TYPE_CHOICES = [
        ('OUT', 'OUT'),
        ('IN', 'IN'),
    ]
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPE_CHOICES)

    # Qty - Non-zero integer field
    qty = models.PositiveIntegerField()

    # Brand - Char field with choices
    brand = models.CharField(max_length=100, choices=get_tires_brand_choices())

    # Size - Integer field with choices
    size = models.IntegerField()

    # Model - Char field with choices
    model = models.CharField(max_length=255)

    # Specs - Char field with choices
    specs = models.CharField(max_length=255)

    # Load - Char field with choices (can be empty)
    load = models.CharField(max_length=100, blank=True, null=True, default="")

    remarks = models.CharField(max_length=4, blank=True, null=True, default="")

    # Supplier - Char field with choices (can be empty)
    SUPPLIER_CHOICES = [
        ('RC', 'RC'),
        ('ENT', 'ENT'),
        ('SP', 'SP'),
        ('YHI', 'YHI'),
        ('PWG', 'PWG'),
    ]
    supplier = models.CharField(max_length=3, choices=SUPPLIER_CHOICES, blank=True, null=True, default="")

    notes = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return f"{self.brand} {self.model} {self.size} {self.specs} {self.load} - {self.supplier}"
    
    class Meta:
        verbose_name = 'Tire'
        verbose_name_plural = 'Tires'
class Magwheel(models.Model):
    # Invoice Number - Integer field
    invoice_number = models.IntegerField(blank=True, null=True, default="")

    # Sold to - Char field (can be empty)
    sold_to = models.CharField(max_length=255, blank=True, null=True, default="")

    # Date - DateTimeField
    date = models.DateField()

    # Salesperson - Char field (can be empty)
    salesperson = models.CharField(max_length=255, blank=True, null=True, default="")

    # Location - Char field with choices
    LOCATION_CHOICES = [
        ('Armada', 'Armada'),
        ('Legacy', 'Legacy'),
        ('Main', 'Main'),
        ('Premiere', 'Premiere'),
    ]
    location = models.CharField(max_length=255, choices=LOCATION_CHOICES)

    # Transaction Type - Char field with choices
    TRANSACTION_TYPE_CHOICES = [
        ('OUT', 'OUT'),
        ('IN', 'IN'),
    ]
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPE_CHOICES)

    # Qty - Non-zero integer field
    qty = models.PositiveIntegerField()

    # Brand - Char field with choices
    brand = models.CharField(max_length=100, choices=get_magwheels_brand_choices())

    # Size - Char field with choices
    size = models.CharField(max_length=10)

    # Model - Char field with choices
    model = models.CharField(max_length=255)

    # PCD 1 - Char field with choices
    pcd1 = models.CharField(max_length=10)

    # PCD 1 - Char field with choices (can be empty)
    pcd2 = models.CharField(max_length=10, blank=True, null=True, default="")

    # Offset - Integer field with choices
    offset = models.CharField(max_length=10)

    # Hole Bore - Integer field with choices
    bore = models.CharField(max_length=10, blank=True, null=True, default="")

    # Color
    color = models.CharField(max_length=255)

    # Supplier - Char field with choices (can be empty)
    SUPPLIER_CHOICES = [
        ('RC', 'RC'),
        ('ENT', 'ENT'),
        ('SP', 'SP'),
        ('YHI', 'YHI'),
        ('PWG', 'PWG'),
    ]
    supplier = models.CharField(max_length=3, choices=SUPPLIER_CHOICES, blank=True, null=True, default="")

    notes = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return f"{self.brand} {self.size} {self.model} {self.pcd1}/{self.pcd2} {self.offset} {self.bore} {self.color} - {self.supplier}"
    
    class Meta:
        verbose_name = 'Magwheel'
        verbose_name_plural = 'Magwheels'


class Transaction(models.Model):
    invoice_number = models.IntegerField(blank=True, null=True, default=None)
    sold_to = models.CharField(max_length=255, blank=True, default="")
    date = models.DateField()
    salesperson = models.CharField(max_length=255, blank=True, default="")
    location = models.CharField(max_length=255, choices=[(_,_) for _ in all_locations])    
    transaction_type = models.CharField(max_length=3, choices=[(_,_) for _ in inventory_movement])
    service = models.BooleanField(default = False)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    notes = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.sold_to} ({self.date})"

class Tire_test(models.Model):
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='tires',null=True,blank = True)

    qty = models.PositiveIntegerField()
    brand = models.CharField(max_length=100, choices=get_tires_brand_choices())
    size = models.IntegerField()
    model = models.CharField(max_length=255)
    specs = models.CharField(max_length=255)
    load = models.CharField(max_length=100, blank=True, null=True, default="")
    remarks = models.CharField(max_length=4, blank=True, null=True, default="")    
    supplier = models.CharField(max_length=3, choices=[(_,_) for _ in suppliers], blank=True, null=True, default="")
    notes = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return f"{self.brand} {self.model} {self.size} {self.specs} {self.load} - {self.supplier}"
    

class Magwheel_test(models.Model):
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='magwheels',null = True, blank = True)

    qty = models.PositiveIntegerField()
    brand = models.CharField(max_length=100, choices=get_magwheels_brand_choices())
    size = models.CharField(max_length=10)
    model = models.CharField(max_length=255)
    pcd1 = models.CharField(max_length=10)
    pcd2 = models.CharField(max_length=10, blank=True, null=True, default="")
    offset = models.CharField(max_length=10)
    bore = models.CharField(max_length=10, blank=True, null=True, default="")
    color = models.CharField(max_length=255)
    supplier = models.CharField(max_length=3, choices=[(_,_) for _ in suppliers], blank=True, null=True, default="")
    notes = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return f"{self.brand} {self.size} {self.model} {self.pcd1}/{self.pcd2} {self.offset} {self.bore} {self.color} - {self.supplier}"

class TransactionPayment(models.Model):
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='payments',null = True, blank = True)
    method = models.CharField(max_length=50, choices=[(_, _) for _ in payment_method_choices])
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.BooleanField(default = False)
    locked = models.BooleanField(default = False, editable = False)

    credit_card_type = models.CharField(max_length=50, choices=[(_,_) for _ in [cc_discount_rates[i][0] for i in range(len(cc_discount_rates))]], null = True, blank = True)
    debit_card_bank = models.CharField(max_length=50, choices=[(_,_) for _ in [dc_discount_rates[i][0] for i in range(len(dc_discount_rates))]],null=True,blank=True)
    cheque_on_date = models.PositiveIntegerField(null=True,blank=True)

    notes = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return f"{self.method} - {self.amount}"
    
    def save(self, *args, **kwargs):
        if self.pk:
            old = TransactionPayment.objects.get(pk=self.pk)
            if old.status and not self.status:
                raise ValueError("Cannot unset payment once marked as received.")
        if self.status:
            self.locked = True # once status is True, lock it
        super().save(*args, **kwargs)
