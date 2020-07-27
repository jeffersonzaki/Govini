# Govini

<p align="center">
  <img src="https://www.rosette.com/wp-content/uploads/2017/12/name-dedupe.svg">
</p>

- Problem: Mapping entities between disparate datasets. Collecting data from a veriety of sources, and knowing that a certain entity is the same from one dataset to another is essential.
    - Example: For example, there may be a company named "FOO" in one data set, and a company named "foo 123" in another. We need to be able to determine with a high enough confidence that those are the same entity. However, a majority of the time, the data does not share a unique key.
    
- What Needs To Happen: Need to create an algorithm that could automatically tie related entities together. The output should have the matches as well as a confidence score for the match.

- What I'm Given:
    - Two sample datasets, and it'll be up to you to generate a mapping between the two. In most cases, the mapping should be one to one. An ID from data set A should map to an ID in data set B.
    
- Files Described Below:
    - Procurement Data:

        - data/mdl__dim_vendor.csv - Company Information
        - data/mdl__dim_geo.csv - Location Information
        - mdl__dim_vendor.csv references mdl__dim_geo.csv via the column geo_id.

    - Finance Data:

        - data/factset__ent_entity_coverage.csv - Company Information
        - data/factset__ent_entity_structure.csv - Company Hierarchy
        - data/factset__ent_entity_address.csv - Location Information

**All of these files are tied together using factset_entity_id.**

**End Goal**
- Explore the data
- Map **mdl__dim_vendor.vendor_id** to corresponding **factset__ent_entity_coverage.factset_entity_id**
- A file containing three columns: vendor_id, factset_entity_id, confidence_of_match
- README file that explains how your algorithm works

## Content Summary
- [Data](https://github.com/jeffersonzaki/Govini/tree/master/Data) - Contains csv files used

- [Scripts](https://github.com/jeffersonzaki/Govini/tree/master/Scripts) - Contains a python file with production code

- [gitignore](https://github.com/jeffersonzaki/Govini/blob/master/.gitignore) - Ignores certain items

- [Dockerfile](https://github.com/jeffersonzaki/Govini/blob/master/Dockerfile) - Used to build an image in docker using this jupyter notebook contents

- [Exploratory Data Analysis](https://github.com/jeffersonzaki/Govini/blob/master/EDA.ipynb) - Goes into the data in detail to learn more about the data that was given

- [README](https://github.com/jeffersonzaki/Govini/blob/master/README.md) - Summary of project

- [Work with no edit](https://github.com/jeffersonzaki/Govini/blob/master/all-work-with-no-edits.ipynb) - Contains my work that hasn't been cleaned. First impressions

- [NLP](https://github.com/jeffersonzaki/Govini/blob/master/nlp-fuzzy-name-matching.ipynb) - Cleaned NLP notebook. Fuzzy name matching is used to connect the disparate dataset

- [Preprocessing](https://github.com/jeffersonzaki/Govini/blob/master/preprocessing.ipynb) - Cleaning data

## Project Member
- [Zaki Jefferson](https://github.com/jeffersonzaki)

## Data
- [AWS-Govini](https://s3.amazonaws.com/BUCKET_FOR_FILE_TRANSFER/interview.tar.xz)
