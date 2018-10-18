from cosmoslik import *
import os.path as osp
from numpy import exp, inf
import sys

param = param_shortcut('start','scale')
   
class SPT(SlikPlugin):

    def __init__(self,model='lcdm'):
        super(SlikPlugin,self).__init__(**all_kw(locals()))
        
        self.cosmo = get_plugin('models.cosmology')(
            model='lcdm',
            #tau = param(0.088,0.015,min=0,gaussian_prior=(0.088,0.015)),
            pivot_scalar = 0.05,
	    l_max_scalar=4000,	
        )
        self.cosmo.tau = param(0.066,0.02,min=0,gaussian_prior=(0.066,0.02)) 
        self.cosmo.G_neff = param(0,0.01)
        self.cosmo.int_nu_f = 1
        #self.cosmo.ombh2 =0.02222 #0.0104085159
         #0.0104085159  
        self.s12 = get_plugin('likelihoods.spt_lowl')(
     			        which = 's12',
                                
                              
                                #lmax = 2000,
                                #lmin = 1500,
				#drop = range(7,17),
                cal = param(0.983,0.0015,min=0,gaussian_prior=(0.983,0.0015)),
                fgs = get_plugin('models.clust_poisson_egfs')(
		    	#Asz = param(5.5,3,min=0, gaussian_prior=(5.5,3)),	
                    	Aps = param(19.3,3.5,min=0,gaussian_prior=(19.3,3.5)),
                    	Acib = param(5,2.5,min=0,gaussian_prior=(5,2.5)), 
                    	ncib=.8,
                        #beta_p = 0,#param(1.5,3,uniform_prior=(.5,3.5)),
                    	#beta_c = 0,#param(1.5,3,uniform_prior=(.5,3.5))
                    	#xi = param(0.113,0.05,min=0,gaussian_prior=(0.113,0.05)),
                		),
                           )
        
        self.sampler = get_plugin('samplers.metropolis_hastings')(
             self,
             num_samples=200000,
             output_file='/home/kmaylor/int_neutrinos/Saved_chains/SPT_chainz_h1h2.chains',
             proposal_cov='/home/kmaylor/Python_Projects/cosmoslik_proposal_covmats/SPT_chainz_h1h2.covmat',
	         print_level=2,
	         proposal_scale = 1,
             output_extra_params=['cosmo.Yp','cosmo.H0'],
             
        )
        
        self.get_cmb = get_plugin('models.camb')()
        self.bbn = get_plugin('models.bbn_consistency')()
        self.hubble_theta = get_plugin('models.hubble_theta')()
        self.priors = get_plugin('likelihoods.priors')(self)
        
    def __call__(self):
        if self.cosmo.tau >= .01:
            self.cosmo.As = exp(self.cosmo.logA)*1e-10
            if 'yp' not in self.model: self.cosmo.Yp = self.bbn(**self.cosmo)
            self.cosmo.H0 = self.hubble_theta.theta_to_hubble(**self.cosmo)
	
            self.cmb_result = self.get_cmb(outputs=['cl_TT'],**self.cosmo)
		
               
	    return lsum(lambda: self.priors(self),
                    lambda: self.s12(self.cmb_result,self.s12.fgs(**self.s12.fgs)))
	else: return inf





