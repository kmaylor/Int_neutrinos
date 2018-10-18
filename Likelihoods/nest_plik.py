import os.path as osp
from numpy import exp, inf, sum
import sys
from Nest.likelihoods.clik import clik
from Nest.models.camb import camb
from scipy.special import ndtri
           
class planck(object):

    def __init__(self):

        highl_clik_file='/home/kmaylor/Official_Planck_likelihoods_2015/plc_2.0/hi_l/plik_lite/plik_lite_v18_TT.clik'
        lowl_clik_file = '/home/kmaylor/Official_Planck_likelihoods_2015/plc_2.0/low_l/commander/commander_rc2_v1.1_l2_29_B.clik'
        
        param_names = ['log10_G_neff','tau','ombh2','omch2','logA','ns','H0','A_Planck']
        self.map_params = lambda x: dict(zip(param_names,x))
        
        self.high_l = clik(clik_file=highl_clik_file)
        self.low_l = clik(clik_file=lowl_clik_file)
        
        self.int_nu_f = 1
        self.get_cmb = camb()

    def Prior(self,cube):
        cube[0]=cube[0]*5-5
        cube[1]=cube[1]*.3+.01
        cube[2]=cube[2]*2.26e-03*2-2.26e-03+2.22e-02
        cube[3]=cube[3]*2.16e-02*2-2.16e-02+1.20e-01
        cube[4]=cube[4]*3.60e-01*2-3.60e-01+3.09
        cube[5]=cube[5]*6.20e-02*2-6.20e-02+9.65e-01
        cube[6]=cube[6]*9.57*2-9.57+6.73e+01
        cube[7]=ndtri(cube[7])*0.0025+1
        return cube     
        

    def LogLikelihood(self,cube):
        params = self.map_params(cube)
        #self.low_l.A_planck = params['A_Planck']
        params['As'] = exp(params['logA'])*1e-10
        params['G_neff'] = 10**(params['log10_G_neff'])
        params['int_nu_f']=self.int_nu_f
        self.cmb_result = self.get_cmb(outputs=['cl_TT'],**params)
        lnl= -sum([self.high_l(self.cmb_result,params),
                    self.low_l(self.cmb_result,params)])
        print lnl
        return lnl
      
