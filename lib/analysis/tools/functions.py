import numpy as np
import math


def convertPtsToSparseImage(data, params, spacing=5e-6):
    """Function for converting a list of stimulation spots and their associated values into a fine-scale smoothed image.
           data - a numpy record array which includes fields for 'xPos', 'yPos' and the parameters specified in params.
           params - a list of values to set
           spacing - the size of each pixel in the returned grid (default is 5um)
           
        Return a 2D record array with fields for each param in params - if 2 or more data points fall in the same grid location
        their values are averaged.
        """
    if len(params) == 0:
        return
    ## sanity checks
    if params==None:
        raise Exception("Don't know which parameters to process. Options are: %s" %str(data.dtype.names))
    if 'xPos' not in data.dtype.names or 'yPos' not in data.dtype.names:
        raise Exception("Data needs to have fields for 'xPos' and 'yPos'. Current fields are: %s" %str(data.dtype.names))
      
    ### Project data from current spacing onto finer grid, averaging data from duplicate spots
    xmin = data['xPos'].min()
    ymin = data['yPos'].min()
    xdim = int((data['xPos'].max()-xmin)/spacing)+5
    ydim = int((data['yPos'].max()-ymin)/spacing)+5
    dtype = []
    for p in params:
        dtype.append((p, float))
    dtype.append(('stimNumber', int))
    #print xmin, data['xPos'].max(), spacing
    #print len(data[data['xPos'] > 0.002]) + len(data[data['xPos'] < -0.002])
    #print np.argwhere(data['xPos'] > 0.002)
    #print xdim, ydim
    arr = np.zeros((xdim, ydim), dtype=dtype)
    for s in data:
        x, y = (int((s['xPos']-xmin)/spacing), int((s['yPos']-ymin)/spacing))
        for p in params:
            arr[x,y][p] += s[p]
        arr[x,y]['stimNumber'] += 1
    arr['stimNumber'][arr['stimNumber']==0] = 1
    for f in arr.dtype.names:
        arr[f] = arr[f]/arr['stimNumber']
    #arr = arr/arr['stimNumber']
    arr = np.ascontiguousarray(arr)
    
    return arr


def bendelsSpatialCorrelationAlgorithm(data, radius, spontRate, timeWindow, printProcess=False):
    ## check that data has 'xPos', 'yPos' and 'numOfPostEvents'
    #SpatialCorrelator.checkArrayInput(data) 
    fields = data.dtype.names
    if 'xPos' not in fields or 'yPos' not in fields or 'numOfPostEvents' not in fields:
        raise HelpfulException("Array input needs to have the following fields: 'xPos', 'yPos', 'numOfPostEvents'. Current fields are: %s" %str(fields))   
    
    ## add 'prob' field to data array
    if 'prob' not in data.dtype.names:
        arr = np.zeros(len(data), dtype=data.dtype.descr + [('prob', float)])
        arr[:] = data     
        data = arr
    else:
        data['prob']=0
        
    
    ## spatial correlation algorithm from :
    ## Bendels, MHK; Beed, P; Schmitz, D; Johenning, FW; and Leibold C. Etection of input sites in 
    ## scanning photostimulation data based on spatial correlations. 2010. Journal of Neuroscience Methods.
    
    ## calculate probability of seeing a spontaneous event in time window
    p = 1-np.exp(-spontRate*timeWindow)
    if printProcess:
        print "======  Spontaneous Probability: %f =======" % p
    ## for each spot, calculate the probability of having the events in nearby spots occur randomly
    for x in data:
        spots = data[(np.sqrt((data['xPos']-x['xPos'])**2+(data['yPos']-x['yPos'])**2)) < radius]
        nSpots = len(spots)
        nEventSpots = len(spots[spots['numOfPostEvents'] > 0])
        
        prob = 0
        for j in range(nEventSpots, nSpots+1):
            a = ((p**j)*((1-p)**(nSpots-j))*math.factorial(nSpots))/(math.factorial(j)*math.factorial(nSpots-j))
            #prob += ((p**j)*((1-p)**(nSpots-j))*math.factorial(nEventSpots))/(math.factorial(j)*math.factorial(nSpots-j))
            if printProcess:
                print "        Prob for %i events: %f     Total: %f" %(j, a, prob+a)
            prob += a
        #j = arange(nEventSponts, nSpots+1)
        #prob = (((p**j)*((1-p)**(nSpots-j))*np.factorial(nEventSpots))/(np.factorial(j)*np.factorial(nSpots-j))).sum() ## need a factorial function that works on arrays
        if printProcess: ## for debugging
            print "    %i out of %i spots had events. Probability: %f" %(nEventSpots, nSpots, prob)
        x['prob'] = prob
    
    return data