# RandomNumberManager
This is a Python module for management of random number generator of numpy.random.
## Installation
Installation by pip from github.
```
pip install git+https://github.com/yy-harashima/RandomNumberManager.git
```
Update.
```
pip install git+https://github.com/yy-harashima/RandomNumberManager.git -U
```
## Usage
Random number stream state is saved in the file 'rng_state.dat' by default.
```
import numpy as np
import rnmanager

rng = rnmanager.RandomNumberManager()
rng.restoreState()
np.random.rand()
rng.storeState()
```