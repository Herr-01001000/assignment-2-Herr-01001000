# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 01:28:05 2018

@author: Wenxin Hu
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