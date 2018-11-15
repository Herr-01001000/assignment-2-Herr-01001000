# -*- coding: utf-8 -*-
"""Print statements to see which variables are defined in the namespaces of
your modules or functions.
"""

# Print all local variables, excluding some built-in variables.
print('\n\nLocal variables in INDICATE MODULE OR FUNCTION):')
item = ''
for item in sorted(locals()):
    if not item.startswith('_'):
        print(item)

# Print all global variables, excluding some built-in variables.
print('\nGlobal variables in INDICATE MODULE OR FUNCTION:')
for item in sorted(globals()):
    if not item.startswith('_'):
        print(item)