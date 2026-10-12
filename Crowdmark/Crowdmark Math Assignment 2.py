#Input parameters (change these for each test case)
import numpy as np
#change the values below to test your code
#Input parameters. Adapt these to test your code.
a = 1
b = 10
max_iter = 1000
tolerance = 1e-10
def f(x):

    # The function whose root we want. Uncomment exactly one return line per test
    #TEST 1
    return np.exp(x/10) + np.log(x/10)
    #TEST 2
    #return np.arctan(x) - x**2
    #TEST 3
    #return np.sin(x)/np.log(x)
    #TEST 4
    #return np.log(np.cos(x))

#  Variables that track the result
#Whether an approximate root has been found
root_approximated = False
#Value of the approximate root (if found)
approximate_root = None
#Failure reason (if the algorithm fails)
bisection_failure = False
bisection_failure_reason = ""
#A variable to store the number of iterations
i = 0
# the left and right endpoint of the interval at each step
L = a
R = b
#check the endpoints
if f(L) == 0:
    root_approximated = True
    approximate_root = L
elif f(R) == 0:
    root_approximated = True
    approximate_root = R
#check the Intermediate Value Theorem condition
elif f(L) * f(R) > 0:
    bisection_failure = True
    bisection_failure_reason = "Bisection method does not apply: f(a) and f(b) have the same sign."

   
else:
    while not root_approximated and i < max_iter:
        c= (L + R) / 2
        if f(c) == 0 or abs(R - L) < tolerance:
            root_approximated = True
            approximate_root = c
        elif f(c) * f(L) > 0:
            L = c  
        else:
            R = c
        i += 1
#handle running out of iterations
if not root_approximated and not bisection_failure:
    bisection_failure = True
    bisection_failure_reason = "Reached maximum amount of attempts"


#print the outcome
if root_approximated:
    print("Success! Approximate root:", approximate_root)
    print("Iterations:", i)
    print("f(approximate_root):", f(approximate_root))
else:
    print("Failed:", bisection_failure_reason)
