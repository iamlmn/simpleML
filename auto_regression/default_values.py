algo_abbreviations  = {'Linear Regression':'lr',
'Lasso Regression':'lasso',
'Ridge Regression':'ridge',
'Elastic Net':'en',
'Least Angle Regression':'lar',
'Lasso Least Angle Regression':'llar',
'Orthogonal Matching Pursuit':'omp',
'Bayesian Ridge':'br',
'Automatic Relevance Determination':'ard',
'Passive Aggressive Regressor':'par',
'Random Sample Consensus':'ransac',
'TheilSen Regressor':'tr',
'Huber Regressor':'huber',
'Kernel Ridge':'kr',
'Support Vector Machine':'svm',
'K Neighbors Regressor':'knn',
'Decision Tree':'dt',
'Random Forest':'rf',
'Extra Trees Regressor':'et',
'AdaBoost Regressor':'ada',
'Gradient Boosting Regressor':'gbr',
'Multi Level Perceptron':'mlp',
'Extreme Gradient Boosting':'xgboost',
'Light Gradient Boosting':'lightgbm',
'CatBoost Regressor':'catboost'}

default_general_answers = {}

default_setup_answers = {'sampling': False, 
		      'sample_estimator': None,
			  'categorical_features': None, 
			  'categorical_imputation': 'constant', 
			  'ordinal_features': None,
			  'high_cardinality_features': None, 
			  'high_cardinality_method': 'frequency', 
			  'numeric_features': None,
			  'numeric_imputation': 'mean', 
			  'date_features': None, 
			  'ignore_features': None, 
			  'normalize': False, 
			  'normalize_method': 'zscore', 
			  'transformation': False, 
			  'transformation_method': 'yeo-johnson', 
			  'handle_unknown_categorical': False, 
			  'unknown_categorical_method': 'least_frequent', 
			  'pca': False, 'pca_method': 'linear', 
			  'ignore_low_variance': False, 
			  'combine_rare_levels': False, 
			  'rare_level_threshold': False, 
			  'bin_numeric_features': False, 
			  'remove_outliers': False, 
			  'outliers_threshold': '0.05', 
			  'remove_multicollinearity': False, 
			  'multicollinearity_threshold': '0.9', 
			  'create_clusters': False, 
			  'cluster_iter': '20', 
			  'polynomial_features': False, 
			  'polynomial_degree': '2', 
			  'trigonometry_features': False, 
			  'polynomial_threshold': '0.1', 
			  'group_features': None, 
			  'group_names': None, 
			  'feature_selection': False, 
			  'feature_selection_threshold': '0.8', 
			  'feature_interaction': False, 
			  'feature_ratio': False, 
			  'interaction_threshold': '0.01', 
			  'transform_target': False, 
			  'transform_target_method': 'box-tox', 
			  'session_id': None, 
			  'silent': True}


default_modelling_answers = {}