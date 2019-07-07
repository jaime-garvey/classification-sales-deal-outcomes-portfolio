import pandas as pd
import numpy as np

'''
Set of helper functions from Sales Deals Classification Portfolio Project 
'''


def read_in_dataset(dataset, verbose=False):
    '''
    Read in dataset (csv format) to pandas dataframe
    
    Keyword Arguments:
    ------------------
    * dataset - string with dataset filename
    * verbose - True will print intormation about the dataset
    
    Returns:
    --------
    a pandas dataframe
    '''
    
    df = pd.read_csv('../data/raw/{}'.format(dataset))
    
    if verbose:
        print('\n{0:-^80}'.format(' Reading in the following dataset: {0}'.format(dataset)))
        print("\n Shape: {0} rows and {1} columns".format(*df.shape))
        print('\n{0:-^80}\n'.format(' It has the following columns '))
        print(df.columns)
        print('\n{0:-^80}\n'.format(' The first 5 rows look like this '))
        print(df.head())
        
    return df



