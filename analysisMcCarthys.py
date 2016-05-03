#analysis of mccarthy's data
import numpy as np
import csv
import pylab as plt
import pymc as pm
from sklearn import mixture
import sys
from scipy.stats import beta
def gaussian(x, mu, sig):
    return (1/(sig*np.sqrt(2*np.pi)))*np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
filename = "C:\Users\leon\Documents\Data\McCarthys.dat"
raw_data = list(csv.reader(open(filename, 'rb')))
data = np.zeros((256,2))
for idx,line in enumerate(raw_data):
    data[idx, :] =  line[0].split()
master_data = np.array([])
for line in data:
    new_data = np.repeat(line[0], line[1])
    master_data = np.append(master_data, new_data)
master_data = master_data[:, None]
#clf = mixture.GMM(n_components=2, )
#clf.fit(master_data)
#plt.hist(master_data, 100, normed = True)
#plt.plot(gaussian(np.linspace(0,50,100), clf.means_[0], clf.covars_[0]))
#plt.plot(gaussian(np.linspace(0,50,100), clf.means_[1], clf.covars_[1]))
sys.exit()
[alpha, beta, loc, scale] = beta.fit(master_data)