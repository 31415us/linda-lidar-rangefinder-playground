
import numpy as np
from math import pi

from linda.Vec2D import Vec2D
from linda.Ray import Ray

class LidarSimulator(object):

    def __init__(self, default_dist=10.0, nb_samples=100, angular_cutoff=pi):
        self.default_dist = default_dist
        self.nb_samples = nb_samples
        # measurement points are in [-angular_cutoff, +angular_cutoff]
        self.angular_cutoff = angular_cutoff

    def lidar_sample(self, robot_state, environment, noise_sigma=None):
        y_values = []
        x_values = []

        origin = Vec2D(robot_state.x, robot_state.y)
        current_angle = robot_state.theta - self.angular_cutoff
        delta_theta = 2*self.angular_cutoff / self.nb_samples

        for _ in range(0, self.nb_samples):
            current_angle = current_angle + delta_theta
            ray = Ray(origin, Vec2D(1, 0).rotate(current_angle))

            intersection_points = []
            for elem in environment:
                intersection_points += elem.intersect_ray(ray)

            inter_dist = [(p - origin).length() for p in intersection_points]

            if inter_dist:
                y_val = min(inter_dist)
            else:
                y_val = self.default_dist

            if not noise_sigma is None:
                y_val += np.random.normal(0.0, noise_sigma)

            x_values.append(current_angle - robot_state.theta)
            y_values.append(y_val)

        return (np.array(x_values), np.array(y_values))

