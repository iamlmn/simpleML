import yaml

meta_job_info = dict()

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


with open('config.yml', 'w') as outfile:
    yaml.dump(setup, outfile, default_flow_style=False)


# Reading config again

# Read YAML file
with open("config.yml", 'r') as stream:
    setup_loaded = yaml.safe_load(stream)

assert setup == setup_loaded