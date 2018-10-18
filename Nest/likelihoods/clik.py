from __future__ import absolute_import
from numpy import hstack, zeros, arange, pi, inf, nan

class clik(object):
    """
    
    """
    
    def __init__(self,
                 clik_file,
                 ):
        

        from clik import clik as _clik
        self.clik = _clik(clik_file)            
        
    def __call__(self, cmb, params):
        
        cl = hstack(tocl(cmb.get('cl_%s'%x,zeros(lmax+1))[:lmax+1])
                    for x, lmax in zip(['TT','EE','BB','TE','TB','EB'],self.clik.get_lmax()) 
                    if lmax!=-1)
        nuisance = [params['A_Planck']]
        lnl = -self.clik(hstack([cl,nuisance]))[0]
        if lnl==0: return inf
        else: return lnl
            
    
def tocl(dl): 
    return hstack([zeros(2),dl[2:]/arange(2,dl.size)/(arange(2,dl.size)+1)*2*pi])
    
