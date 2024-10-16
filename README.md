# __House-Price-Predictor__

A [tkinter](https://docs.python.org/3/library/tkinter.html) GUI basically using an ML model that is trained by [Random Forest Regressor](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.RandomForestRegressor.html) algorithm to predict the house prices at Boston. The Boston Housing Dataset is used for the training and testing of the model that contains 506 rows and 14 columns. Based on the following 13 features:

1. CRIM - per capita crime rate by town
2. ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
3. INDUS - proportion of non-retail business acres per town.
4. CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
5. NOX - nitric oxides concentration (parts per 10 million)
6. RM - average number of rooms per dwelling
7. AGE - proportion of owner-occupied units built prior to 1940
8. DIS - weighted distances to five Boston employment centres
9. RAD - index of accessibility to radial highways
10. TAX - full-value property-tax rate per 10,000 dollars
11. PTRATIO - pupil-teacher ratio by town
12. B - $ 1000 (Bk - 0.63)^2 $ where Bk is the proportion of blacks by town
13. LSTAT - percentage of lower status of the population

the model predicts the price of such a house at Boston. Further measures such as [Stratified Shuffling](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html) with respect to CHAS, Data Preprocessing using [Imputer](https://scikit-learn.org/1.5/modules/generated/sklearn.impute.SimpleImputer.html) and [Standard Scaler](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.StandardScaler.html) inside a common [Pipeline](https://scikit-learn.org/1.5/modules/generated/sklearn.pipeline.Pipeline.html), [Cross Validation](https://scikit-learn.org/stable/modules/cross_validation.html) for Evaluation, etc. have been taken while selecting the most appropriate model.


## __Output__

### __Method-1 (Recommended): Using Executable File__
* Step-1: Download the build dolder
* Step-2: Locate the GUI.exe file
* Step-3: Double right click on it  
### __Method-2: Using [Python](https://www.python.org/) File__
* Step-1: Download these 4 files namely-Pre_processor.joblib, Model.joblib, dragon.ico and GUI.py
* Step-2: Create a new folder and place all these files inside it
* Step-3: Open powershell or command prompt inside this folder
* Step-4: Enter "pip install tk [pandas](https://pandas.pydata.org/) [numpy](https://numpy.org/) [joblib](https://pypi.org/project/joblib/)"
* Step-5: Enter "code ." to open [VS Code](https://code.visualstudio.com/) with this folder
* Step-6: Just Run the python script 
