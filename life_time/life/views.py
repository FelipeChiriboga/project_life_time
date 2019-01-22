from django.shortcuts import render
from pandas import DataFrame
from sklearn.linear_model import LinearRegression

import os
import time
import pandas as pd
import numpy as np

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/DB/"
df = pd.read_csv(path + 'UNdata_Life_Expectancy.csv')

def main(request):
    text = "How much time will you spend with the people you care about?"
    return render(request, 'main.html', context={'title': text})

def sub_person_1(request):
    name1 = request.POST["firstname1"]
    gender1 = request.POST["gender1"]
    age1 = request.POST["age1"]
    country1 = request.POST["country1"]
    print(name1)
    return render (request, 'second_person.html', context={'title':
                'Result', 'first_person': [name1, gender1, age1, country1] })

def sub_person_2(request):
    name1 = request.POST["firstname1"]
    gender1 = request.POST["gender1"]
    age1 = request.POST["age1"]
    country1 = request.POST["country1"]
    name2 = request.POST["firstname2"]
    gender2 = request.POST["gender2"]
    age2 = request.POST["age2"]
    country2 = request.POST["country2"]
    print(name2)
    return render (request, 'relation.html', context={'title':
                'Result',  'first_person': [name1, gender1, age1, country1],
                           'second_person': [name2, gender2, age2, country2] })

def sub_relation(request):
    name1 = request.POST["firstname1"]
    gender1 = request.POST["gender1"]
    age1 = request.POST["age1"]
    country1 = request.POST["country1"]
    name2 = request.POST["firstname2"]
    gender2 = request.POST["gender2"]
    age2 = request.POST["age2"]
    country2 = request.POST["country2"]
    relation = request.POST["relation"]
    print(relation)
    return render (request, 'days_hours.html', context={'title':
                'Result', 'first_person': [name1, gender1, age1, country1],
                          'second_person': [name2, gender2, age2, country2],
                          'ralation': relation})

def sub_times(request):
    name1 = request.POST["firstname1"]
    gender1 = request.POST["gender1"]
    age1 = int(request.POST["age1"])
    country1 = request.POST["country1"]
    name2 = request.POST["firstname2"]
    gender2 = request.POST["gender2"]
    age2 = int(request.POST["age2"])
    country2 = request.POST["country2"]
    relation = request.POST["relation"]

    week = request.POST["week"]
    days = request.POST["days"]
    year = request.POST["year"]

    if week:
        times_seen_p1_p2 = int(week)
    elif days:
        times_seen_p1_p2 = int(days)
    else:
        times_seen_p1_p2 = int(year)

    hours = int(request.POST["hours"])

    person_1 = contact_1(name1, gender1, age1, country1, df)
    print(df.shape)
    person_2 = contact_1(name2, gender2, age2, country2, df)
    current_year = time.localtime().tm_year
    years_left = min([person_1, person_2]) - current_year
    time_left = (hours * 0.000114155) * times_seen_p1_p2 * years_left * 365
    days = int(time_left)
    hours = round((time_left - days) * 24, 1)

    return render (request, 'result.html', context={'title':
                'Result', 'first_person': [name1, gender1, age1, country1],
                          'second_person': [name2, gender2, age2, country2],
                          'ralation': relation,
                           'days_hours': [week, days, year, hours] })


def contact_1(name, gender, age, country, df):
    print(df.shape)
#    import pdb; pdb.set_trace()
    df_Germany = df.loc[df['country'] == country]
    print(df_Germany.shape)
    X = df_Germany['avg_year'].values
    X = np.array(X).reshape(-1,1)

    if gender == 'male':
        y = df_Germany['age'].values

    else:
        y = df_Germany['age_w'].values

    m = LinearRegression()
    m.fit(X,y)
    current_year = time.localtime().tm_year
    p1 = ( age - current_year - m.intercept_) / (m.coef_[0] - 1)

    return p1
