import dolfin as fem
import numpy as np
from remanu import lab, fid
from scipy.optimize import curve_fit

import logging
logging.getLogger('FFC').setLevel(logging.WARNING)
logging.getLogger('UFL').setLevel(logging.WARNING)

def fit(mt, t):
    popt, _ = curve_fit(lambda t, T: np.exp(-t/T), t, mt)
    return popt[0]

def test_square():
    # Create mesh
    L = 1.e-7; mesh = fem.UnitSquareMesh(100, 100); mesh.scale(L)

    # Create a model
    rho, D = 1.e-5, 1.e-9; model = lab(mesh, rho= rho, D= D)

    # Create a sequence
    tf, n = 1.e-2, 50; seq = fid(model, dt= tf/n, tf= tf)

    # Run simulation
    mt = model.run()

    # Get curve fit
    T2 = fit(mt, seq.t_arr)

    assert abs(T2 - 1./((1./model.T2) + 4.*rho/L)) < 1.e-6
