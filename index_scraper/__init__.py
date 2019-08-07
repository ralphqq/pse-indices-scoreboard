import os
import sys

# Append current directory to sys.path
S_ROOT = os.path.abspath(os.path.dirname(__file__))
if S_ROOT not in sys.path:
    sys.path.append(S_ROOT)
