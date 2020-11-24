import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

pi = np.pi
sin = np.sin
N = 10

def x(t, t0):
    if(t >= 0.0 and t <= t0):
        return 1.0
    else:
        return 0.0
    
def xN(t, t0, N):
    xNtotal = 0.0
    x0 = t0/(2.0*pi)
    sum = 0
    for k in range(1, N+1):
        sum += 1.0/k * (sin(k*t)-sin(k*(t-t0)))
    xNtotal = x0 + sum/pi
    return xNtotal

def calculateError(tArray, xArray):
    e = 0.0
    for i in range(len(tArray)):
        if(np.abs(tArray[i] - xArray[i]) >e):
            e = np.abs(tArray[i]-xArray[i])
    return e


t0 = np.pi
tValues = list(np.arange(0.0, np.pi*2.0, 0.01))
Nlist = [1000]
errorList = []
errorListL2 = []
tValues.append(2*np.pi)

def L2Error(xArray, xNArray, tArray):
    func = []    
    for i in range(len(tArray)):
        l2 = (xArray[i] - xNArray[i])
        l2squared = l2**2
        func.append(l2squared)
    integral = simps(func, tArray)
    #print integral
    error = np.sqrt(integral)
    #print error
    return error

xValues = []
for t in tValues:
    xValues.append(x(t, t0)) 
        
for N in Nlist:
    xNValues = []
    for t in tValues:
        xNValues.append(xN(t, t0, N))
    error = calculateError(xValues, xNValues)
    eL2 = L2Error(xValues, xNValues, tValues)
    errorList.append(error)
    errorListL2.append(eL2)
  
print errorList  
print errorListL2
    
# =============================================================================
# plt.figure(1,figsize=(20, 15))
# plt.subplot(222)
# plt.title('Trapezoid Method')
# plt.plot(tValues, xValues,label = 'x values')
# plt.plot(tValues, xNValues,label = 'xN values')
# plt.legend()
# plt.grid(True)
# plt.show()
# #    
# 
# 
# =============================================================================
