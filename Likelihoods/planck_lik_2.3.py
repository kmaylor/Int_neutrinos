from cosmoslik import *
import os.path as osp
from numpy import exp, inf
import sys


        
param = param_shortcut('start','scale')
   
class planck(SlikPlugin):

    def __init__(self, model='lcdm'):
        super(SlikPlugin,self).__init__(**all_kw(locals()))
        highl_clik_file='/home/kmaylor/Official_Planck_likelihoods_2015/plc_2.0/hi_l/plik_lite/plik_lite_v18_TT.clik'
        lowl_clik_file = '/home/kmaylor/Official_Planck_likelihoods_2015/plc_2.0/low_l/commander/commander_rc2_v1.1_l2_29_B.clik'
        self.cosmo = get_plugin('models.cosmology')(
            model='lcdm',
            pivot_scalar = 0.05,
        l_max_scalar=4000,
        )
        self.cosmo.tau = param(0.066,0.02,min=.01,gaussian_prior=(0.066,0.02)) 
        self.cosmo.log10_G_neff = param(-1.5,.16,min=-5,max=0)
        self.cosmo.int_nu_f = .666666
        
        self.high_l = get_plugin('likelihoods.clik')(
            clik_file=highl_clik_file,
        A_Planck         = param(1,   0.0025, range=(0.9,1.1), gaussian_prior=(1,0.0025)),
            
            )
        self.low_l = get_plugin('likelihoods.clik')(
            clik_file=lowl_clik_file,
            A_Planck=None
            )
        self.get_cmb = get_plugin('models.camb')()
        self.bbn = get_plugin('models.bbn_consistency')()
        #self.hubble_theta = get_plugin('models.hubble_theta')()
        self.priors = get_plugin('likelihoods.priors')(self)

        self.sampler = get_plugin('samplers.metropolis_hastings')(
             self,
             num_samples=200000,
             output_file='/home/kmaylor/int_neutrinos/Saved_chains/annealing_chain_%s_%s.chain'%(model,osp.basename(highl_clik_file)+osp.basename(lowl_clik_file)),
             #proposal_cov='/home/kmaylor/Python_Projects/cosmoslik_proposal_covmats/SPT_chainz_h1h2.covmat',
             proposal_scale=1,
             print_level=2,
             output_extra_params=['cosmo.Yp','cosmo.theta','cosmo.G_neff']
        )

    def __call__(self):
        self.low_l.A_planck = self.high_l.A_Planck
        self.cosmo.As = exp(self.cosmo.logA)*1e-10
        self.cosmo.G_neff = 10**(self.cosmo.log10_G_neff)
        if 'yp' not in self.model: self.cosmo.Yp = self.bbn(**self.cosmo)
        if self.priors(self) != inf:
                
                self.cmb_result = self.get_cmb(outputs=['cl_TT'],**self.cosmo)
                self.cosmo.theta = self.cmb_result['100theta']
                return lsum(lambda: self.priors(self),
                    lambda: self.high_l(self.cmb_result),
                    lambda: self.low_l(self.cmb_result))
            
        else: 
            return inf
