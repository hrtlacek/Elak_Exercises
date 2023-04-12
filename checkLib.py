import numpy as np
from sillyQuotes import getMsg
import matplotlib.pyplot as plt

def checkEx01(y):
    corr = False
    try:
        t = np.linspace(0, 2*np.pi,100)
        x = np.sin(t)
        err = np.average((y-x)**2)
        corr = err<1e-6
        getMsg(corr)
    except:
        getMsg(corr)
    return corr
        
def checkEx03(y):
    x = np.arange(11)
    corrSol = x[::-1]
    corr = np.array_equal(y,corrSol)
    getMsg(corr)
    return corr


def checkEx04(fun):
    x = np.random.random(20)
    y = fun(x)
    corr = np.alltrue(np.isclose(y-1, x))
    getMsg(corr)
    return corr

def checkEx05(fun):
    x = abs(np.random.random(20))
    y = fun(x)
    corr = np.alltrue(np.isclose(y, 20*np.log10(x)))
    getMsg(corr)
    return corr

def checkEx06(fun):
    corr = True
    for i in range(20):
        x = abs(np.random.random(i))
        corrVal = len(x)>10
        outVal = fun(x) 
        if corrVal != outVal:
            corr=False

    getMsg(corr)
    return corr

def checkEx07(fun):
    N = 100
    x = np.linspace(-2, 2, N)
    corrVal = np.clip(x, -1,1)
    Y = np.zeros(N)
    for n in range(N):
        Y[n] = fun(x[n])
        
    corr = np.alltrue(np.isclose(corrVal, Y))
    if not corr:
        with plt.xkcd():
            plt.plot(x,corrVal,'k', label = 'What it should look like')
            plt.plot(x,Y, 'r--', label= 'What you are doing')
            plt.title ('Something seems off..')

    else:
        plt.plot(x,Y, 'g', label= 'Best Hard Clipper ever')
        plt.title('Success!')
        plt.grid()
        plt.xlabel('$x$')
        plt.ylabel('$y$')

    plt.legend()
    plt.show()

    
    getMsg(corr)
    return corr
    