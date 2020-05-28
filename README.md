# simpleML

Simple ML is python based machcine learning library wrapped over PyCaret.

Aim is to attain no code ML training while still having a transperancy on what technique/model/paramets has been used with just few clicks with neat HTML reports with plots and reduce the hypothesis to insights cycle time in a ML experiment
Altough a lot of cloud providers provide this option and sometimes it may not be worth using it, and even costlier.

## Linear Regression 
Currently we can run linear regression from command line.. It provides interactive terminal to configure your machine learning pipelines.
We have an option to run on default configuration (need docs but can refer to PyCaret docs for now).  Provides preprocessing configuration for EDA & making data ready.
Runs 25 Linear regression and comapres the R2,MAE,MAPE,RMSE merics and provides the best model, but still users have an option to override and run their model of interest.
Option for auto hyperparameter tuning based on random grid search.
Creates a details HTML report with residual plots, Feature importance plot, Prediction Error plot, Learning Curve plot, Cooks Distance Plot, Validation Curve Plot
SHAP plots for SHapley Additive exPlanations
Pickling model for re-use.


Sample runs as of (28thMay2020)
### Default configuration on Linear regression.
![](assets/regression/default_regression.gif)

### Detailed configuration on Linear regression for customized preprocessing.
![](assets/regression/preprocessing.gif)

<!-- ![View sample HTML report on Boston data](assets/regression/regression.html) -->

### Install & run
```
git clone https://github.com/iamlmn/simpleML.git
cd simpleML
python3 auto_regression/main.py
```

TODOs and Planned work : 
- [ ] Classification
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