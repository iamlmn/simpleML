from icli_validators import *

general_questions = [
    {
        'type': 'input',
        'name': 'user_name',
        'message': 'Provide your nickname : ',
        'default': 'lmn'
    },
    {
        'type': 'input',
        'name': 'analysis_name',
        'message': 'Provide a unique name for your execution : ',
        'default': 'my-regression'
    },

    {
        'type': 'confirm',
        'name': 'demo_run',
        'message': 'Run a demo data?',
        'default': True
    },

    {
        'type': 'list',
        'name': 'demo_dataset',
        'message': 'Select any of the demo dataset',
        'when': lambda setup_answers: setup_answers['demo_run'] == True,
        'choices': ['boston', 'parkinsons', 'traffic', 'house', 'gold', 'forest', 'bike']
    },

    {
        'type': 'input',
        'name': 'input_file',
        'message': 'Path to input CSV',
        'when': lambda setup_answers: setup_answers['demo_run'] == False,
        'validate': InputFilePathValidator
    },

    {
        'type': 'list',
        'name': 'target_variable',
        'message': 'target variable',
        'when': lambda setup_answers: setup_answers['demo_run'] == False,
        'choices': lambda setup_answers: get_column_names(setup_answers),

    }]

setup_questions = [
    {

        'type': 'confirm',
        'name': 'custom_setup',
        'message': 'customize setup/preprocessing?',
        'default': False,
    },
    {
        'type': 'confirm',
        'name': 'sampling',
        'message': 'Sampling?',
        'default': False,
        'when': lambda setup_answers: setup_answers['custom_setup'] == True
    },

    {
        'type': 'input',
        'name': 'sample_estimator',
        'message': 'sample_estimator : If None, Linear Regression is used by default.',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },


    {
        'type': 'input',
        'name': 'categorical_features',
        'message': 'categorical_features = [‘column1’] : string, default = None',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },

    {
        'type': 'list',
        'name': 'categorical_imputation',
        'message': 'categorical_imputation : string, default = ‘constant’',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'choices': ['constant', 'mode']
    },

    {
        'type': 'input',
        'name': 'ordinal_features',
        'message': 'ordinal_features = { ‘column_name’ : [‘low’, ‘medium’, ‘high’] } (dictionary)',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },

    {
        'type': 'input',
        'name': 'high_cardinality_features',
        'message': 'high_cardinality_features: string, default = None',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },

    {
        'type': 'list',
        'name': 'high_cardinality_method',
        'message': 'high_cardinality_method string, default = frequency',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'choices': ['frequency', 'clustering']
    },

    {
        'type': 'input',
        'name': 'numeric_features',
        'message': 'numeric_features = [‘column1’] (string)',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },

    {
        'type': 'list',
        'name': 'numeric_imputation',
        'message': 'numeric_imputation',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'choices': ['mean', 'median']
    },

    {
        'type': 'input',
        'name': 'date_features',
        'message': 'date_features : date_column_name (string) .',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },

    {
        'type': 'input',
        'name': 'ignore_features',
        'message': 'ignore_features',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },

    {
        'type': 'confirm',
        'name': 'normalize',
        'message': 'normalize : bool.',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },

    {
        'type': 'list',
        'name': 'normalize_method',
        'message': 'normalize_method : .',
        'choices': ['zscore', 'minmax', 'maxabs', 'robust'],
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'zscore'
    },

    {
        'type': 'confirm',
        'name': 'transformation',
        'message': 'transformation : bool.',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },

    {
        'type': 'input',
        'name': 'transformation_method',
        'message': 'transformation_method: string',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'yeo-johnson'
    },

    {
        'type': 'confirm',
        'name': 'handle_unknown_categorical',
        'message': 'handle_unknown_categorical: bool.',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },

    {
        'type': 'input',
        'name': 'unknown_categorical_method',
        'message': 'unknown_categorical_method: string.',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'least_frequent'
    },

    {
        'type': 'confirm',
        'name': 'pca',
        'message': 'pca: bool',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'input',
        'name': 'pca_components',
        'message': 'pca_components: int/float',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': '0.99'
    },


    {
        'type': 'input',
        'name': 'pca_method',
        'message': 'pca_method: string',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'linear'
    },

    {
        'type': 'input',
        'name': 'ignore_low_variance',
        'message': 'ignore_low_variance: bool.',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'linear'
    },

    {
        'type': 'confirm',
        'name': 'ignore_low_variance',
        'message': 'ignore_low_variance: bool, default = False ',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },


    {
        'type': 'confirm',
        'name': 'combine_rare_levels',
        'message': 'combine_rare_levels: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'confirm',
        'name': 'rare_level_threshold',
        'message': 'rare_level_threshold: float, default = 0.1',

        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'confirm',
        'name': 'bin_numeric_features',
        'message': 'ibin_numeric_features: list, default = None',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'confirm',
        'name': 'remove_outliers',
        'message': 'remove_outliers: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'input',
        'name': 'outliers_threshold',
        'message': 'ioutliers_threshold: float, default = 0.05',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': '0.05'
    },

    {
        'type': 'confirm',
        'name': 'remove_multicollinearity',
        'message': 'remove_multicollinearity: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'input',
        'name': 'multicollinearity_threshold',
        'message': 'multicollinearity_threshold: float, default = 0.9',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': '0.9'
    },
    {
        'type': 'confirm',
        'name': 'create_clusters',
        'message': 'create_clusters: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },

    {
        'type': 'input',
        'name': 'cluster_iter',
        'message': 'cluster_iter: int, default = 20',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': '20'
    },
    {
        'type': 'confirm',
        'name': 'polynomial_features',
        'message': 'polynomial_features: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },

    {
        'type': 'input',
        'name': 'polynomial_degree',
        'message': 'polynomial_degree: int, default = 2',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': '2'
    },
    {
        'type': 'confirm',
        'name': 'trigonometry_features',
        'message': 'trigonometry_features: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'input',
        'name': 'polynomial_threshold',
        'message': 'polynomial_threshold: float, default = 0.1',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': '0.1'
    },

    {
        'type': 'input',
        'name': 'group_features',
        'message': 'group_features: list or list of list, default = None',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },
    {
        'type': 'input',
        'name': 'group_names',
        'message': 'group_names: list, default = None',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },

    {
        'type': 'confirm',
        'name': 'feature_selection',
        'message': 'feature_selection: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'input',
        'name': 'feature_selection_threshold',
        'message': 'feature_selection_threshold: float, default = 0.8',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': '0.8'
    },
    {
        'type': 'confirm',
        'name': 'feature_interaction',
        'message': 'feature_interaction: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },

    {
        'type': 'confirm',
        'name': 'feature_ratio',
        'message': 'feature_ratio: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'input',
        'name': 'interaction_threshold',
        'message': 'interaction_threshold: bool, default = 0.01',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': '0.01'
    },

    {
        'type': 'confirm',
        'name': 'transform_target',
        'message': 'transform_target: bool, default = False',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': False
    },
    {
        'type': 'list',
        'name': 'transform_target_method',
        'message': 'transform_target_method: string, default = ‘box-cox’',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'choices': ['box-tox', 'yeo-johnson']
    },
    {
        'type': 'input',
        'name': 'session_id',
        'message': 'session_id: int, default = None',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': 'None'
    },

    {
        'type': 'confirm',
        'name': 'silent',
        'message': 'silent: bool, default = True',
        'when': lambda setup_answers: setup_answers['custom_setup'] == True,
        'default': True
    },
    {
        'type': 'confirm',
        'name': 'profile',
        'message': 'profile: bool, default = True',
        'default': True
    }]
modelling_questions = [

    {
        'type': 'list',
        'name': 'user_selected_model',
        'message': 'Select model of interest  : default = auto_select_best_model ',
        'choices': ['Auto select best model', 'Linear Regression', 'Lasso Regression', 'Ridge Regression', 'Elastic Net', 'Least Angle Regression',
                    'Lasso Least Angle Regression', 'Orthogonal Matching Pursuit', 'Bayesian Ridge', 'Automatic Relevance Determination', 'Passive Aggressive Regressor',
                    'Random Sample Consensus', 'TheilSen Regressor', 'Huber Regressor', 'Kernel Ridge', 'Support Vector Machine', 'K Neighbors Regressor', 'Decision Tree',
                    'Random Forest', 'Extra Trees Regressor', 'AdaBoost Regressor', 'Gradient Boosting Regressor', 'Multi Level Perceptron', 'Extreme Gradient Boosting',
                    'Light Gradient Boosting', 'CatBoost Regressor']

    },
    {
        'type': 'list',
        'name': 'auto_select_best_model_by',
        'message': 'auto_select_best_model_by ',
        'when': lambda modelling_answers: modelling_answers['user_selected_model'] == 'Auto select best model',
        'choices': ['MAE', 'MSE', 'RMSE', 'R2', 'RMSLE', 'MAPE']

    },

    {
        'type': 'confirm',
        'name': 'auto_tune',
        'message': 'Auto tune hyperparameters with random grid search?',
        'default': True

    },
    {
        'type': 'input',
        'name': 'train_size',
        'message': 'Training set size?',
        'default': '0.7'
    },

    {
        'type': 'input',
        'name': 'Kfolds',
        'message': 'K-fold CV: integer',
        'validate': KfoldsValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'confirm',
        'name': 'view_config',
        'message': 'view configurations?',
        'default': False
    }
]
status = [
    {
        'type': 'confirm',
        'name': 'cli_summary',
        'message': 'High level summary?',
        'default': True
    }
]
