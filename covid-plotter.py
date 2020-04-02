import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Chart COVID-19 Data')  # PARSE ARGUMENTS
parser.add_argument('-country',
                    help='Country to chart')
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
parser.add_argument('-ctparam',
                    help='Specify a parameter for Covid Tracking Project: ')
args = parser.parse_args()

country = args.country
type = args.type or 'confirmed'

if country != 'US':
    print("poop")
    countries = country.split('/')
    # Show confirmed cases in a country
    if type == 'confirmed':
        y_title = args.ytitle or "Cases"
        confirmed = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        fig = go.Figure()
        for country in countries:
            a = confirmed[confirmed['Country/Region'] == country]
            dates = list(a)
            dates = dates[4:-1]
            cases = []
            for date in dates:
                cases.append(list(confirmed[confirmed['Country/Region'] == country][date])[0])
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
        print("poop")
        y_title = args.ytitle or "Cases"
        deaths = pd.read_csv(
            'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        a = deaths[deaths['Country/Region'] == country]
        dates = list(a)
        dates = dates[4:-1]
        cases = []
        for date in dates:
            cases.append(list(deaths[deaths['Country/Region'] == country][date])[0])
        fig = go.Figure()
        print("poop")
        fig.add_trace(go.Scatter(x=dates, y=cases,
                                 name='confirmed',
                                 mode='lines+markers'))
        fig.update_layout(title=args.title,
                          font={"size": 20},
                          xaxis_title='',
                          yaxis_title=y_title
                          )
        fig.show()
    # Show recovered
    if type == 'recovered':
        y_title = args.ytitle or "Cases"
        rec = pd.read_csv(
            'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        a = rec[rec['Country/Region'] == 'US']
        dates = list(a)
        dates = dates[4:-1]
        cases = []
        for date in dates:
            cases.append(list(rec[rec['Country/Region'] == country][date])[0])
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=cases,
                                 name='confirmed',
                                 mode='lines+markers'))
        fig.update_layout(title=args.title,
                          font={"size": 20},
                          xaxis_title='',
                          yaxis_title=y_title
                          )
        fig.show()

if country == 'US':
    df = pd.read_csv('https://covidtracking.com/api/us/daily.csv')
    type = args.type or 'positive'
    y_title = args.ytitle or ''
    dates = []
    for foo in df['date'].values:
        year = str(foo)[0:4]
        month = str(foo)[4:6]
        day = str(foo)[6:8]
        dates.append(year + '-' + month + '-' + day)
    cases = df[type].values
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=cases,
                             name='confirmed',
                             mode='lines+markers+text',
                             text=cases,
                             textposition='top left',
                             textfont=dict(
                                 family='sans serif',
                                 size=14,
                                 color='#ff7f0e'
                             )
                             ))
    fig.update_layout(title=args.title,
                      font={"size": 20},
                      xaxis_title='',
                      yaxis_title=y_title
                      )
    fig.update_xaxes(nticks=20)
    fig.show()

if args.usstate:
    ct_param = args.ctparam or 'positive'
    y_title = args.ytitle or ''
    if args.usstate:
        state = args.usstate
        dates = []
        df = pd.read_csv('http://covidtracking.com/api/states/daily.csv')
        blob = df[df['state'] == state]
        for foo in blob['date'].values:
            year = str(foo)[0:4]
            month = str(foo)[4:6]
            day = str(foo)[6:8]
            dates.append(year + '-' + month + '-' + day)
        if ct_param == 'positive':
            y = blob['positive'].values
        if ct_param == 'positiveIncrease':
            y = blob['positiveIncrease'].values
        if ct_param == 'negative':
            y = blob['negative'].values
        if ct_param == 'negativeIncrease':
            y = blob['negativeIncrease'].values
        if ct_param == 'pending':
            y = blob['pending'].values
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=y,
                                 name='confirmed',
                                 mode='lines+markers'))
        fig.update_layout(title=args.title,
                          font={"size": 20},
                          xaxis_title='',
                          yaxis_title=y_title
                          )
        fig.show()
