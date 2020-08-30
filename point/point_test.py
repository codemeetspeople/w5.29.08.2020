import unittest
from point import Point


class TestPoint(unittest.TestCase):
    def test_point_default_init(self):
        point = Point()

        self.assertEqual(point.x, 0.0)
        self.assertEqual(point.y, 0.0)

    def test_point_init(self):
        point = Point(2, 7)

        self.assertEqual(point.x, 2.0)
        self.assertEqual(point.y, 7.0)

    def test_point_string_representation(self):
        point = Point(2, 7)

        self.assertEqual(str(point), '(2.0, 7.0)')

    def test_point_operators(self):
        a = Point()
        b = Point(1, 2)
        c = Point(1, 2)

        self.assertTrue(a != b)
        self.assertFalse(a == b)
        self.assertTrue(b == c)
        self.assertFalse(b != c)

    def test_point_setters(self):
        point = Point()
        self.assertEqual(point.x, 0.0)

        point.x = 42
        self.assertEqual(point.x, 42.0)

    def test_point_init_exception(self):
        with self.assertRaises(ValueError):
            Point('ololo', 'trololo')

    def test_point_setter_exception(self):
        point = Point()
        with self.assertRaises(TypeError):
            point.x = Point()


if __name__ == '__main__':
    unittest.main()
