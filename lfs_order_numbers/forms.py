# django imports
from django import forms

# lfs_serial_number imports
from lfs_serial_numbers.models import OrderNumberGenerator


class OrderNumberGeneratorForm(forms.ModelForm):
    """Form to edit order number generator.
    """
    class Meta:
        model = OrderNumberGenerator
        fields = ("format", "last")
