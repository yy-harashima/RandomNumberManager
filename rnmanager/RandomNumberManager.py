import os
import numpy as np

class RandomNumberManager:
    def __init__(self,seed=None,filename='rng_state.dat'):
        self.seed = seed
        self.filenameState = filename
        self.restored = False
        return

    ''' restore a random number stream state from a file or random seed. '''
    def restoreState(self, filename = None):
        if (not (filename is None)):
            self.filenameState = filename
        if (os.path.exists(self.filenameState)):
            with  open(self.filenameState,'r') as fileobj:
                lines = fileobj.readlines()
            rngstate = ['',np.empty(624,dtype=int),0,0,0.0]
            rngstate[0] = lines[0].strip()
            strtmp = lines[1].strip().split()
            for i in range(624):
                rngstate[1][i] = int(strtmp[i])
            rngstate[2] = int(lines[2])
            rngstate[3] = int(lines[3])
            rngstate[4] = float(lines[4])
            np.random.set_state(rngstate)
            self.seed = int(lines[5])
        else:
            if (self.seed == None):
                self.seed = np.random.randint(0,2**32-1)
            np.random.seed(self.seed)
            print('set random seed.')
        self.restored = True
        return

    ''' save a random number stream state into a file. '''
    def storeState(self, filename = None):
        if (not self.restored):
            print('Warning: not restored RandomState in Random Number Manager.')
            return
        if (not (filename is None)):
            self.filenameState = filename
        rngstate = np.random.get_state()
        with open(self.filenameState,'w') as fileobj:
            print(rngstate[0],file=fileobj)
            for i in range(624):
                print(' {}'.format(rngstate[1][i]),end='',file=fileobj)
            print('',file=fileobj)
            print(rngstate[2],file=fileobj)
            print(rngstate[3],file=fileobj)
            print(rngstate[4],file=fileobj)
            print(self.seed,file=fileobj)
        return

if (__name__=="__main__"):
    ### Usage example. ###
    print('Usage example.')
    import RandomNumberManager
    rnm = RandomNumberManager.RandomNumberManager()
    rnm.restoreState()
    print(np.random.uniform(0.0,1.0))
    rnm.storeState()
