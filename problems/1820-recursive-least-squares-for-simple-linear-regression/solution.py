import numpy as np
def run_mean(mean,new_val,n):
    return (mean*n+new_val)/(n+1)
def online_simple_regression(xs, ys):
    # return (N, 2) array of (w0, w1) after each point
    x_mean=0
    y_mean=0
    w1=0
    w2=0
    Cxx=0
    Cxy=0
    result=[]
    for i in range(len(xs)):
        x=xs[i]
        y=ys[i]
        x_old=x_mean
        y_old=y_mean
        x_mean=run_mean(x_mean,x,i)
        y_mean=run_mean(y_mean,y,i)
        Cxx=(i*Cxx+((x-x_mean)*(x-x_old)))/(i+1)
        Cxy=(i*Cxy+((x-x_mean)*(y-y_old)))/(i+1)
        if Cxx==0:
            w1=0
            w0=y_mean
            result.append((w0,w1))
        else:
            w1=Cxy/Cxx
            w0=y_mean-w1*x_mean
            result.append((w0,w1))

    return np.array(result)