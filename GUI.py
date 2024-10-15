import tkinter.messagebox as tmsg
from tkinter import *
from joblib import load
import pandas as pd
import numpy as np
import os

# Resets the features to 0
def resetFeatures():
    for i in range(13):
        tv[i].set(0)
        features[i].update()
    output["text"] = "Enter new house features"
    

# Uses a Machine Learning(ML) model trained by RandomForestRegressor Algorithm 
def predictPrice():
    try:
        if (tv[0].get() >= 0) and (tv[1].get() >= 0)  and (tv[2].get() >= 0) and ((tv[3].get() == 0) or (tv[3].get() == 1)) and ((tv[4].get() >= 0) and (tv[4].get() <= 1)) and (tv[5].get() >= 0) and (tv[6].get() >= 0) and (tv[7].get() >= 0) and (tv[8].get() >= 0) and (tv[9].get() >= 0) and (tv[10].get() >= 0) and (tv[11].get() >= 0) and ((tv[12].get() >= 0) and (tv[12].get() <= 100)): 
            Model = load(os.path.join(app_dir, "Model.joblib"))
            Pre_processor = load(os.path.join(app_dir, "Pre_processor.joblib"))
            
            features = [tv[0].get(), tv[1].get(), tv[2].get(), tv[3].get(), tv[4].get(), tv[5].get(), tv[6].get(), tv[7].get(), tv[8].get(), tv[9].get(), tv[10].get(), tv[11].get(), tv[12].get()]
            features_na = np.array([features])                                   
            features_df = pd.DataFrame(features_na)                              # Unpreprocessed Features
            features_df.rename(columns={0:"CRIM", 1:"ZN", 2:"INDUS", 3:"CHAS", 4:"NOX", 5:"RM", 6:"AGE", 7:"DIS", 8:"RAD", 9:"TAX", 10:"PTRATIO", 11:"B", 12:"LSTAT"}, inplace=True)
            features_pp = Pre_processor.transform(features_df)                   # Preprocessed Features
            price_prediction = Model.predict(features_pp)

            output["text"] = f"The price of such a house at Boston is $ {1000*price_prediction[0]}"
        else:
            tmsg.showinfo(title="Warning!", message="Invalid input has been entered")
            output["text"] = "Enter valid new house features"
    except TclError:
        output["text"] = "Do not enter integers with preceding zeros"
              

# Screen Customization
root = Tk()
root.geometry("1000x800")
root.resizable(False, True)
root.config(bg="lavender")
root.title("Dragon Real Estate")  
app_dir = os.path.dirname(os.path.abspath(__file__))          
root.iconbitmap(os.path.join(app_dir, "dragon.ico"))


# Giving Title
f1 = Frame(root, bg="lavender", highlightbackground="thistle", highlightthickness=2)
f1.pack(fill=X, padx=50, pady=50)
Label(f1, text="Boston House's Price Predictor", bg="lavender", font="Lucida 30 bold").pack(padx=10, pady=10)


# Creating Entries for taking House Features
f2 = Frame(root, bg="lavender", highlightbackground="thistle", highlightthickness=2)
f2.pack(fill=X, ipadx=10, ipady=10, padx=50)
Label(f2, text="1. Enter CRIM - per capita crime rate by town"                                       , bg="lavender", font="Lucida 12 normal").grid(row=0, column=0, sticky=W, padx=5, pady=5)
Label(f2, text="2. Enter ZN - proportion of residential land zoned for lots over 25,000 sq ft"       , bg="lavender", font="Lucida 12 normal").grid(row=1, column=0, sticky=W, padx=5)
Label(f2, text="3. Enter INDUS - proportion of non-retail business acres per town"                   , bg="lavender", font="Lucida 12 normal").grid(row=2, column=0, sticky=W, padx=5, pady=5)
Label(f2, text="4. Enter CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)" , bg="lavender", font="Lucida 12 normal").grid(row=3, column=0, sticky=W, padx=5)
Label(f2, text="5. Enter NOX - nitric oxides concentration (parts per 10 million)"                   , bg="lavender", font="Lucida 12 normal").grid(row=4, column=0, sticky=W, padx=5, pady=5)
Label(f2, text="6. Enter RM - average number of rooms per dwelling"                                  , bg="lavender", font="Lucida 12 normal").grid(row=5, column=0, sticky=W, padx=5)
Label(f2, text="7. Enter AGE - proportion of owner-occupied units built prior to 1940"               , bg="lavender", font="Lucida 12 normal").grid(row=6, column=0, sticky=W, padx=5, pady=5)
Label(f2, text="8. Enter DIS - weighted distances to five Boston employment centres"                 , bg="lavender", font="Lucida 12 normal").grid(row=7, column=0, sticky=W, padx=5)
Label(f2, text="9. Enter RAD - index of accessibility to radial highways"                            , bg="lavender", font="Lucida 12 normal").grid(row=8, column=0, sticky=W, padx=5, pady=5)
Label(f2, text="10. Enter TAX - full-value property-tax rate per 10,000 dollars"                     , bg="lavender", font="Lucida 12 normal").grid(row=9, column=0, sticky=W, padx=5)
Label(f2, text="11. Enter PTRATIO - pupil-teacher ratio by town"                                     , bg="lavender", font="Lucida 12 normal").grid(row=10, column=0, sticky=W, padx=5, pady=5)
Label(f2, text="12. Enter B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town"        , bg="lavender", font="Lucida 12 normal").grid(row=11, column=0, sticky=W, padx=5)
Label(f2, text="13. Enter LSTAT - percentage of lower status of the population"                      , bg="lavender", font="Lucida 12 normal").grid(row=12, column=0, sticky=W, padx=5, pady=5)

tv = [None]*13
features = [None]*13
initial_features = np.array([0.05819, 85.0, 4.64, 0, 0.992, 6.108, 10.0, 15.2203, 1, 500, 19.4, 399.89, 5])
for i in range(13):
    tv[i] = DoubleVar()
    tv[i].set(initial_features[i])
    features[i] = Entry(f2, textvariable = tv[i], font="Lucida 14 normal", bg="thistle", relief=SUNKEN)
    if i%2 == 0:
        features[i].grid(row=i, column=1, sticky=W, ipady=2,  padx=50, pady=5)
    else:
        features[i].grid(row=i, column=1, sticky=W, ipady=2,  padx=50)

Button(f2, text="RESET", command=resetFeatures, font="Lucida 14 bold", activebackground="gold", bg="deepskyblue", width=10, bd=2, relief=SUNKEN).grid(row=15, column=0, sticky=W, padx=50, pady=5, ipady=3)
Button(f2, text="PREDICT", command=predictPrice, font="Lucida 14 bold", activebackground="gold", bg="lime", width=10, bd=2, relief=SUNKEN).grid(row=15, column=0, ipady=3)


# Labelling the Prediction
f3 = Frame(root, bg="lavender", highlightbackground="thistle", highlightthickness=2)
f3.pack(fill=X, padx=50, pady=20)
output = Label(f3, text="Press RESET for entering new house features", fg="crimson", bg="lavender", font="Lucida 15 bold")
output.pack(padx=10, pady=10)


root.mainloop()