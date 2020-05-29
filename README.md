# simpleML 
:soon:

Simple ML is command-line machcine learning utility written in Python3.7 wrapped over existing ML libraries.

![](assets/cli_usage.png?raw=true)

Aim is to attain no-code ML training while still having the ability to use multiple(all) technique/model/parameters with just few clicks and output neat HTML reports(transperancy on data and models/analysis) with plots and data analysis report which can be helpful in reducing the hypothesis to insights cycle time in a ML experiment

Altough a lot of cloud providers provide this option and sometimes it may not be worth using it, and even costlier.  While It's simpler over CLI.

Currently we can run linear regression & Binary classification from command line. It provides interactive terminal to configure your machine learning pipelines and preprocessing steps.

The analysis part run on a jupyter notebook which can be changed as required easily and we can still use the existing framework to provide the reports and CLI configurations. 



## Linear Regression <!-- :octocat: -->
Regression Module is a supervised machine learning module that is used for estimating the relationships between a dependent variable (often called the ‘outcome variable’, or ‘target’) and one or more independent variables (often called ‘features’, ‘predictors’, or ‘covariates’). The objective of regression is to predict continuous values such as predicting sales amount, predicting quantity, predicting temperature etc. This supports several pre-processing features that prepare the data for modeling through CLI just by clicking. It has over 25 ready-to-use algorithms and several plots to analyze the performance of trained models.
> Option to run on default configuration (docs :soon:).  

> Provides preprocessing configuration for EDA & making data ready.

> Supports comparing 25 Linear regression results based on below 
 - R2
 - MAE
 - MAPE
 - RMSE 

  merics and provides the best model, but still users have an option to override and run their model of interest.

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


## Binary classification <!-- :octocat: -->
Classification Module is a supervised machine learning module which is used for classifying elements into groups. The goal is to predict the categorical class labels which are discrete and unordered. Some common use cases include predicting customer default (Yes or No), predicting customer churn (customer will leave or stay), disease found (positive or negative). This module can be used for binary and provides several pre-processing features that prepare the data for modeling through CLI. It has over 18 ready-to-use algorithms and several plots to analyze the performance of trained models.

> Option to run on customized preprocessing configurations (docs :soon:).  

> Provides preprocessing configuration for EDA & making data ready.

> Runs 18 classification and comapres the 
- 'Accuracy'
- 'AUC'
- 'Recall'
- 'Precision'
- 'F1'
- 'Kappa' 
	merics and provides the best model, but still users have an option to override and run their model of interest.

> Option for auto tune hyperparameters based on random grid search.

> Creates a details HTML report with below plots
- Area Under the Curve
- Discrimination Threshold
- Precision Recall Curve
- Confusion Matrix
- Class Prediction Error
- Classification Report
- Decision Boundary
- Recursive Feature Selection
- Learning Curve
- Manifold Learning
- Calibration Curve
- Validation Curve
- Dimension Learning
- Feature Importance
- Model Hyperparameter

> SHAP plots for SHapley Additive exPlanations

> Pickling model for re-use.



<h2>Sample demos as of (30thMay2020) - <a href="https://iamlmn.github.io/simpleML/">View here</a>></h2>
<h5> Creating Linear regression with default configuration on boston dataset</h5> 
<!-- ![](assets/regression/default_regression.gif) -->
<video width="320" height="240" controls>
  <source src="assets/lr-all.mp4" type="video/mp4">
</video>

<h5>Creating Linear regression model with customized preprocessing configurations</h5>
<!-- ![](assets/regression/preprocessing.gif) -->

<video width="320" height="240" controls>
  <source src="assets/video.mov" type="video/mp4">
</video>

<h5>Creating Binary Classification model with default preprocessing configurations on credit card dataset </h5>
<!-- ![](assets/regression/preprocessing.gif) -->

<video width="320" height="240" controls>
  <source src="assets/Classification.mov" type="video/mp4">
</video>

<h5>Creating Binary Classification with default preprocessing configurations on credit card dataset </h5>
<!-- ![](assets/regression/preprocessing.gif) -->

<video width="320" height="240" controls>
  <source src="assets/classificaiton_report.mov" type="video/mp4">
</video>


<!-- ![View sample HTML report on Boston data](assets/regression/regression.html) -->



### Install & run 
```
git clone https://github.com/iamlmn/simpleML.git
cd simpleML
pip install -r requirements.txt
python3 auto_regression/main.py
```

TODOs and completed work : 
- [x] Binary Classification
- [x] Regression
- [x] Interactive CLI configuration
- [x] HTML Reporting
- [ ] Clustering
- [ ] Blending model
- [ ] Stacking model
- [x] Ensemble Classification model (Baggin and Boosting)
- [ ] Ensemble Regression model (Baggin and Boosting)
- [ ] Multiple(best) model creations
- [ ] HTML report remediation
- [ ] Dockerization
- [ ] Convert it to an executable
- [ ] Documentation
- [ ] Support different file types
- [ ] Unit tests
- [ ] Multiclass Classification


#### :octocat: Contributions and ideas are welcome.

