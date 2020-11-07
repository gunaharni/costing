from odoo.tests import common


class TestTypes(common.TransactionCase):

    def setUp(self):
        super(TestTypes, self).setUp()
        # Add the set up code here...
        self.types = self.env['costing.types']

        # create an employee record
        self.type1 = self.types.create({
            'name': 'Preliminary Costing',
        })
        self.type2 = self.types.create({
            'name': 'Buyer Approved Costing',
        })

    def test_name(self):

        self.assertEqual(self.type1.name, 'Preliminary Costing')

        self.assertEqual(self.type2.name, 'Buyer Approved Costing')

