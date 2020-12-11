import unittest
from vs_project.DRAG.Dragon import sides
from vs_project.DRAG.Dragon import input_data


class TestDragonCurve(unittest.TestCase):

    def test_sides2(self):
        q = sides(2)
        self.assertEqual(q, 'rrl')

    def test_sides3(self):
        q = sides(3)
        self.assertEqual(q, 'rrlrrll')

    def test_sider4(self):
        q = sides(4)
        self.assertEqual(q, 'rrlrrllrrrllrll')

    def test_sider5(self):
        q = sides(5)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrll')

    def test_sider6(self):
        q = sides(6)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrllrrrlrrllrrrllrlllrrlrrlllrrllrll')

    def test_sider7(self):
        q = sides(7)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrllrrrlrrllrrrllrlllrrlrrlllrrllrllrrrlrrllrrrllrllrrrlrrlllrrllrlllrrlrrllrrrllrlllrrlrrlllrrllrll')

    def test_sider8(self):
        q = sides(8)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrllrrrlrrllrrrllrlllrrlrrlllrrllrllrrrlrrllrrrllrllrrrlrrlllrrllrlllrrlrrllrrrllrlllrrlrrlllrrllrllrrrlrrllrrrllrllrrrlrrlllrrllrllrrrlrrllrrrllrlllrrlrrlllrrllrlllrrlrrllrrrllrllrrrlrrlllrrllrlllrrlrrllrrrllrlllrrlrrlllrrllrll')

    def test_sider9(self):
        q = sides(9)
        self.assertEqual(q, 'rrlrrllrrrllrllrrrlrrlllrrllrllrrrlrrllrrrllrlllrrlrrlllrrllrllrrrlrrllrrrllrllrrrlrrlllrrllrlllrrlrrllrrrllrlllrrlrrlllrrllrllrrrlrrllrrrllrllrrrlrrlllrrllrllrrrlrrllrrrllrlllrrlrrlllrrllrlllrrlrrllrrrllrllrrrlrrlllrrllrlllrrlrrllrrrllrlllrrlrrlllrrllrllrrrlrrllrrrllrllrrrlrrlllrrllrllrrrlrrllrrrllrlllrrlrrlllrrllrllrrrlrrllrrrllrllrrrlrrlllrrllrlllrrlrrllrrrllrlllrrlrrlllrrllrlllrrlrrllrrrllrllrrrlrrlllrrllrllrrrlrrllrrrllrlllrrlrrlllrrllrlllrrlrrllrrrllrllrrrlrrlllrrllrlllrrlrrllrrrllrlllrrlrrlllrrllrll')

    def test_color1(self):
        q = input_data()
        self.assertEqual(type(q[0]), str)

    def test_color2(self):
        q = input_data()
        self.assertEqual(type(q[1]), str)


if __name__ == '__main__':
    unittest.main()