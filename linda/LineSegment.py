
from linda.Vec2D import Vec2D


class LineSegment(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def intersect_ray(self, ray):
        "return whether self and ray intersect \
        inspired by: \
        https://stackoverflow.com/questions/563198/ \
        how-do-you-detect-where-two-line-segments-intersect"

        dir1 = self.end - self.start
        dir2 = ray.direction

        dir_cross_prod = dir1.cross(dir2)
        diff = (ray.origin - self.start)
        diff_cross_dir1 = diff.cross(dir1)

        if abs(dir_cross_prod) < Vec2D.EPSILON and \
           abs(diff_cross_dir1) < Vec2D.EPSILON:

            # ray and line overlapping should not happen
            return [] 
        elif abs(dir_cross_prod) < Vec2D.EPSILON:
            return []
        else:
            param_u = diff_cross_dir1 / dir_cross_prod
            param_t = diff.cross(dir2) / dir_cross_prod
            if 0 <= param_u and 0 <= param_t <= 1:
                return [ray.origin + ray.direction * param_u]
            else:
                return []

    def is_equal(self, other):
        
        if other is None:
            return False

        cond1 = self.start.is_equal(other.start) and self.end.is_equal(other.end)
        cond2 = self.start.is_equal(other.end) and self.end.is_equal(other.start)

        return cond1 or cond2

    def __str__(self):
        return "Line from {start} to {end}".format(start=self.start, end=self.end)

    def __add__(self, vec):
        return LineSegment(self.start + vec, self.end + vec)

