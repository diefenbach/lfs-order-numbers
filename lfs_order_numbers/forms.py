# django imports
from django import forms

# lfs_order_numbers imports
from lfs_order_numbers.models import OrderNumberGenerator


class OrderNumberGeneratorForm(forms.ModelForm):
    """Form to edit order number generator.
    """
    class Meta:
        model = OrderNumberGenerator
        fields = ("format", "last")
