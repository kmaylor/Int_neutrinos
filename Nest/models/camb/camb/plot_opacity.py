#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.artist as mart


#opac = np.genfromtxt('opacity_neutrinos_1e-3.dat',dtype=[('z','f8'),('a','f8'),('opacity','f8'),('ratio','f8'),('H','f8')])
#opac2 = np.genfromtxt('opacity_neutrinos_1e-4.dat',dtype=[('z','f8'),('a','f8'),('opacity','f8'),('ratio','f8'),('H','f8')])
#opac3 = np.genfromtxt('opacity_neutrinos_1e-5.dat',dtype=[('z','f8'),('a','f8'),('opacity','f8'),('ratio','f8'),('H','f8')])


vis = np.genfromtxt('visibility_neutrinos_1e-3.dat',dtype=[('z','f8'),('a','f8'),('tau','f8'),('visibility_tau','f8'),('visibility_z','f8')])
vis2 = np.genfromtxt('visibility_neutrinos_1e-4.dat',dtype=[('z','f8'),('a','f8'),('tau','f8'),('visibility_tau','f8'),('visibility_z','f8')])
vis3 = np.genfromtxt('visibility_neutrinos_1e-5.dat',dtype=[('z','f8'),('a','f8'),('tau','f8'),('visibility_tau','f8'),('visibility_z','f8')])
vis4 = np.genfromtxt('visibility_neutrinos_secmode.dat',dtype=[('z','f8'),('a','f8'),('tau','f8'),('visibility_tau','f8'),('visibility_z','f8')])


#z = opac['z']
#opacity = opac['opacity']
#z2 = opac2['z']
#opacity2 = opac2['opacity']
#z3 = opac3['z']
#opacity3 = opac3['opacity']

z1 = vis['z']
z2 = vis2['z']
z3 = vis3['z']
z4 = vis4['z']
tau = 1/vis['tau']
#visibility_tau = vis['visibility_tau']
visibility_z = 0.0013*vis['visibility_z']
visibility_z2 = 0.0445*vis2['visibility_z']
visibility_z3 = 0.217*vis3['visibility_z']
visibility_z4 = 0.0005*vis4['visibility_z']

ax = plt.subplot(111)
ax.set_xscale('log')
#ax.set_yscale('log')

ax.set_xlim(1E2,1E10)
#ax.set_ylim(0,1.6e-7)

#ax.plot(z, opacity,'r',z2, opacity2,'b--',z3, opacity3,'g-.')
#ax.plot(z1, tau,c='m')

#ax.plot(z1, visibility_z,c='blue')
#ax.plot(tau, visibility_tau,c='blue')

ax.plot(z1,visibility_z, 'g',z2, visibility_z2,'r--',z3, visibility_z3,'b',z4, visibility_z4,'k',linewidth = 2.5)
#ax.plot(z1,visibility_z, 'g',z2, visibility_z2,'r--',z3, visibility_z3,'b',linewidth = 2.5)
#ax.plot(z4,visibility_z4, 'g',linewidth = 2.5)
#mart.setp(lines, linewidth=2)
#plt.setp(lines, linewidth=2.0)

#ticklabels = ax.get_xticklabels()
#ticklabels.extend( ax.get_yticklabels() )

#for label in ticklabels:
#label.set_color('k')
#label.set_fontsize('medium')

plt.xlabel('$z$',size = 18)
#plt.ylabel('Opacity',size = 18)
plt.ylabel('$g_{\\nu}(z)$',size = 18)

#leg = ax.legend(('Neutrino Opacity','Comoving Hubble Horizon'),'upper left')
#leg = ax.legend(('$G_{\\rm eff} = 10^{-4}{\\rm MeV}^{-2}$','$G_{\\rm eff} = 10^{-5}{\\rm MeV}^{-2}$','$G_{\\rm eff} = 10^{-6}{\\rm MeV}^{-2}$'),'upper left')
#leg = ax.legend(('$G_{\\rm eff} = 10^{-3}{\\rm MeV}^{-2}$','$G_{\\rm eff} = 10^{-4}{\\rm MeV}^{-2}$','$G_{\\rm eff} = 10^{-5}{\\rm MeV}^{-2}$','$G_{\\rm eff} = 10^{-6}{\\rm MeV}^{-2}$'),'upper left')
#leg = ax.legend(('$G_{\\rm eff} = 10^{-3}{\\rm MeV}^{-2}$','$G_{\\rm eff} = 10^{-4}{\\rm MeV}^{-2}$','$G_{\\rm eff} = 10^{-5}{\\rm MeV}^{-2}$'),'upper left')
#plt.savefig('../Plots/opacity_z_geff_paper.pdf')

plt.show()



