
from collections import namedtuple

import numpy as np
import scipy.linalg as linalg

Gaussian = namedtuple('Gaussian', ['mean', 'cov'])

def quadratic_regression(prior, x_vals, y_vals):
    "implementation for bayesian quadratic regression \
    https://en.wikipedia.org/wiki/Bayesian_linear_regression"

    if prior is None:
        prior = Gaussian(np.zeros(3), np.zeros((3, 3)))

    extend = [[1.0, x, x*x] for x in x_vals]
    design_matrix = np.array(extend)

    cov = design_matrix.T.dot(design_matrix) + prior.cov

    mean = prior.cov.dot(prior.mean) + design_matrix.T.dot(y_vals)
    mean = linalg.inv(cov).dot(mean.T)

    return Gaussian(mean, cov)
