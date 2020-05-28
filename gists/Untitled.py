#!/usr/bin/env python
# coding: utf-8

# In[4]:


# ARGS & PARAMS
# if _user_selected_model is None:
#     Execution_Id = "output/{}/Job_{}_best_{}".format(dataset_name, _id,datetime.datetime.now())
# Pycaret Args
from IPython.display import HTML
from pyfiglet import Figlet
f = Figlet(font='slant')
print (f.renderText('SimpleML'))

# Read config

import yaml
# Setup Environment constants
setup = dict(train_size = 0.7, sampling = True, sample_estimator = None, categorical_features = None, categorical_imputation = 'constant', 
	ordinal_features = None, high_cardinality_features = None, high_cardinality_method = 'frequency', numeric_features = None, 
	numeric_imputation = 'mean', date_features = None, ignore_features = None, normalize = False, 
	normalize_method = 'zscore', transformation = False, transformation_method = 'yeo-johnson', handle_unknown_categorical = True, 
	unknown_categorical_method = 'least_frequent', pca = False, pca_method = 'linear', pca_components = None, 
	ignore_low_variance = False, combine_rare_levels = False, rare_level_threshold = 0.10, 
	bin_numeric_features = None, remove_outliers = False, outliers_threshold = 0.05, remove_multicollinearity = False, 
	multicollinearity_threshold = 0.9, create_clusters = False, cluster_iter = 20, polynomial_features = False, polynomial_degree = 2, 
	trigonometry_features = False, polynomial_threshold = 0.1, group_features = None, group_names = None, feature_selection = False, 
	feature_selection_threshold = 0.8, feature_interaction = False, feature_ratio = False, interaction_threshold = 0.01, transform_target = False, 
	session_id = None, silent=False, profile = False )

with open('new_config.yml', 'w') as outfile:
    yaml.dump(setup, outfile, default_flow_style=False)

# Read YAML file
with open("new_config.yml", 'r') as stream:
    config = yaml.safe_load(stream)

assert setup == config


# CCaret config
_input_file = None
_demo_dataset = 'boston'
_pandas_profiling = True # Default is True which gives detailed 
_target = 'medv' # default Target cclass for Boston data
_silent_preproccessing = True

_target_class = 'medv'
_normalize = True
_transformation = True
_transform_target = True
_combine_rare_levels = True
_rare_level_threshold = 0.05
_remove_multicollinearity = True
_multicollinearity_threshold = 0.95
_bin_numeric_features = []
_silent_preproccessing = True

# Temp args
_autoselect = True
_kfold = 10
_round = 4
_sort_best_model_by = 'R2' #['R2']
_turbo = True
_blacklist = None
_user_selected_model = None

# Now create model
number_of_models = 1
_auto_tune = True 


# In[ ]:





# In[ ]:


## My ARGS

# Pycaret Args
_input_file = None
_demo_dataset = 'boston'
_pandas_profiling = True # Default is True which gives detailed 
_target = 'medv' # default Target cclass for Boston data
_silent_preproccessing = True
import logging
#import the dataset from pycaret repository
import pandas as pd
if _input_file == None and _demo_dataset == None:
    from pycaret.datasets import get_data
    input_data = get_data('boston', profile = True)
    data = input_data.sample(frac=0.9, random_state=786).reset_index(drop=True)
    data_unseen = input_data.drop(data.index).reset_index(drop=True)

    print('Data for Modeling: ' + str(data.shape))
    print('Unseen Data For Predictions: ' + str(data_unseen.shape))
elif _demo_dataset in ['diabetes', 'boston']:
    from pycaret.datasets import get_data
    input_data = get_data(_demo_dataset, profile = True)
    data = input_data.sample(frac=0.9, random_state=786).reset_index(drop=True)
    data_unseen = input_data.drop(data.index).reset_index(drop=True)

    print('Data for Modeling: ' + str(data.shape))
    print('Unseen Data For Predictions: ' + str(data_unseen.shape))
else:
    input_data = pd.read_csv(_input_file)
    # print('No proper input was given, So running regression on Boston dataset')
    logging.info('Succesfully read the input csv')
    data = input_data.sample(frac=0.9, random_state=786).reset_index(drop=True)
    data_unseen = input_data.drop(data.index).reset_index(drop=True)

    print('Data for Modeling: ' + str(data.shape))
    print('Unseen Data For Predictions: ' + str(data_unseen.shape))


# In[ ]:


print("Data shape : {}".format(input_data.shape))


# 
# ### Setup
# 
# pre-processing steps (other than those that are imperative for machine learning experiments which were performed 
# automatically by PyCaret). In this example we will take it to the next level by customizing the pre-processing pipeline using setup(). Let's look at how to implement all the steps discussed in section 4 above.

# In[ ]:


_target_class = 'medv'
_normalize = True
_transformation = True
_transform_target = True
_combine_rare_levels = True
_rare_level_threshold = 0.05
_remove_multicollinearity = True
_multicollinearity_threshold = 0.95
_bin_numeric_features = []
_silent_preproccessing = True
from pycaret.regression import *

exp_reg102 = setup(data = input_data, target = 'medv', session_id=123,
                  normalize = True, transformation = True, transform_target = True, 
                  combine_rare_levels = True, rare_level_threshold = 0.05,
                  remove_multicollinearity = True, multicollinearity_threshold = 0.95, 
                  bin_numeric_features = [], silent = _silent_preproccessing) 


# ## Comparing all Models
# Comparing all models to evaluate performance is the recommended starting point for modeling once the setup is completed (unless you exactly know what kind of model you need, which is often not the case). This function trains all models in the model library and scores them using k-fold cross validation for metric evaluation. The output prints a score grid that shows average MAE, MSE, RMSE, R2, RMSLE and MAPE accross the folds (10 by default) of all the available models in the model library.

# In[ ]:


# Temp args
_autoselect = True
_kfold = 10
_round = 4
_sort_best_model_by = 'R2' #['R2']
_turbo = True
_blacklist = None
_user_selected_model = None

models_comparison = compare_models(blacklist = _blacklist, fold = _kfold,  round = _round,  sort = _sort_best_model_by, turbo = _turbo)
models_comparison.to_excel('tmp_models.xlsx')
models_comparison_df = pd.read_excel('tmp_models.xlsx',index = False)
display(models_comparison)
best_model = models_comparison_df['Model'][0]
top_five_best_models = models_comparison_df['Model'][0:5]
top_three_best_models = models_comparison_df['Model'][0:3]
print("Best suggested model based on best value for {} is {}".format(best_model, _sort_best_model_by))
if _user_selected_model is not None:
    print('Model of interest is selected {}'.format(_user_selected_model))

if _autoselect == True or _user_selected_model is None:
    model_selected = best_model
    print("Selected {} based on {}".format(best_model, _sort_best_model_by))
else:
    model_selected = _user_selected_model
    print("Selected {} based on user choice".format(model_selected))

#print("model stats for {}: DF")


# Two simple words of code (not even a line) have created over 22 models using 10 fold cross validation and evaluated the 6 most commonly used regression metrics (MAE, MSE, RMSE, R2, RMSLE and MAPE). The score grid printed above highlights the highest performing metric for comparison purposes only. The grid by default is sorted using R2 (highest to lowest) which can be changed by passing sort parameter. For example compare_models(sort = 'RMSLE') will sort the grid by RMSLE (lower to higher since lower is better). If you want to change the fold parameter from the default value of 10 to a different value then you can use the fold parameter. For example compare_models(fold = 5) will compare all models on 5 fold cross validation. Reducing the number of folds will improve the training time.

# ## Create a Model
# While compare_models() is a powerful function and often a starting point in any experiment, it does not return any trained models. PyCaret's recommended experiment workflow is to use compare_models() right after setup to evaluate top performing models and finalize a few candidates for continued experimentation. As such, the function that actually allows to you create a model is unimaginatively called create_model(). This function creates a model and scores it using stratified cross validation. Similar to compare_models(), the output prints a score grid that shows MAE, MSE, RMSE, R2, RMSLE and MAPE by fold.
# 
# For the remaining part of this tutorial, we will work with the below models as our candidate models. The selections are for illustration purposes only and do not necessarily mean they are the top performing or ideal for this type of data.
# 
#  - AdaBoost Regressor ('ada')
#  - Light Gradient Boosting Machine ('lightgbm')
#  - Decision Tree ('dt')
# There are 25 regressors available in the model library of PyCaret. Please view the create_model() docstring for the list of all available models.

# In[ ]:


# Now create model
number_of_models = 1
_auto_tune = True 

def model_to_abv(model):
    return model
def train_and_plot_model(model, _auto_tune, plots = True):
    print("Training {}".format(model))
    if _auto_tune:
        print('Training with default hyper parameters')
        trained_model = tune_model(model_to_abv(model))
        print("Completed trained with default hyperparameters tuned {}".format(trained_model))
    else:
        print("Hyperparameter tuning... {}".format(_auto_tune))
        trained_model = create_model(model_to_abv(model))
        print("Completed training with hyperparameters tuned {}".format(trained_model))
    return trained_model 
trained_model = train_and_plot_model('gbr',True)


# 
# When a model is created using the create_model() function it uses the default hyperparameters. 
# In order to tune hyperparameters, the tune_model() function is used. This function 
# automatically tunes the hyperparameters of a model on a pre-defined search space and scores 
# it using k-fold cross validation. The output prints a score grid that shows 
# MAE, MSE, RMSE, R2, RMSLE and MAPE by fold.
# 
# Note: tune_model() does not take a trained model object as an input. 
# It instead requires a model name to be passed as an abbreviated string similar to 
# how it is passed in create_model(). All other functions inpycaret.regression 
# require a trained model object as an argument.

# In[ ]:


#evaluate_model(trained_model)


# In[ ]:


plots = True
if plots == True:
    print('Hyper parameters')
    display(plot_model(trained_model, plot = 'parameter'))


# In[ ]:



# Residual Plot
print('Residual plots')
print(plot_model(trained_model))
  
  


# In[ ]:


print("Feature importance plot")
plot_model(trained_model, plot = 'feature')
        


# In[ ]:


# Prediction Error Plot
print("Prediction Error plot")
plot_model(trained_model, plot = 'error')
        


# In[ ]:


# Learning
print("Learning Curve plot")
display(plot_model(trained_model, plot = 'learning'))
    


# In[ ]:


# Recursive Feature Selection
print("Recursive Feature Selection")
plot_model(trained_model, plot = 'rfe')


# In[ ]:


# Cooks Distance Plot
print("Cooks Distance Plot")
plot_model(trained_model, plot = 'cooks')
        


# In[ ]:


# Validation Curve Plot
print("Validation Curve Plot")
display(plot_model(trained_model, plot = 'vc'))


# In[ ]:


# manifold 
print("manifold")
display(plot_model(trained_model, plot = 'manifold'))


# # Predict on Test / Hold-out Sample
# Before finalizing the model, it is advisable to perform one final check by predicting the test/hold-out set and reviewing the evaluation metrics. If you look at the information grid in Section 6 above, you will see that 30% (1621 samples) of the data has been separated out as a test/hold-out sample. All of the evaluation metrics we have seen above are cross-validated results based on training set (70%) only. Now, using our final trained model stored in the tuned_lightgbm variable we will predict the hold-out sample and evaluate the metrics to see if they are materially different than the CV results

# # Finalize Model for Deployment
# Model finalization is the last step in the experiment. A normal machine learning workflow in PyCaret starts with setup(), followed by comparing all models using compare_models() and shortlisting a few candidate models (based on the metric of interest) to perform several modeling techniques such as hyperparameter tuning, ensembling, stacking etc. This workflow will eventually lead you to the best model for use in making predictions on new and unseen data. The finalize_model() function fits the model onto the complete dataset including the test/hold-out sample (30% in this case). The purpose of this function is to train the model on the complete dataset before it is deployed in production.

# In[ ]:


final_model = finalize_model(trained_model)


# In[ ]:


predict_model(trained_model)


# The R2 on the test/hold-out set is 0.9728 compared to 0.9753 achieved on tuned_lightgbm CV results (in section 9.2 above). This is not a significant difference. If there is a large variation between the test/hold-out and CV results, then this would normally indicate over-fitting but could also be due to several other factors and would require further investigation. In this case, we will move forward with finalizing the model and predicting on unseen data (the 10% that we had separated in the beginning and never exposed to PyCaret).
# 
# (TIP : It's always good to look at the standard deviation of CV results when using create_model().)

# # Predict on Unseen Data
# The predict_model() function is also used to predict on the unseen dataset. The only difference from section 11 above is that this time we will pass the data_unseen parameter. data_unseen is the variable created at the beginning of the tutorial and contains 10% (600 samples) of the original dataset which was never exposed to PyCaret. (see section 5 for explanation)
# 

# In[ ]:


unseen_predictions = predict_model(final_model, data=data_unseen)
unseen_predictions.head()
unseen_predictions_file = 'output/unseen_prediction.csv'
unseen_predictions.to_csv(unseen_predictions_file)
print('Exported {}'.format(unseen_predictions_file))


# # Save the model / Pickle

# In[ ]:


print('Pickling model..')
save_model(final_model,'output/FinalModel 27May2020')


# In[ ]:





# In[ ]:




