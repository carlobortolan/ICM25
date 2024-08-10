import numpy as np
import pandas as pd
import statsmodels.api as sm

'''
Prepare MSCI world return data (Switzerland, Germany, France, UK, Japan, USA)
'''
dataMSCI = pd.read_csv('data/Case2MSCI.csv')
print(dataMSCI.info())
print(dataMSCI.describe())
dataMSCI['Date'] = pd.to_datetime(dataMSCI['Date'])


returnsMSCI = dataMSCI.copy()
for index in dataMSCI.columns[1:]:
    for i in range(1, len(dataMSCI[index])):
        returnsMSCI.loc[i, index] = np.log(dataMSCI.loc[i, index] / dataMSCI.loc[i - 1, index])

# First row needs to be removed as it is 100% return
returnsMSCI = returnsMSCI.drop(0)

print(returnsMSCI.info())
print(returnsMSCI.head())

'''
Prepare global factors return data (MSCI World, CRB Index, EUR 10Y Rate, FX USD/EUR)
'''
dataFactors = pd.read_csv('data/Case2Factors.csv')
print(dataFactors.info())
print(dataFactors.describe())
dataFactors['Date'] = pd.to_datetime(dataFactors['Date'])

returnsFactors = dataFactors.copy()
for index in dataFactors.columns[1:]:
    for i in range(1, len(dataFactors[index])):
        returnsFactors.loc[i, index] = np.log(dataFactors.loc[i, index] / dataFactors.loc[i - 1, index])

# First row needs to be removed as it is 100% return
returnsFactors = returnsFactors.drop(0)

print(returnsFactors.info())
print(returnsFactors.head())

'''
Market return on the MSCI World index return (single factor model)
'''
for country in returnsMSCI.columns[1:]:
    y = returnsMSCI[country]
    X = returnsFactors['MSCI World']
    # Add a constant to the independent variable
    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()
    # print(f"\n\n{"="*10} {country} {"="*10}")
    # print(model.summary())
    
'''
Market return on the 4 global factors (4-factor model)
'''
for country in returnsMSCI.columns[1:]:
    y = returnsMSCI[country]
    X = returnsFactors[['FX USD/EUR', 'EUR 10Y Rate' ,'CRB Index', 'MSCI World']]
    # Add a constant to the independent variable
    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()
    # print(f"\n\n{"="*10} {country} {"="*10}")
    # print(model.summary())
