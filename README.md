# DoubleLift-python
Double Lift Charts in Python

Installation:

To install using pip: `pip install DoubleLift`

double_lift takes in the following 3 pandas series with the same index: 
1) Actual Results
2) Model 1 Predictions
3) Model 2 Predictions 

And creates a double lift chart similar to the description in CAS Monograph on GLM's. 

The model_type argument can be set to "additive" (think Loss Cost) or "ratio" (think Loss Ratio). 


