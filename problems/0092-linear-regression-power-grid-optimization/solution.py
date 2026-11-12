import math
import numpy as np
PI = 3.14159

def func(a:int,ind:int):
    return 10*math.sin((2*PI*ind)/10)
def power_grid_forecast(consumption_data):
    # 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
    # 2) Perform linear regression on the detrended data.
    # 3) Predict day 15's base consumption.
    # 4) Add the day 15 fluctuation back.
    # 5) Round, then add a 5% safety margin (rounded up).
    # 6) Return the final integer.
    dataset=np.array(consumption_data)
    y_new=[]
    x=np.column_stack((np.ones(10),np.arange(1,11)))
    for i in range(len(dataset)):
        y_new.append(dataset[i]-func(dataset[i],i+1))
    y=np.array(y_new)
    theta=(np.linalg.inv(x.T@x))@(x.T@y)
    y_15=theta[0]+theta[1]*15
    y_15_pred=y_15+func(y_15,15)
    val=math.ceil(y_15_pred*1.05)

    return val
     