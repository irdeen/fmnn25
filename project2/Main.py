from Newton_Handler import Classic_Newton, Exact_Newton, Inexact_Newton_G, Inexact_Newton_WP
import numpy as np
from chebyquad_problem import chebyquad, gradchebyquad
import scipy.optimize as so

if __name__ == '__main__':

    # f = lambda x: x[0] ** 2 + x[1] ** 2
    f = lambda x: 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2

    classic_newton = Classic_Newton()
    exact_newton = Exact_Newton()
    inexact_newton_g = Inexact_Newton_G()
    inexact_newton_wp = Inexact_Newton_WP()

    x0 = np.array([1.01,0.901])

    print("Classic Newton:")
    print("\tAnswer:", classic_newton.optimize(f, x0, 100))
    print("\nExact Newton:")
    print("\tAnswer:", exact_newton.optimize(f, x0, 100))
    print("\nInexact c Newton G:")
    print("\tAnswer:", inexact_newton_g.optimize(f, x0, 100))
    print("\nInexact Newton WP:")
    print("\tAnswer:", inexact_newton_wp.optimize(f, x0, 100))

    x = np.linspace(0,1,4)

    classic_newton = Classic_Newton(gradchebyquad)
    exact_newton = Exact_Newton(gradchebyquad)
    inexact_newton_g = Inexact_Newton_G(gradchebyquad)
    inexact_newton_wp = Inexact_Newton_WP(gradchebyquad)
    print("\nNewton CHEBY:")
    print("\tAnswer:", classic_newton.optimize(chebyquad, x, 100))
    # print("\tAnswer:", exact_newton.optimize(chebyquad, x, 100))
    # print("\tAnswer:", inexact_newton_g.optimize(chebyquad, x, 100))
    # print("\tAnswer:", inexact_newton_wp.optimize(chebyquad, x, 100))
    # xmin= so.fmin_bfgs(chebyquad,x,gradchebyquad)