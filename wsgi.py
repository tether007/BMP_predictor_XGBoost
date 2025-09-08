import sys
import os

# Add your project directory to the Python path
path = '/home/yourusername/bmp-predictor'
if path not in sys.path:
    sys.path.append(path)

# Import your FastAPI app
from app import app

# This is the WSGI application that PythonAnywhere will use
application = app
