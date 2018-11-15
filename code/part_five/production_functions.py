"""Define production functions."""


# define production functions
def general_cobb_douglas(factors, weights, a):
    """Return the value of a general Cobb-Douglas function with
	inputs *factors* and technology parameters *a* and *weights*.
    The list *factors* and *weights* should have the same length.
	"""
    if len(factors) == len(weights):
        output = a
        for i in range(len(factors)):
            output = output * factors[i] ** weights[i]
        
        return output
    else:
        print("Error: Factors and weights don't have the same length.")

def general_ces(factors, weights, a, rho):
    """Return the value of a Constant Elasticity of Subsititution 
    production function with inputs *factors* and technology parameters
    *a* and *weights*. The list *factors* and *weights* should have 
    the same length.
	"""
    if len(factors) == len(weights):
        output = 0
        for i in range(len(factors)):
            output = output + weights[i]*factors[i]**(-rho)
            
        output = a * output**(-1/rho)
        return output
    else:
        print("Error: Factors and weights don't have the same length.")

def robust_general_ces(factors, weights, a, rho):
    """Return the value of a Constant Elasticity of Subsititution 
    production function with inputs *factors* and technology parameters
    *a* and *weights*. Particularly, when *rho* equals 0, this function
    will return the value of a general Cobb-Douglas function with 
    inputs *factors* and technology parameters *a* and *weights*, because
    when *rho* approaches zero, the output of the CES function is close to
    the output of the Cobb-Douglas function. The list *factors* and *weights* 
    should have the same length.
	"""
    if len(factors) == len(weights):
        if rho == 0:
            output = general_cobb_douglas(factors, weights, a)
            return output
        else:
            output = general_ces(factors, weights, a, rho)
            return output
    else:
        print("Error: Factors and weights don't have the same length.")