import unittest

import escape_codes

class TestAttrDict (unittest.TestCase):
	def setUp(self):
		self.attrdict = escape_codes.AttrDict({'x': 1, 'y': 2})

	def test_get_attribute (self):
		self.assertEqual(self.attrdict.x, 1)

	def test_get_key (self):
		self.assertEqual(self.attrdict['y'], 2)

	def test_get_attribute_fails (self):
		with self.assertRaises(KeyError):
			self.attrdict.nonexistent

if __name__ == '__main__':
	unittest.main()
