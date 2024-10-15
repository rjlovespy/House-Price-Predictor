"""   
To convert .py file into .exe file using cx_Freeze, perform the following steps:-
    Step-1: Create an empty setup.py file
    Step-2: Write the below python script in setup.py file with the necessary changes mentioned via comments
    Step-3: Go to the folder where your entire project is present
    Step-4: Press Shift and right click to open powershell
    Step-5: Enter this command "python setup.py build"
"""
import sys, os
from cx_Freeze import setup, Executable


""" Relative Path Generation so that on changing the folder location no problem occurs """
app_dir = os.path.dirname(os.path.abspath(__file__))


# Write the name of main python file in place of GUI.py whose execuatble is required
script_file = os.path.join(app_dir, "GUI.py")                


# Include names of additional files like icon, images, data, models, pipelines
include_files = [
    os.path.join(app_dir, "dragon.ico"),
    os.path.join(app_dir, "Model.joblib"),
    os.path.join(app_dir, "Pre_processor.joblib"),
    os.path.join("C:\\Windows\\System32", "vcomp140.dll")       # Include vcomp140.dll for sklearn 
]


# Give a list of packages required for the application
packages = ["tkinter", "joblib", "pandas", "numpy", "sklearn", "ctypes"]   # Added 'ctypes' to handle DLLs


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
        "ctypes",     # Add ctypes for handling DLL dependencies
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
    name="Price_Predictor",  # Application name
    version="0.1",  # Version number
    description="A Tkinter GUI using an ML model trained on Random Forest Regressor",  # Description
    options={"build_exe": build_exe_options},  # Build options
    executables=[Executable(script_file, base=base, icon=os.path.join(app_dir, "dragon.ico"))]  # Executable configuration
)
