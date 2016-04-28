#analysis of mccarthy's data
import numpy as np
import csv
import pylab as plt
from pymc import *
filename = "C:\Users\leon\Documents\Data\McCarthys.dat"
raw_data = list(csv.reader(open(filename, 'rb')))
data = np.zeros((256,2))
for idx,line in enumerate(raw_data):
    data[idx, :] =  line[0].split()

 
theta = Uniform("theta", lower=0, upper=1)
bern = Bernoulli("bern", p=theta, size=len(data))
 
mean1 = Uniform('mean1', lower=min(data), upper=max(data))
mean2 = Uniform('mean2', lower=min(data), upper=max(data))
std_dev = Uniform('std_dev', lower=0, upper=50)
 
@deterministic(plot=False)
def mean(bern=bern, mean1=mean1, mean2=mean2):
    return bern * mean1 + (1 - ber) * mean2
 
@deterministic(plot=False)
def precision(std_dev=std_dev):
    return 1.0 / (std_dev * std_dev)
 
process = Normal('process', mu=mean, tau=precision, value=data, observed=True)