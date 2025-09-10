from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import TransactionPayment

def update_transaction_amount(transaction):
    total = sum(p.amount for p in transaction.payments.all())
    transaction.amount = total
    transaction.save(update_fields=['amount'])

@receiver(post_save, sender=TransactionPayment)
def payment_saved(sender, instance, **kwargs):
    update_transaction_amount(instance.transaction)

@receiver(post_delete, sender=TransactionPayment)
def payment_deleted(sender, instance, **kwargs):
    try:
        transaction = instance.transaction
        update_transaction_amount(transaction)
    except instance._meta.get_field("transaction").related_model.DoesNotExist:
        # Transaction is already deleted → safe to ignore
        pass
