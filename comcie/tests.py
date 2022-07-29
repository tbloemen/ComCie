from django.test import TestCase

from comcie.models import Role


# Create your tests here.
class RoleTests(TestCase):
    def setUp(self) -> None:
        Role.objects.create(name="ComCie")

    def test_to_str(self):
        comcie_role = Role.objects.get(name="ComCie")
        self.assertEqual(comcie_role.__str__(), "ComCie")
