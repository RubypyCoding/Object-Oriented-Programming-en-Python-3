import unittest
from door import Door


class DoorTests(unittest.TestCase):

	def setUp(self):
		self.func = Door("green", 5)

	def test_color_is_evaluated_as_getter(self):
	    with self.assertRaises(AttributeError):
	        self.func.color

	def test_color_is_evaluated_as_setter(self):
		raised = False
		try:
			self.func.color = "red"
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')

	def test_size_is_evaluated_as_getter(self):
		self.assertEqual(self.func.size, 5)

	def test_size_is_evaluated_as_setter(self):
	    with self.assertRaises(AttributeError):
	        self.func.size = 10

	def test_status_as_getter_with_default_parameter(self):
		self.assertEqual(self.func.status, "Cerrado")

	def test_status_is_evaluated_as_setter(self):
		raised = False
		try:
			self.func.status = "Abierto"
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')

	def test_status_if_status_is_cerrado_then_open_returns_business_is_closed(self):
		self.func.status = "Cerrado"
		self.assertEqual(self.func.open(), "Business is closed")

	def test_status_if_status_is_abierto_then_open_returns_open_red_door(self):
		self.func.color = "red"
		self.func.status = "Abierto"
		self.assertEqual(self.func.open(), "open red door")

	def test_close_if_status_is_cerrado_then_close_returns_door_is_closed(self):
		self.func.status = "Cerrado"
		self.assertEqual(self.func.close(), "Door is closed")

	def test_close_if_status_is_abierto_then_close_returns_close_door_of_5_meters(self):
		self.func.status = "Abierto"
		self.assertEqual(self.func.close(), "close door of 5 meters")


if __name__=="__main__":
    unittest.main()