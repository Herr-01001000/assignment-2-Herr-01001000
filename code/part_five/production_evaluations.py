"""Evaluate production functions."""

from production_functions import robust_general_ces

# Define Input values
factors = []

# Define parameters
weights = []
a: int
rho: int

# Evaluate production functions.
# Evaluate robust CES production functions when *rho* is zero.
result = robust_general_ces(
    factors = [1, 2, 3], 
    weights = [0.1, 0.4, 0.5],
    a = 2,
    rho = 0
)

print('robust_general_ces')
print('factors = [1, 2, 3]')
print('weights = [0.1, 0.4, 0.5]')
print('a = 2')
print('rho = 0')
print('Expected result: 4.57')
print('Calculated result: ', result)
print('*****************************')

# Evaluate robust CES production functions when *rho* is not zero.
result = robust_general_ces(
    factors = [1, 2, 3], 
    weights = [0.1, 0.4, 0.5],
    a = 2,
    rho = 10
)

print('robust_general_ces')
print('factors = [1, 2, 3]')
print('weights = [0.1, 0.4, 0.5]')
print('a = 2')
print('rho = 10')
print('Expected result: 2.52')
print('Calculated result: ', result)
print('*****************************')