"basic circle functionality"

from linda.Vec2D import Vec2D
from linda.Ray import Ray
from math import sqrt

class Circle(object):
    "simple 2d circle class"

    def __init__(self, pos=Vec2D(), radius=1.0):
        self.pos = pos
        self.radius = radius

    def intersects(self, other):
        "return if self intersects other circle"
        return (self.pos - other.pos).length() <= (self.radius + other.radius)

    def contains_circle(self, other):
        "return if self contains other circle"
        return (self.pos - other.pos).length() <= (self.radius - other.radius)

    def contains_point(self, point):
        "return if self contains point"
        return (self.pos - point).length() <= self.radius

    def intersect_ray(self, ray):
        "return whether self intersects with tangent"

        direction = ray.direction
        diff = ray.origin - self.pos

        param1 = direction.dot(direction)
        param2 = 2 * direction.dot(diff)
        param3 = diff.dot(diff) - (self.radius * self.radius)

        points = []

        for res in Circle.solve_quadratic(param1, param2, param3):
            if res >= 0:
                points.append(ray.origin + direction * res)

        return points

    def __str__(self):
        "string representation for debugging"
        return "Circle: {pos}, {r}".format(pos=str(self.pos), r=self.radius)

    def __add__(self, vec):
        "translate circle by vec"
        return Circle(self.pos + vec, self.radius)

    def is_equal(self, other):
        "two circles are equal if the have the same center position and radius"

        if other is None:
            return False

        return (self.pos.is_equal(other.pos) and
                abs(self.radius - other.radius) < Vec2D.EPSILON)

    @staticmethod
    def solve_quadratic(param_a, param_b, param_c):
        "solve a*x^2 + b*x + c = 0"
        det = param_b*param_b - 4*param_a*param_c

        if det < 0:
            return []
        elif abs(det) < Vec2D.EPSILON:
            return [-param_b/(2*param_a)]
        else:
            sqrt_det = sqrt(det)
            res1 = (-param_b + sqrt_det)/(2 * param_a)
            res2 = (-param_b - sqrt_det)/(2 * param_a)
            return [res1, res2]
