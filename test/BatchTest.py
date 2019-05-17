# -*- coding: utf-8 -*-
""" Batch Test on All Unit Tests
description:
    This is the batch test file for all the unit test in this folder.
reference: 
    1. https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2017/06/09
    - 2019/05/10 fix __import__ issues
"""
import os
import sys
import unittest

def Main():
    
    current_script = os.path.basename(__file__)    
    test_files = os.listdir(os.path.dirname(__file__))
    testmodules = [filename.replace('.py', '') for filename in test_files if 
                   filename != current_script and filename.endswith('.py')]
    
    suite = unittest.TestSuite()
    
    for t in testmodules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            units = [mod.__dict__[key] for key in mod.__dict__.keys() if key.lower().startswith('test')]
            for unit in units:
                suite.addTest(unittest.TestLoader().loadTestsFromTestCase(unit))
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
    
    u = unittest.TextTestRunner(sys.stdout, verbosity=2).run(suite)
    
if __name__ == '__main__':    
    Main()