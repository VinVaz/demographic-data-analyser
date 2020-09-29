import pandas as pd

adult_file = pd.read_csv("./adult.data", names=["age","workclass","fnlwgt",
                                                "education","education-num",
                                                "marital-status","occupation",
                                                "relationship","race","sex",
                                                "capital-gain","capital-loss",
                                                "hours-per-week",
                                                "native-country","salary"])
                                                



  
#def calculate_demographic_data (data):
  
# How many people of each race are represented in this dataset?  
race_series = adult_file["race"].value_counts()

# What is the average age of men?
age_series = adult_file["age"]
sex_series = adult_file['sex'].fillna('')

male_age = age_series[sex_series.str.strip()=='Male']
avg_male_age = male_age.mean()
