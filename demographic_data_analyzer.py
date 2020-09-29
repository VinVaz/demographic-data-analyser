import pandas as pd
import numpy as np

adult_file = pd.read_csv("./adult.data", names=["age","workclass","fnlwgt",
                                                "education","education-num",
                                                "marital-status","occupation",
                                                "relationship","race","sex",
                                                "capital-gain","capital-loss",
                                                "hours-per-week",
                                                "native-country","salary"])
                                                



  
#def calculate_demographic_data (data):
  
# how many people of each race are represented in this dataset?  
race_series = adult_file["race"].value_counts()

# average age of men
age_series = adult_file["age"]
sex_series = adult_file['sex'].fillna('')

male_age = age_series[sex_series.str.strip()=='Male']
avg_male_age = male_age.mean()

edu_series = adult_file["education"]
total = edu_series.count()

# percentage of people who have a Bachelor’s degree
has_bachelors = edu_series[edu_series.str.strip()=='Bachelors']
pct_bachelors = 100 * has_bachelors.count() / total


# percentage of people with advanced education 
# (Bachelors, Masters, or Doctorate) that make more than 50K

adv_degrees = ['Bachelors','Masters','Doctorate']
country_sal_df = adult_file[['education', 'salary']]

has_high_sal = country_sal_df['salary'].str.strip()=='>50K'
high_sal_series = country_sal_df['education'][has_high_sal]
num_high_sal = high_sal_series.count()

has_adv_ed_high_sal = high_sal_series.str.strip().isin(adv_degrees)
adv_ed_high_sal_series = high_sal_series[has_adv_ed_high_sal]
num_adv_ed_high_sal = adv_ed_high_sal_series.count()


pct_educ_salary = 100 * num_adv_ed_high_sal / total

# percentage of people without advanced education that make more than 50K
pct_uneduc_salary = 100 * (num_high_sal - num_adv_ed_high_sal) / total

# minimum number of hours a person works per week
hours_week_series = adult_file["hours-per-week"]
min_hours_week = hours_week_series.min()

# percentage of the people who work the minimum number of hours per week 
# that have a salary of more than 50K?
work_min_hours = hours_week_series==min_hours_week
num_ppl_work_min_high_sal = high_sal_series[work_min_hours].count()

pct_work_min_high_sal = 100 * num_ppl_work_min_high_sal / total

# percentage and country with the highest percentage of people that earn >50K
country_sal_df = adult_file[['native-country', 'salary']]

has_high_sal = country_sal_df['salary'].str.strip()=='>50K'

country_high_sal = country_sal_df['native-country'][has_high_sal]
# clean undefined countries
country_high_sal = country_high_sal.str.strip().replace('?', np.nan).dropna()

# reindex eliminating rows with undefined countries
country_sal_df = country_sal_df.reindex(index=country_high_sal.index)

num_country = country_sal_df.groupby('native-country').count()
# rename the new series column to represent the number of people that earn >50K
num_country.columns = ['rich-population']

pct_country =100 * num_country / total
print(pct_country)

# the most popular occupation for those who earn >50K in India





