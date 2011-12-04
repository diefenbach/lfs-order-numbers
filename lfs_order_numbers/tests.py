# django imports
from django.test import TestCase

# lfs_serial_numbers imports
from models import OrderNumberGenerator


class OrderNumberTestCase(TestCase):
    """Tests order numbers.
    """
    fixtures = ['lfs_shop.xml']

    def setUp(self):
        self.sn = OrderNumberGenerator.objects.create(
            id="shop",
            format="PRE-%03d-SUF",
        )

    def test_defaults(self):
        self.assertEqual(self.sn.id, "shop")
        self.assertEqual(self.sn.last, 0)
        self.assertEqual(self.sn.format, "PRE-%03d-SUF")

    def test_get_next_1(self):
        self.assertEqual("PRE-001-SUF", self.sn.get_next())
        self.assertEqual("PRE-002-SUF", self.sn.get_next())
        self.assertEqual("PRE-003-SUF", self.sn.get_next())

    def test_get_next_2(self):
        self.assertEqual(1, self.sn.get_next(formatted=False))
        self.assertEqual(2, self.sn.get_next(formatted=False))
        self.assertEqual(3, self.sn.get_next(formatted=False))
