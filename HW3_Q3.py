p

t0 = 3
pi = np.pi
sin = np.sin
N = 10
T = 2*pi
tValues = list(np.arange(0.0, np.pi*2.0, 0.01))
Nlist = [10]
errorList = []
errorListL2 = []

def x(t, t0):
    if(t >= 0.0 and t <= t0):
        return 1.0
    else:
        return 0.0

def pk(t, N):
    pkvalues = []
    p0 = (t0**2)/(4*(pi**2))
    pkvalues.append(p0)
    for N in Nlist:
        for k in range(1, N):
            value = (1-np.cos(k*t0))/(2*(pi**2)*(k**2))
            pkvalues.append(value)
    return pkvalues

tVals = []
for N in Nlist:
    for n in range(0, N):
        tValues = (n*T)/N
        tVals.append(tValues)

#print tVals

xValues = []
for t in tVals:
    xValues.append(x(t, t0)) 
#print xValues
        

pkTildaValues = pk(t0, Nlist)
#print pkTildaValues
# =============================================================================
# print pkvals
# =============================================================================

def fourierTransform(k, x, N):
    sum = 0
    for n in range(N):
        sum += np.e**((-2*pi*1j*k*n)/N)*x[n]
    total = 1.0/N * sum
    return total

xkhat = []
for k in range(N):
    xkhat.append(fourierTransform(k, xValues, N))
#print len(xkhat)

pkHatValues = []
for i in xkhat:
    pkHatValue = (np.abs(i))**2
    pkHatValues.append(pkHatValue)

    
#print pkHatValues

Nvalues = []
for g in range(N):
    Nvalues.append(g)
    
#print Nvalues

# =============================================================================
# fourier = list(((np.fft.rfft(xValues)/N)**2).real)
# #print fourier
# 
#     
# # =============================================================================
# # print xkhat
# # =============================================================================
# reverse = list(fourier[::-1])
# reverseT = reverse[1:500]  ## middle of total values
# #print reverseT
# 
# fourierT = fourier + reverseT
# 
# 
# print fourierT
# =============================================================================


plt.figure(1,figsize=(20, 15))
plt.subplot(222)
plt.title('pk comparisons')
plt.plot(Nvalues, pkHatValues,linestyle="",marker="o",label = 'pk ^ values')
plt.plot(Nvalues, pkTildaValues,linestyle="",marker="*", label = 'pk ~ values')
#plt.plot(Nvalues, fourierT,linestyle="",marker="o")
#plt.plot(Nvalues, fourierT,label = 'pk hat fft values')
plt.yscale("log");
plt.legend()
plt.grid(True)
plt.show()
#    



