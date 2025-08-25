#!/usr/bin/env python3
"""
Simple script to run the unit tests for the Sweet Dreams Bakery API.

This script provides an easy way to run all tests with proper coverage reporting.
"""

import subprocess
import sys
import os

def run_tests():
    """Run the unit tests with verbose output"""
    
    # Check if pytest is available
    try:
        result = subprocess.run([
            "/home/ubuntu/.local/bin/pytest", 
            "test_main.py", 
            "-v", 
            "--tb=short"
        ], check=False, capture_output=False)
        
        if result.returncode == 0:
            print("\n✅ All tests passed successfully!")
            print("\nTo run tests manually, use:")
            print("python3 -m pytest test_main.py -v")
        else:
            print("\n❌ Some tests failed. Check the output above for details.")
            
        return result.returncode
        
    except FileNotFoundError:
        print("❌ pytest not found. Please install dependencies first:")
        print("python3 -m pip install --break-system-packages -r requirements.txt")
        return 1

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)