import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Chart COVID-19 Data')  # PARSE ARGUMENTS
parser.add_argument('-country',
                    help='Country to chart')
parser.add_argument('-list',
                    help='List of available thingies: [countries]')
parser.add_argument('-type',
                    help='Confirmed, deaths, or recovered: [confirmed] [deaths] [recovered]')
parser.add_argument('-sw',
                    help='Plotting software to be used: [plotly] [matplotlib]')
parser.add_argument('-filter',
                    help='Subtract a trace from primary plot: [confirmed] [deaths] [recovered]')
parser.add_argument('-usstate',
                    help='Specify a US state: [state]')
parser.add_argument('-title',
                    help='Specify a title: [title]')
parser.add_argument('-ytitle',
                    help='Specify a title for Y axis: [title]')
parser.add_argument('-pc',
                    help='Per capita: [yes] ')
args = parser.parse_args()

states_df = pd.read_csv('states.csv')

if args.list == 'countries':
    confirmed = pd.read_csv(
        'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    a = confirmed['Country/Region']
    print(list(a))

country = args.country
type = args.type or 'confirmed'

countries = country.split('/')
# Show confirmed cases in a country
if type == 'confirmed':
    y_title = args.ytitle or "Confirmed Cases"
    df = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    fig = go.Figure()
    for country in countries:
        a = df[df['Country/Region'] == country]
        dates = list(a)
        dates = dates[4:-1]
        cases = []
        for date in dates:
            # Sum up various entries for same country eg China
            bar = np.sum(list(df[df['Country/Region'] == country][date]))
            cases.append(bar)
        fig.add_trace(go.Scatter(x=dates, y=cases,
                                 name=country,
                                 mode='lines+markers'))
    fig.update_layout(title=args.title,
                      font={"size": 20},
                      xaxis_title='',
                      yaxis_title=y_title
                      )
    fig.show()
# Show deaths
if type == 'deaths':
    y_title = args.ytitle or "Deaths"
    df = pd.read_csv(
        'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    fig = go.Figure()
    for country in countries:
        a = df[df['Country/Region'] == country]
        dates = list(a)
        dates = dates[4:-1]
        cases = []
        for date in dates:
            # Sum up various entries for same country eg China
            bar = np.sum(list(df[df['Country/Region'] == country][date]))
            cases.append(bar)
        fig.add_trace(go.Scatter(x=dates, y=cases,
                                 name=country,
                                 mode='lines+markers'))
    fig.update_layout(title=args.title,
                      font={"size": 20},
                      xaxis_title='',
                      yaxis_title=y_title
                      )
    fig.show()
# Show recovered
if type == 'recovered':
    y_title = args.ytitle or "Recovered Cases"
    df = pd.read_csv(
        'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    fig = go.Figure()
    for country in countries:
        a = df[df['Country/Region'] == country]
        dates = list(a)
        dates = dates[4:-1]
        cases = []
        for date in dates:
            # Sum up various entries for same country eg China
            bar = np.sum(list(df[df['Country/Region'] == country][date]))
            cases.append(bar)
        fig.add_trace(go.Scatter(x=dates, y=cases,
                                 name=country,
                                 mode='lines+markers'))
    fig.update_layout(title=args.title,
                      font={"size": 20},
                      xaxis_title='',
                      yaxis_title=y_title
                      )
    fig.show()