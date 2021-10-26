import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px      # for interactive plotting; see README.md for more details
import pandas as pd

pd.options.mode.chained_assignment = None    # to deprecate an indexing warning in pandas (warning not relevant here)


'''
A function to normalize/scale stock prices such that prices of all stocks start at 1 unit currency (eg. USD) on day 1
i/p:
df = a DataFrame with first column for dates, and subsequent columns for stock prices
o/p:
x = normalized DataFrame
'''
def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:    # skip first column; contains dates
        x[i] = x[i] / x[i][0]  # divide each element in each column by the first element of that column
    return x

'''
A function to make interactive plots (using plotly express) of stock prices
i/p:
df = a DataFrame with first column for dates, and subsequent columns for stock prices
title = a title for the plot (as string)
o/p:
an interactive plot of stock prices
'''
def interactive_plot(df, title):
    fig = px.line(title = title)
    for i in df.columns[1:]:
        fig.add_scatter(x = df['Date'], y = df[i], name = i)
    fig.show()

'''
A function to generate random weights that will be assigned to the various stocks
i/p:
n = number of stocks (can be obtained by len(df.columns)-1)
o/p:
x = numpy array of n random numbers between 0 and 1, such that they add to 1
'''
def weights(n):
    x = np.random.random(n)
    x = x / np.sum(x)        # divide each element by the sum of all elements, so that the sum is now 1
    return x
    
'''
A function to perform basic portfolio analysis such as total worth and daily % returns
i/p:
dataframe = a DataFrame with first column for dates, and subsequent columns for stock prices
weights = an array of randomly generated weights for each stock
o/p:
df = a copy of dataframe, with two additional columns for 'Portfolio daily worth' and 'Portfolio daily % return'; all figures rounded to 2 decimal places
'''
def analyze_portfolio(dataframe, weights):
    df = dataframe.copy()
    
    df = normalize(df)
    
    # multiply each column containing stock data by its corresponding weight; also multiply by 1M (portfolio val. on day 1) for clear visualization
    for counter, stock in enumerate(df.columns[1:]):
        df[stock] = df[stock] * weights[counter]
        df[stock] = df[stock] * 1e06
    
    # sum of all columns (in a row) except 'Date' gives the portfolio daily worth
    df['Portfolio daily worth'] = df[df != 'Date'].sum(axis = 1)
    
    # create new column for portfolio saily percentage return
    df['Portfolio daily % return'] = 0.0
    # calculate daily percentage return according to the usual formula
    for i in range(1, len(df)):
        df['Portfolio daily % return'][i] = (df['Portfolio daily worth'][i] - df['Portfolio daily worth'][i-1]) * 100 / df['Portfolio daily worth'][i-1]
        
    return df.round(decimals = 2)