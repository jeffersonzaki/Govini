# All imports 

import pandas as pd
import numpy as np

# Graphing
import matplotlib.pyplot as plt

# Removing unwanted characters
import re
import string

# NLP
"""
fuzzywuzzy package has a module 
called process that allows you to 
calculate the string with the highest 
similarity out of a vector of strings
"""

# Name matching packages
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import fuzzymatcher

# Data
# All given datasets
a_company_csv = pd.read_csv("Data/a__company.csv")
a_geo_csv = pd.read_csv("Data/a__geo.csv")
b_address_csv = pd.read_csv("Data/b__address.csv")
b_company_csv = pd.read_csv("Data/b__company.csv")
b_hierarchy = pd.read_csv("Data/b__hierarchy.csv")

# Merging datasets using geo_id column
a_company_all = pd.merge(a_company_csv, a_geo_csv, on="geo_id", how="inner")

# Merging b__address.csv and b__hierarchy.csv using b_entity_id column
b_address_hierarchy = pd.merge(b_address_csv, b_hierarchy, on="b_entity_id", how="inner")

# Merging b_address_hierarchy and b_company.csv using b_entity_id
b_company_all = pd.merge(b_company_csv, b_address_hierarchy, on="b_entity_id", how="inner")

# Data cleaning function
def clean_text(df, column:str):
    """Make text lowercase, 
    remove square brackers,
    and remove punctuations"""
    df[column] = [names.lower() for names in df[column]]  # Convert all letter to lowercase
    df[column] = [names.encode("ascii", errors="ignore").decode() for names in df[column]] # Remove non ascii chars
    df[column] = [re.sub("\[.*?\]", "", names) for names in df[column]]  # Remove anything in brackets
    df[column] = [re.sub("[%s]" % re.escape(string.punctuation), "", names) for names in df[column]]  # Remove punctuations
    df[column] = [re.sub("\w*\d\w*", "", names) for names in df[column]]  # Remove words with numbers in them
    return df[column]

# Separting rows to name and vendor id
a_company_name_id = a_company_all[["vendor_id", "name"]]

# Removing duplicated names
a_company_name_id.drop_duplicates(subset="name", inplace=True)

# Removing business abbreviations
remove_words = ["healthcare", "corporations", "llc", "corp", "parnters", "inc", "co", "corporation", "ltd"]
for i in remove_words:
    a_company_name_id["name"] = a_company_name_id["name"].str.replace(i, "", case = False)
	
"""
Using the clean_text
function in order to
clean the text similar to
a_company_all
"""
b_company_all["entity_name"] = clean_text(b_company_all, "entity_name")

# Separting rows to name and vendor id
b_company_name_id = b_company_all[["b_entity_id", "entity_name"]]

# Removing duplicated names
b_company_name_id.drop_duplicates(subset="entity_name", inplace=True)

# Removing business abbreviations
remove_words = ["healthcare", "corporations", "llc", "corp", "parnters", "inc", "co", "corporation", "ltd"]
for i in remove_words:
    b_company_name_id['entity_name'] = b_company_name_id['entity_name'].str.replace(i, "", case = False)
