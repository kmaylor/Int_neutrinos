from cosmoslik import *

class myscript(SlikPlugin):
    def __init__(self):
        super(SlikPlugin,self).__init__()
        
        # define sampled parameters
        self.a = param(start=0, scale=1)
        self.b = param(start=0, scale=1)
        
        # set the sampler
        self.sampler = get_plugin('samplers.metropolis_hastings')(
            self,
            num_samples=1e5, 
            output_file="myscript.chain",
        )

    def __call__(self):
        # compute the likelihood
        return (self.a**2 + self.b**2)/2
