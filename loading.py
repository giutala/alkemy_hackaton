import pandas as pd
import os
import pandas as pd
from helpermodules.memory_handling import PickleHelper

def list_files_in_directory(base_dir):
    """
    List all files in the specified directory and its subdirectories.
    
    Args:
        base_dir (str): The base directory to search for files.
    
    Returns:
        None: Prints the full path of each file found.
    """
    for dirname, _, filenames in os.walk(base_dir):
        for filename in filenames:
            print(os.path.join(dirname, filename))

def load_datasets(dataset_names, base_path):
    """
    Load multiple datasets from CSV files into a dictionary.
    
    Args:
        dataset_names (list of str): List of dataset names (without the .csv extension).
        base_path (str): The base path where the datasets are located.
    
    Returns:
        dict: A dictionary with dataset names as keys and DataFrames as values.
              If a dataset cannot be loaded, its value will be None.
    """
    datasets = {}
    for name in dataset_names:
        file_path = os.path.join(base_path, name + '.csv')
        try:
            datasets[name] = pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            datasets[name] = None
    return datasets

def merge_datasets(datasets):
    """
    Merge multiple datasets into a single DataFrame based on predefined keys.
    
    Args:
        datasets (dict): A dictionary of DataFrames to be merged.
    
    Returns:
        DataFrame: A merged DataFrame containing data from all provided datasets.
    """
    # Start by merging orders with customers
    merged = pd.merge(datasets['olist_orders_dataset'], datasets['olist_customers_dataset'], on='customer_id', how='left')

    # Define the merge keys for subsequent datasets
    merge_keys = {
        'order_items': 'order_id',
        'order_payments': 'order_id',
        'order_reviews': 'order_id',
        'sellers': 'seller_id',
        'products': 'product_id',
        'product_category_name_translation': 'product_category_name'  # Make sure this dataset is loaded correctly
    }

    # Merge each dataset into the main merged DataFrame
    for name, key in merge_keys.items():
        if name in datasets and datasets[name] is not None:
            merged = pd.merge(merged, datasets[name], on=key, how='left')

    return merged

# Base path for datasets
base_path = '/kaggle/input/brazilian-ecommerce/'

# Dataset names
dataset_names = [
    'olist_customers_dataset', 
    'olist_order_items_dataset', 
    'olist_order_payments_dataset', 
    'olist_order_reviews_dataset', 
    'olist_orders_dataset', 
    'olist_sellers_dataset', 
    'olist_products_dataset', 
    'product_category_name_translation'
]

# Load datasets from the specified path
datasets = load_datasets(dataset_names, base_path)

# Display the first few rows of each dataset to understand their structure
for name, df in datasets.items():
    if df is not None:
        print(f"\nFirst few rows of {name}:")
        print(df.head())
    else:
        print(f"Failed to load {name}")

# Assuming individual datasets need to be loaded separately (for demonstration)
datasets = {
    'olist_customers_dataset': pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_customers_dataset.csv'),
    'order_items': pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_order_items_dataset.csv'),
    'order_payments': pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_order_payments_dataset.csv'),
    'order_reviews': pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_order_reviews_dataset.csv'),
    'olist_orders_dataset': pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_orders_dataset.csv'),
    'sellers': pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_sellers_dataset.csv'),
    'products': pd.read_csv('/kaggle/input/brazilian-ecommerce/olist_products_dataset.csv'),
    'product_category_name_translation': pd.read_csv('/kaggle/input/brazilian-ecommerce/product_category_name_translation.csv')
}

# Merge the loaded datasets into a single DataFrame
merged_df = merge_datasets(datasets)

# Save the merged DataFrame using PickleHelper
PickleHelper(obj=merged_df).pickle_dump(filename='cleaned_nasdaq_dataframe')
