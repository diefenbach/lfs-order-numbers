from django.db import models
from django.utils.translation import ugettext_lazy as _

from lfs.plugins import OrderNumberGenerator as Base


class OrderNumberGenerator(Base):
    """
    Generates order numbers and saves the last one.

    **Attributes:**

    last
        The last stored/returned order number.

    format
        The format of the integer part of the order number.
    """
    last = models.IntegerField(_(u"Last Order Number"), default=0)
    format = models.CharField(_(u"Format"), blank=True, max_length=20)

    def get_next(self, formatted=True):
        """Returns the next order number.

        **Parameters:**

        formatted
            If True the number will be returned within the stored format.
        """
        self.last += 1
        self.save()
        if formatted and self.format:
            return self.format % self.last
        else:
            return self.last
