"""Define production functions."""


# define production functions
def general_cobb_douglas(factors, weights, a):
    """Return the value of a general Cobb-Douglas function with
	inputs *factors* and technology parameters *a* and *weights*.
	"""
    output = a
    for i in range(len(factors)):
        output = output * factors[i] ** weights[i]
        
    return output

def general_ces(factors, weights, a, rho):
    """Return the value of a Constant Elasticity of Subsititution 
    production function with inputs *factors* and technology parameters
    *a* and *weights*.
	"""
    output = 0
    for i in range(len(factors)):
        output = output + weights[i]*factors[i]**(-rho)
        
    output = a * output**(-1/rho)
    return output

def robust_general_ces(factors, weights, a, rho):
    """Return the value of a Constant Elasticity of Subsititution 
    production function with inputs *factors* and technology parameters
    *a* and *weights*. Particularly, when *rho* equals 0, this function
    will return the value of a general Cobb-Douglas function with 
    inputs *factors* and technology parameters *a* and *weights*, because
    when *rho* approaches zero, the output of the CES function is close to
    the output of the Cobb-Douglas function.
	"""
    if rho == 0:
        output = general_cobb_douglas(factors, weights, a)
        return output
    else:
        output = general_ces(factors, weights, a, rho)
        return output