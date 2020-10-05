import unittest

from campersheaven.geometries import Point, Bbox


class TestPoint(unittest.TestCase):
    def test_valid_point_true(self):
        p = Point(0.0, 0.0)
        self.assertTrue(p.valid())

        p = Point(180.0, 0.0)
        self.assertTrue(p.valid())

        p = Point(-180.0, 0.0)
        self.assertTrue(p.valid())

        p = Point(0.0, 90.0)
        self.assertTrue(p.valid())

        p = Point(0.0, -90.0)
        self.assertTrue(p.valid())

    def test_valid_point_false(self):
        p = Point(181.0, 0.0)
        self.assertFalse(p.valid())

        p = Point(-181.0, 0.0)
        self.assertFalse(p.valid())

        p = Point(0.0, 91.0)
        self.assertFalse(p.valid())

        p = Point(0.0, -91.0)
        self.assertFalse(p.valid())

    def test_point_bounding_box(self):
        bbox_diff = (-0.1, 0.1, -0.1, 0.1,)

        p = Point(0.0, 0.0)
        self.assertTupleEqual(p.bbox(bbox_diff), bbox_diff)

        p = Point(180.0, 0.0)
        self.assertTupleEqual(p.bbox(bbox_diff), (179.9, 180.0, -0.1, 0.1))

        p = Point(-180.0, 0.0)
        self.assertTupleEqual(p.bbox(bbox_diff), (-180, -179.9, -0.1, 0.1))

        p = Point(0.0, 90.0)
        self.assertTupleEqual(p.bbox(bbox_diff), (-0.1, 0.1, 89.9, 90.0))

        p = Point(0.0, -90.0)
        self.assertTupleEqual(p.bbox(bbox_diff), (-0.1, 0.1, -90.0, -89.9))

    def test_within_true(self):
        bbox = Bbox(-0.1, 0.1, -0.1, 0.1)
        p = Point(0.0, 0.0)
        self.assertTrue(p.within(bbox))

        p = Point(0.1, 0.1)
        self.assertTrue(p.within(bbox))
        p = Point(0.1, -0.1)
        self.assertTrue(p.within(bbox))
        p = Point(-0.1, -0.1)
        self.assertTrue(p.within(bbox))
        p = Point(-0.1, 0.1)
        self.assertTrue(p.within(bbox))

    def test_within_false(self):
        bbox = Bbox(-0.1, 0.1, -0.1, 0.1)

        p = Point(0.2, 0.0)
        self.assertFalse(p.within(bbox))
        p = Point(0.2, -0.0)
        self.assertFalse(p.within(bbox))
        p = Point(-0.0, -0.2)
        self.assertFalse(p.within(bbox))
        p = Point(-0.0, 0.2)
        self.assertFalse(p.within(bbox))


class TestBbox(unittest.TestCase):
    def test_valid_bbox_true(self):
        bbox = Bbox(-0.1, 0.1, -0.1, 0.1)
        self.assertTrue(bbox.valid())

        bbox = Bbox(-180.0, 180.0, -90.0, 90.0)
        self.assertTrue(bbox.valid())

    def test_valid_bbox_false(self):
        bbox = Bbox(180.0, -180.0, -90.0, 90.0)
        self.assertFalse(bbox.valid())

        bbox = Bbox(-180.0, 180.0, 90.0, -90.0)
        self.assertFalse(bbox.valid())

        bbox = Bbox(-181.0, 180.0, -90.0, 90.0)
        self.assertFalse(bbox.valid())

        bbox = Bbox(-180.0, 181.0, -90.0, 90.0)
        self.assertFalse(bbox.valid())

        bbox = Bbox(-180.0, 180.0, -91.0, 90.0)
        self.assertFalse(bbox.valid())

        bbox = Bbox(-180.0, 180.0, -90.0, 91.0)
        self.assertFalse(bbox.valid())
