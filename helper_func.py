# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

def glance(data):
    """Function that prints all data information
        
    Args:
        data: data to be understood - dataframe
    
    Return:
        None: Only prints summary info to the scrren
    """
    
    # checking the data
    print('----- Glimpse of the Data-----\n')
    print(data.head(2))
    
    print(data.tail(2))
    
    # checking data info
    print('\n\n----- Data Info ------\n')
    print(data.info())
    
    # viewing the columns
    print('\n\n----- Data Columns ------\n')
    print(data.columns)
    
    # viewing summary statistics
    print('\n\n----- Data Summary ------\n')
    print(data.describe(include='all'))
    
    
def missing_values(data):
    """Function that checks for null values and computes the percentage of null values
    Args:
        data: loaded dataframe
    Return:
        dataframe: dataframe of total null values with corresponding percentages
    """
    total = data.isnull().sum().sort_values(ascending=False)   # create an empty datafram
    percentage = round((total / data.shape[0]) * 100, 2)
    
    return pd.concat([total, percentage], axis=1, keys=['Total','Percentage'])
    """Function that checks for null values and computes the percentage of null values
    Args:
        data: loaded dataframe
    Return:
        dataframe: dataframe of total null values with corresponding percentages
    """
    total = data.isnull().sum().sort_values(ascending=False)   # create an empty datafram
    percentage = round((total / data.shape[0]) * 100, 2)
    
    return pd.concat([total, percentage], axis=1, keys=['Total','Percentage'])

