# Project-1

TEDSA (Treatment Episode Data Set – Admissions) Analysis

Overview
- This project involves the analysis and cleaning of TEDSA data from the year 2020. TEDSA is a comprehensive dataset that captures information about individuals admitted to substance abuse treatment programs. The analysis includes data preprocessing steps, handling missing values, creating new informative columns, creating visuals, and exploring key demographic and drug preference trends.



Project Structure

Data Exploration:
- The initial steps involve loading the TEDSA dataset and exploring its structure.
- Display basic information such as columns, a snapshot of the data, and summary statistics.
- Identify and handle null values appropriately.

Data Cleaning:
- Drop rows with missing values if necessary.
- Handle duplicates if present in the dataset.

Demographic Analysis:
- Convert numerical codes to meaningful labels for gender, ethnicity, age, and location.
- Explore and visualize the distribution of demographic variables.

Geographical Analysis:
- Convert geographical codes to meaningful labels for region, division, and state.
- Analyze and present distribution based on regions, divisions, and states.

Drug Preference Analysis:
- Map numerical codes to meaningful labels for primary drug preferences.
- Explore and visualize the distribution of primary drug preferences.

Saving Cleaned Data:
- Save the cleaned dataset to a new CSV file for future analysis.



Data Dictionary

- GENDER_LABEL: Gender information with labels.
- ETHNICITY_LABEL: Ethnicity information with labels.
- AGE_LABEL: Age groups with labels.
- Location_by_region: Geographical information by region.
- Location_by_division: Geographical information by division.
- Location_by_state: Geographical information by state.
- Primary_Drug_Preference: Information about the primary drug of choice with labels.

Conclusion
- This project provides valuable insights into the demographic and drug preference trends of individuals admitted to substance abuse treatment programs based on the TEDSA dataset for the year 2020.

