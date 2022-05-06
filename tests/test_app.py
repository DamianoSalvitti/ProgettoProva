import sys
import os

# Reach the parent's path
f_path = os.path.dirname(__file__)
root_path = os.path.join(f_path, os.pardir)
sys.path.append(os.path.abspath(root_path))

# Import of the desired module
import src.compute_flask_cv.app as a

# pytest
def test_homepage():
    assert a.homepage() == "Hello"
