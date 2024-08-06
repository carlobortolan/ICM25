import math
import statistics
import numpy as np
import scipy.stats as stats
import pandas as pd
import plotly.express as px


# Metadata
data = pd.read_csv('data/Case1.csv')
print(data.info())
print(data.describe())
data['Date'] = pd.to_datetime(data['Date'])

'''
1. Display the long-term performance of the equity markets 
'''
data_melted = data.melt(id_vars=['Date'], value_vars=data.columns[1:], var_name='Index', value_name='Value')
fig = px.line(data_melted, x='Date', y='Value', color='Index', title='Long-term performance of the equity markets', log_y=True)
# fig.show()

'''
2. Calculate mean returns and volatilities over the total period
'''

returns = data.copy()
for index in data.columns[1:]:
    for i in range(1, len(data[index])):
        returns.loc[i, index] = np.log(data.loc[i, index] / data.loc[i - 1, index])

# First row needs to be removed as it is 100% return
returns = returns.drop(0)

print(returns.info())
print(returns.head())

# Mean and SD (volatility) of the returns
results_list = []
for index in returns.columns[1:]:
    mean_return = math.exp(returns[index].mean()*12)-1
    std_return = returns[index].std()*math.sqrt(12)
    results_list.append({'Index': index, 'Mean Return p.a.': mean_return, 'Volatility': std_return})

results = pd.DataFrame(results_list)
results_melted = results.melt(id_vars='Index', value_vars=['Mean Return p.a.', 'Volatility'], var_name='Metric', value_name='Value')
fig = px.bar(results_melted, x='Index', y='Value', color='Metric', barmode='group', title='Mean returns p.a. and volatilities')
# fig.show()

'''
3. Calculate yearly returns for the stock markets
'''

# TODO

'''
4. Calculate the correlations between the markets over the period 1993-2017
'''

# TODO

'''
5. Calculate the correlations for five sub-periods
– 1993-1997
– 1998-2002
– 2003-2007
– 2008-2012
– 2013-2017
'''

# TODO

'''
6. Analyze the correlation regimes
'''

# TODO