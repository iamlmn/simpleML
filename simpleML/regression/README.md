# simpleML - Linear Regression
:soon:
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

> Creates a details HTML report with :
- residual plots
- Feature importance plot
- Prediction Error plot 
- Learning Curve plot 
- Cooks Distance Plot 
- Validation Curve Plot

> SHAP plots for SHapley Additive exPlanations

> Pickling model for re-use.



<h2>Sample demos as of (30thMay2020)</h2>
<h5> Configuring Linear regression with default configuration on boston dataset</h5> 
<!-- ![](assets/regression/default_regression.gif) -->
<video width="320" height="240" controls>
  <source src="assets/lr-all.mp4" type="video/mp4">
</video>

<h5>Configuring Linear regression with customized preprocessing</h5>
<!-- ![](assets/regression/preprocessing.gif) -->

<video width="320" height="240" controls>
  <source src="assets/video.mov" type="video/mp4">
</video>


TODO : ADD TODOS