import pandas as pd

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
edu_sal_df = adult_file[['education', 'salary']]


has_adv_ed = edu_sal_df['education'].str.strip().isin(adv_degrees)
sal_series = edu_sal_df[has_adv_ed]['salary']
predef_salary_series = sal_series[sal_series.str.strip()=='>50K']

pct_educ_salary = 100 * predef_salary_series.count() / total

print(pct_educ_salary)






