#!/usr/bin/python

import numpy as np
import os


def create_points(number):
    """Create a random set of 2D points of size number where no two
    points have the same x or same y coordinates
    :param number: of points to create
    :return : list of 2D points
    """ 

    # generate x and y coordinates:
    x = np.random.permutation(2*number)[:number] - number
    y = np.random.permutation(2*number)[:number] - number

    points = [ { 0 : float(x[i]), 1 : float(y[i]), "index" : i} for i in range(len(x)) ]

    return points

    # generate points as coordinate pairs of floats.
    # return zip(map(float,x),map(float,y))

def create_weighted_intervals(number) :

    # finish times
    f = 6 + np.random.permutation(2*number)
    # durations
    l = np.random.randint(2,7, 2*number)
    # weights
    w = np.random.randint(3,9, 2*number)
    n = "ABCDEFGH"
    
    intervals = [{ "name": n[i], "start" : int(f[i] - l[i]), "finish": int(f[i]), "value": int(w[i]) } for i in range(int(len(w)/ 2)) ]

    return intervals

def check_seed():
    """Checks whether random number generator works the same as on my
    maas expected. 
    """
    np.random.seed(1000)
    standard = [
        {0: -3.0, 1: -5.0, 'index': 0},
        {0: -6.0, 1: -8.0, 'index': 1},
        {0: 5.0, 1: -1.0, 'index': 2},
        {0: 1.0, 1: -7.0, 'index': 3},
        {0: -2.0, 1: -3.0, 'index': 4},
        {0: 7.0, 1: 3.0, 'index': 5},
        {0: -4.0, 1: -2.0, 'index': 6},
        {0: 2.0, 1: 6.0, 'index': 7}
    ]

    this_machine = create_points(8)

    flag = True
    for i in range(8) :
        flag &=  this_machine[i][0] == standard[i][0] 
        flag &=  this_machine[i][1] == standard[i][1] 
        flag &=  this_machine[i]["index"] == i
    
    if not flag :
        print("""
        The Python installation on this machine is odd: it appears to
        use a non-standard random number generator -- run 
        this  script on the machines in the Otter lab instead.
        If that fails too, send an email to ag0015@surrey.ac.uk.
        """)
        print ("You got these test points:", this_machine)
        print ("You should have got:", standard)
        exit(-1)
    else :
        print ("Check passed")

if __name__== "__main__" :

    check_seed()

    if len(os.sys.argv) != 2 :
        print ("Call as follows where <URN> is replaced by your 7-digit URN:")
        print ("python " + os.sys.argv[0] + " <URN>")
        exit(-1)

    urn = os.sys.argv[1]
    if len(urn) != 7 :
        print ("Your URN must have 7 digits.")
        exit(-1)
    if int(urn) == 0:
        print ("""
        Your URN cannot be converted to an integer number: Only
        digit are allowed.
        """)

    np.random.seed(int(urn))

    points = create_points(8)
    intervals = create_weighted_intervals(8)

    print("""
List of points S for Question 1:
    """)

    for p in points :
        print("index: {}, coordinates: {}".format(p["index"], (p[0],p[1])))



    print("""
List of intervals for Question 2:
    """)
    for i in intervals:
        print("name {}: start: {}\t finish: {}\t  value: {}".format(i["name"], i["start"], i["finish"], i["value"]))

        # copy from extra
