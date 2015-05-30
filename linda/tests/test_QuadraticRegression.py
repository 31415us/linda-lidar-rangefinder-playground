
import unittest
import numpy as np

from linda.QuadraticRegression import quadratic_regression, Gaussian

class QuadraticRegressionTest(unittest.TestCase):

    def test_simple_parabola(self):

        x_vals = np.array([i * 0.1 for i in range(-100, 100)])
        y_vals = x_vals * x_vals

        prior = None

        true_param = np.array([0.0, 0.0, 1.0])

        posterior = quadratic_regression(prior, x_vals, y_vals)

        np.testing.assert_allclose(posterior.mean, true_param, rtol=1e-5, atol=1e-5)

    def test_general_parabola(self):

        a = 3.0
        b = 2.0
        c = 1.0

        true_mean = np.array([c, b, a])

        x_vals = np.array([i * 0.1 for i in range(-100, 100)])
        y_vals = a * x_vals * x_vals + b * x_vals + c * np.ones(x_vals.size)

        prior = None

        posterior = quadratic_regression(prior, x_vals, y_vals)

        np.testing.assert_allclose(posterior.mean, true_mean, rtol=1e-5, atol=1e-5)


if __name__ == "__main__":
    unittest.main()
