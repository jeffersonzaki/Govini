# Govini

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
- [gitignore](https://github.com/jeffersonzaki/Govini/blob/master/.gitignore) - Ignores certain items
- [Dockerfile](https://github.com/jeffersonzaki/Govini/blob/master/Dockerfile) - Used to build an image in docker using this jupyter notebook contents
- [README](https://github.com/jeffersonzaki/Govini/blob/master/README.md) - Summary of 
