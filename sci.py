import numpy as np
from scipy.optimize import minimize

def rosen(x):
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0+(1-x[:-1])**2.0)
# x=[0,1,2,3,4]
# print(x[1:])
# print(x[:-1])
x0=np.array([1.3,0.7,0.8,1.9,1.2])
res=minimize(rosen,x0,method="nelder-mead",options={"xtol":1e-8,"disp":True})
print("ROSE MINI:",res.x)
def func(x):
    return (2*x[0]*x[1]+2*x[0]-x[0]**2-2*x[1]**2)
def func_deriv(x):
    dfdx0=(-2)

