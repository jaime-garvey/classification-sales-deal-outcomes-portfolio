import pandas as pd
import numpy as np

'''
Set of helper functions from Sales Deals Classification Portfolio Project 
'''


def read_in_dataset(dataset, data_folder='raw', verbose=False):
    ''' 
    Read in dataset (csv format) to pandas dataframe
    
    Keyword Arguments:
    ------------------
    * dataset - string with dataset filename
    * data_folder - string with either raw or processed
    * verbose - True will print intormation about the dataset
    
    Returns:
    --------
    a pandas dataframe
    '''
    
    df = pd.read_csv('../data/{}/{}'.format(data_folder, dataset))
    
    if verbose:
        print('\n{0:-^80}'.format(' Reading in the following dataset: {0}'.format(dataset)))
        print("\n Shape: {0} rows and {1} columns".format(*df.shape))
        print('\n{0:-^80}\n'.format(' It has the following columns '))
        print(df.columns)
        print('\n{0:-^80}\n'.format(' The first 5 rows look like this '))
        print(df.head())
        
    return df


def filter_duplicates(dataset, random_state=0):
    ''' 
    Filter duplicate opportunites out of dataset
    
    Keyword Arguments:
    ------------------
    * dataset - dataframe 
    Returns:
    --------
    a pandas dataframe
    '''
    
    multiple_records = dataset[dataset.duplicated(subset='Opportunity Number', keep=False)].sort_values('Opportunity Number')
    one_record = dataset[dataset.groupby('Opportunity Number')['Opportunity Number'].transform('count') ==1]
    
    duplicates = dataset[dataset.duplicated(keep=False)]
    same_opp_nums_not_dup = multiple_records[~multiple_records['Opportunity Number'].isin(duplicates['Opportunity Number'])]
    
    #Sample opportunities with multiple records
    reduced_data = multiple_records.sample(frac=1, random_state=0).groupby('Opportunity Number').head(1)
    reduced_data = pd.concat([one_record, reduced_data])
    
    #drop duplicates
    reduced_data = reduced_data.drop_duplicates()
    
    return reduced_data

    
def get_data(dset_type):
    '''
    Get Features (X) and Target(y)
    
    Keyword Arguments:
    ------------------
    dset_type - string with either 'train' or 'test' 
    
    Returns:
    --------
    Tuple of pandas dataframe for features(X) and series for target(y)
    '''
    
    if dset_type == 'train':
        filename = 'sales_data_train.csv'
        df = read_in_dataset(dataset=filename, data_folder='processed')
        df = filter_duplicates(df)
        
    else:
        filename = 'sales_data_test.csv'
        df = read_in_dataset(dataset=filename, data_folder='processed')
    
    df.set_index('Opportunity Number', inplace=True)
        
    X = df.loc[:, df.columns != 'Opportunity Result']
    y = df['Opportunity Result']
    
    return X, y

    
def get_percent(part, whole):
    ''' Calculate percent using two series or dataframes
    '''
    percent = (len(part)/len(whole))*100
    return round(percent, 1)