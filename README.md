# simpleML

Simple ML is python based machcine learning tool wrapped over PyCaret.

Aim is to attain no code ML training while still having the ability to use multiple technique/model/paramets has been used with just few clicks with neat HTML reports(transperancy and) with plots and reduce the hypothesis to insights cycle time in a ML experiment
Altough a lot of cloud providers provide this option and sometimes it may not be worth using it, and even costlier. 
Currently we can run linear regression from command line.. It provides interactive terminal to configure your machine learning pipelines.
The algirhtm part is still on a jupyter notebook which can be changes as requirred easily and we can use the existing framework still. 


## Linear Regression 
Regression Module is a supervised machine learning module that is used for estimating the relationships between a dependent variable (often called the ‘outcome variable’, or ‘target’) and one or more independent variables (often called ‘features’, ‘predictors’, or ‘covariates’). The objective of regression is to predict continuous values such as predicting sales amount, predicting quantity, predicting temperature etc. This module provides several pre-processing features that prepare the data for modeling through setup function. It has over 25 ready-to-use algorithms and several plots to analyze the performance of trained models.
> Option to run on default configuration (need docs but can refer to PyCaret docs for now).  

> Provides preprocessing configuration for EDA & making data ready.

> Runs 25 Linear regression and comapres the R2,MAE,MAPE,RMSE merics and provides the best model, but still users have an option to override and run their model of interest.

> Option for auto hyperparameter tuning based on random grid search.

> Creates a details HTML report with residual plots, Feature importance plot, Prediction Error plot, Learning Curve plot, Cooks Distance Plot, Validation Curve Plot

> SHAP plots for SHapley Additive exPlanations

> Pickling model for re-use.


## Classification
Classification Module is a supervised machine learning module which is used for classifying elements into groups. The goal is to predict the categorical class labels which are discrete and unordered. Some common use cases include predicting customer default (Yes or No), predicting customer churn (customer will leave or stay), disease found (positive or negative). This module can be used for binary and provides several pre-processing features that prepare the data for modeling through setup function. It has over 18 ready-to-use algorithms and several plots to analyze the performance of trained models.

> Option to run on default preprocessing configuration (need docs but can refer to PyCaret docs for now).  

> Provides preprocessing configuration for EDA & making data ready.

> Runs 18 classification and comapres the 'Accuracy', 'AUC', 'Recall', 'Precision', 'F1', 'Kappa' merics and provides the best model, but still users have an option to override and run their model of interest.

> Option for auto tune hyperparameters based on random grid search.

> Creates a details HTML report with 
	- Area Under the Curve, 
	- Discrimination Threshold, 
	-	Precision Recall Curve, 
	-	Confusion Matrix, 
	-	Class Prediction Error
	-	Classification Report
	-	Decision Boundary
	-	Recursive Feature Selection
	-	Learning Curve
	-	Manifold Learning
	-	Calibration Curve
	-	Validation Curve
	-	Dimension Learning
	-	Feature Importance
	-	Model Hyperparameter

> SHAP plots for SHapley Additive exPlanations

> Pickling model for re-use.



Sample runs as of (28thMay2020)
<h3>Running Linear regression with Default configuration on boston dataset</h3>
<!-- ![](assets/regression/default_regression.gif) -->
<video width="320" height="240" controls>
  <source src="assets/lr-all.mp4" type="video/mp4">
</video>

<h3>Running Linear regression customized preprocessing configurations</h3>
<!-- ![](assets/regression/preprocessing.gif) -->

<video width="320" height="240" controls>
  <source src="assets/video.mov" type="video/mp4">
</video>



<!-- ![View sample HTML report on Boston data](assets/regression/regression.html) -->





### Install & run
```
git clone https://github.com/iamlmn/simpleML.git
cd simpleML
pip install requirements.txt
python3 auto_regression/main.py
```

TODOs and Planned work : 
- [x] Classification
- [x] Regression
- [ ] Clustering
- [ ] Blending model
- [ ] Stacking model
- [ ] Multiple(best) model creations
- [ ] HTML report remediation
- [ ] Dockerization
- [ ] Convert it to an executable
- [ ] Documentation


Contributions and ideas are welcome.