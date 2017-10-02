#! /usr/bin/env python

import subprocess
from sys import argv
import numpy as np
import matplotlib.pyplot as plt
methods=["TDM","ATC"]
states=range(1,5)


for method in methods:
    a=np.zeros((len(states),len(states)))
    if method=="TDM":
        for i in states:
            for j in states:
                print "Working on {0}_{1}-{2}.txt...".format(argv[1],i,j)
                #subprocess.call("./diabatization.py -p TDM -s {0} {1} -i {2} {3} {4} >{5}_{6}-{7}.txt".format(i,j,argv[1],argv[2],argv[3],argv[1],i,j),shell=True)
                b=subprocess.Popen("./diabatization.py -p TDM -s {0} {1} -i {2} {3} {4}".format(i,j,argv[1],argv[2],argv[3]),shell=True,stdout=subprocess.PIPE)

                a[i-1,j-1]=float(b.communicate()[0])
                print a

        plt.matshow(a)
        plt.colorbar()
        plt.show()

    elif method=="ATC":
        for i in states:
            for j in states:
                print "Working on {0}_{1}-{2}.txt...".format(argv[1],i,j)
                b=subprocess.Popen("./diabatization.py -p ATC -s {0} {1} -i {2}-{0}.out {2}-{1}.out {3} {4} {5}".format(i,j,argv[1],argv[2],argv[3],argv[4]),shell=True,stdout=subprocess.PIPE)

                a[i-1,j-1]=float(b.communicate()[0])
                print a

        plt.matshow(a)
        plt.colorbar()
        plt.show()
