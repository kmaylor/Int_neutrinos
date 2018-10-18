from Likelihoods.nest_plik import planck

from pymultinest.solve import Solver
from pymultinest.analyse import Analyzer
from pymultinest.solve import solve
from pymultinest.watch import ProgressPlotter
basename='/home/kmaylor/int_neutrinos/Multinest_output/Plik_2.3/plik'
p=planck()
p.int_nu_f=.6666666
ProgressPlotter(8, interval_ms=20, outputfiles_basename=basename)
solution = solve(LogLikelihood=p.LogLikelihood, Prior=p.Prior, n_dims=8,n_params=8,n_clustering_params=1, outputfiles_basename=basename, verbose=True, n_live_points=400,max_modes=2, evidence_tolerance=.1)

print(solution)
