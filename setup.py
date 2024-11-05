"""  
@Note:- 
1. cx_Freeze 7.2.4 has compatibilty issues with python 3.13.0 so I used python 3.12.5 which works well with cx_Freeze 7.2.4
2. If you face this issue too then just uninstall python 3.13.0 and install python 3.12.5

@Note:- To create .exe file from .py file, follow these steps:
        step-1: Do the necessary changes mentioned in the comments in this setup.py file only
        step-2: Open powershell or cmd in your ML project folder and run the follwoing command:
                python setup.py build
"""
import sys, os
from cx_Freeze import setup, Executable


# Write the name of main python file in place of GUI.py whose execuatble is required
script_file = "E:\\Machine Learning\\House Price Predictor\\GUI.py"                


# Include names of additional files like icon, images, data, models, pipelines
include_files = [
    "E:\\Machine Learning\\House Price Predictor\\dragon.ico",
    "E:\\Machine Learning\\House Price Predictor\\Model.joblib",
    "E:\\Machine Learning\\House Price Predictor\\Pre_processor.joblib",
    "C:\\Windows\\System32\\vcomp140.dll"       # Include vcomp140.dll for sklearn 
]


# Give a list of packages required for the application
packages = ["tkinter", "joblib", "pandas", "matplotlib", "scienceplots", "numpy", "sklearn", "ctypes"]   # Added 'ctypes' to handle DLLs


# Setup the build options
build_exe_options = {
    "include_files": include_files,                            # Including necessary files
    "packages": packages,                                      # Including required packages
    "includes": [
        "sklearn.ensemble",
        "sklearn.preprocessing",
        "sklearn.impute",
        "sklearn.model_selection",
        "sklearn.pipeline",
        "sklearn.metrics",
        "sklearn.tree",
        "pandas.plotting",
        "ctypes",     # Added ctypes for handling DLL dependencies
        "tkinter.messagebox"
    ],
    "include_msvcr": True  # This includes Microsoft Visual C++ Redistributable files
}

# Specify base (Win32GUI) to hide the console for GUI applications
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Setup configuration
setup(
    name="House Price Predictor",  # Application name
    version="0.1",  # Version number
    description="A Tkinter GUI using an ML model trained on Random Forest Regressor",  # Description
    options={"build_exe": build_exe_options},  # Build options
    executables=[Executable(script_file, base=base, icon="E:\\Machine Learning\\House Price Predictor\\dragon.ico")]  # Executable configuration
)
