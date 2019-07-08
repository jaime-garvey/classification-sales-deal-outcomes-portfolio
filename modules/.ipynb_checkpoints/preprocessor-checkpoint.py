import pandas as pd

'''
Object to preprocess data
'''

class Preprocessor: 
    
    def __init__(self, cols_to_filter=None):
        self.cols_to_filter = cols_to_filter
        self.was_fit = False
        
    def fit(self, X_features, y_target=None):
        '''
        Learn information from training get to transform test set
        '''
        self.was_fit = True
        
        # Filter columns
        X_features_new = X_features.drop(self.cols_to_filter, axis=1)
        
        # Encode categorical variables
        self.categorical_features = X_features_new.dtypes[X_features_new.dtypes == 'object'].index
        
        dummies = pd.get_dummies(X_features_new, columns=self.categorical_features)
        self.col_names = dummies.columns
        del dummies
        
        return self
    
    def transform(self, X_features, y_target=None):
        '''
        transform the training or test data based on info learned in fit step
        '''
        if not self.was_fit:
            raise Error("Need to fit preprocessor first")
            
        # Filter columns
        X_features_new = X_features.drop(self.cols_to_filter, axis=1)
        
        # Encode categorical variables
        X_features_new = pd.get_dummies(X_features_new, columns=self.categorical_features)
        new_cols = set(self.col_names) - set(X_features_new.columns)
        
        for x in new_cols:
            X_features_new[x] = 0
        
        # Fill Null Values
        X_features_new = X_features_new.fillna(-1)   
        
        return X_features_new
    
    def fit_transform(self, X_features, y_target=None):
        '''
        fit and transform for sklearn pipeline
        '''
        
        return self.fit(X_features).transform(X_features)