#import os
#import sys
import warnings
import inspect
#import scipy as sp
#import sklearn as sk
#import matplotlib as matplt

#supress Tensorflow warnings
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

print(f"Entering {__name__} {inspect.stack()[0][3]}")

try:
    import pickle
    print(f"{'Pickle Version':<20}#: {pickle.format_version:<20}")
except Exception as e:
    pass

try:
    import sys
    print(f"{'System Version':<20}#: {sys.version:<20}")
except Exception as e:
    pass

try:
    import nltk
    print(f"{'NLTK Version':<20}#: {nltk.__version__:<20}")
except Exception as e:
    pass

try:
    import SpellChecker
    print(f"{'Spellchk Version':<20}#: {SpellChecker.__version__:<20}")
except Exception as e:
    pass

try:
    import NetCDF4
    netcdf4_version_info = nc.getlibversion().split(" ")
    print("netCDF4 version   #:{:>12}".format(netcdf4_version_info[0]))
except Exception as e:
    pass

try:
    import matplotlib as matplt
    print(f"{'Matplotlib Version':<20}#: {matplt.__version__:<20}")
except Exception as e:
    pass

try:
    import numpy as np
    print(f"{'Numpy Version':<20}#: {np.__version__:<20}")
except Exception as e:
    pass

try:
    import xarray as xr
    print(f"{'Xarray Version':<20}#: {xr.__version__:<20}")
except Exception as e:
    pass

try:
    import torch;
    print(f"{'Torch Version':<20}#: {torch.__version__:<20}")
    print(f"...are GPU's available: {torch.cuda.is_available()}")
    print(f"................count: {torch.cuda.device_count()}")
    print(f"..............current: {torch.cuda.current_device()}")
except Exception as e:
    pass


try:
    import cudf.pandas
    cudf.pandas.install()
    import pandas as pd
    print(f"{'Pandas Version':<20}#: {pd.__version__:<20}")
except Exception as e:
    pass

try:
    import tensorrt
    print(f"{'Tensorrt version':<20}#: {tensorrt.__version__:<20}")
except Exception as e:
    pass

try:
    import tensorflow as tf
    print(f"{'TensorFlow version':<20}#: {tf.__version__:<20}")
    print(f"{'Num GPUs Available':<20}#: " + str(len(tf.config.experimental.list_physical_devices('GPU'))))
    print(f"{'Num CPUs Available':<20}#: " + str(len(tf.config.experimental.list_physical_devices('CPU'))))
except Exception as e:
    pass

try:
    import geopandas as gd
    print(f"{'Geopandas version':<20}#: {gd.__version__:<20}")
except Exception as e:
    pass

try:
    import scipy as sp
    print(f"{'SciPy Version':<20}#: {sp.__version__:<20}")
except Exception as e:
    pass

try:
    import PIL
    print(f"{'PIL Version':<20}#: {Image.__version__:<20}")
except Exception as e:
     pass

try:
    import seaborn as sns
    print(f"{'Seaborn Version':<20}#: {sns.__version__:<20}")
except Exception as e:
    pass

try:
  print(f"{'GCP API Version':<20}#: {aiplatform.__version__:<20}")
except Exception as e:
  pass

try:
  print(f"{'GCP Vertex Version':<20}#: {vertexai.__version__:<20}")
except Exception as e:
  pass

try:
  print(f"{'Secret Manager Version':<20}#: {secretmanager.__version__:<20}")
except Exception as e:
  pass

print(f"Exiting {__name__} {inspect.stack()[0][3]}")
