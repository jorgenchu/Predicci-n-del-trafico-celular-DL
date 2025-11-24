import sys
import os

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

try:
    import matplotlib
    print(f"Matplotlib version: {matplotlib.__version__}")
    print(f"Matplotlib file: {matplotlib.__file__}")
    if hasattr(matplotlib, 'get_data_path'):
        print(f"matplotlib.get_data_path() exists: {matplotlib.get_data_path()}")
    else:
        print("ERROR: matplotlib.get_data_path does NOT exist.")
except ImportError as e:
    print(f"Error importing matplotlib: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    import pandas as pd
    print(f"Pandas version: {pd.__version__}")
except ImportError:
    print("Pandas not installed")

try:
    import dask
    print(f"Dask version: {dask.__version__}")
except ImportError:
    print("Dask not installed")
