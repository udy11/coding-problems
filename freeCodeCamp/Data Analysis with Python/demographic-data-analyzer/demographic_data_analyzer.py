import pandas as pd

def dictmax(d):
     v = list(d.values())
     vmx = max(v)
     return list(d.keys())[v.index(vmx)], vmx

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.value_counts(df.loc[:, 'race'])

    # What is the average age of men?
    average_age_men = round(df.loc[:, 'age'][df.loc[:, 'sex'] == 'Male'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(100.0 * (df.loc[:, 'education'].to_numpy() == 'Bachelors').sum() / df.shape[0], 1)    # fastest method as per https://stackoverflow.com/a/35277776/1587171

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # higher degree and higher salary masks
    dfhe = df.loc[:, 'education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    dfle = ~dfhe
    dfhs = df.loc[:, 'salary'].to_numpy() == '>50K'
    
    # percentage with salary >50K
    higher_education_rich = round(100.0 * (dfhe & dfhs).sum() / dfhe.sum(), 1)
    lower_education_rich = round(100.0 * (dfle & dfhs).sum() / dfle.sum(), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.loc[:, 'hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    dflw = df.loc[:, 'hours-per-week'].to_numpy() == min_work_hours
    rich_percentage = round(100.0 * (dfhs & dflw).sum() / dflw.sum(), 1)

    # What country has the highest percentage of people that earn >50K?
    cs = {c : 100 * (df.loc[:, 'salary'][df.loc[:, 'native-country'].to_numpy() == c].to_numpy() == '>50K').sum() / (df.loc[:, 'native-country'].to_numpy() == c).sum() for c in df.loc[:, 'native-country'].unique()}
    highest_earning_country, highest_earning_country_percentage = dictmax(cs)
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[:, 'occupation'][dfhs & (df.loc[:, 'native-country'].to_numpy() == 'India')].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
