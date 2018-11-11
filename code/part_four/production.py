"""Define and evaluate production functions."""

# Define Input values
factors = map(int, input('Input factors separated by ", " ').split(', '))

# Define parameters
weights = map(int, input('Input weights separated by ", " ').split(', '))
a = []

# Define Production functions
def general_cobb_douglas(factors, weights, a):
    """Return the value of a general Cobb-Douglas function with
	inputs *factors* and technology parameters *a* and *weights*.
	"""
    output = a
    for i in factors:
        output = output * factors[i] ** weights[i]
        
    return output

def general_ces(factors, weights, a, rho):
    """Return the value of a Constant Elasticity of Subsititution 
    production function with inputs *factors* and technology parameters
    *a* and *weights*.
	"""
    output = a
    for i in factors:
        output = output * sum(weights[i]*factors[i]**(-rho))**(-1/rho)
    
    return output

def robust_general_ces(factors, weights, a, rho):
    """Return the value of a Constant Elasticity of Subsititution 
    production function with inputs *factors* and technology parameters
    *a* and *weights*.
	"""
    output = a
    if rho == 0:
        for i in factors:
            output = output * factors[i] ** weights[i]
            
        return output
    else:
        for i in factors:
            output = output * sum(weights[i]*factors[i]**(-rho))**(-1/rho)
        
        return output

# Evaluate production functions.
