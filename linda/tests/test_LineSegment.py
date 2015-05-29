
import unittest

from linda.Vec2D import Vec2D
from linda.Ray import Ray
from linda.LineSegment import LineSegment

class LineSegmentTest(unittest.TestCase):

    def test_intersection(self):

        ray = Ray(Vec2D(), Vec2D(1, 0))
        seg = LineSegment(Vec2D(4, -2), Vec2D(4, 2))

        res = seg.intersect_ray(ray)

        self.assertTrue(len(res) == 1)

        reference = Vec2D(4, 0)

        self.assertTrue(res[0].is_equal(reference))

    def test_not_intersecting(self):

        ray = Ray(Vec2D(), Vec2D(-1, 0))
        seg = LineSegment(Vec2D(4, -2), Vec2D(4, 2))

        res = seg.intersect_ray(ray)

        self.assertTrue(not res)

    def test_equality(self):
        
        seg0 = LineSegment(Vec2D(), Vec2D(1, 0))
        seg1 = LineSegment(Vec2D(), Vec2D(1, 0))

        self.assertTrue(seg0.is_equal(seg1))
        self.assertTrue(seg1.is_equal(seg0))

    def test_equality_inverted(self):
        
        seg0 = LineSegment(Vec2D(), Vec2D(1, 0))
        seg1 = LineSegment(Vec2D(1, 0), Vec2D())

        self.assertTrue(seg0.is_equal(seg1))
        self.assertTrue(seg1.is_equal(seg0))

if __name__ == "__main__":
    unittest.main()
