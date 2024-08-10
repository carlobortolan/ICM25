# ICM25

Analysis of the long-term evolution of international equity markets (average returns, volatilities, long-term correlations) and economic risks of European stock markets.

> [!Note] 
> This project has been inspired by the _International Capital Markets and Investment Practice_ lecture held during S2024 by _Prof. Dr. Peter Oertmann_.

## Case 1: Analyzing 25 years of stock market returns

Analysis of the **longterm evolution of international equity markets**, i.e.
- Average returns
- Volatilities
- Long-term correlations between markets
- Correlation regimes

Data set ([Case1.csv](./data/Case1.csv)) includes 16 stock market indices in local currencies covering developed markets in North America, Europe and Asia-Pacific
- Monthly stock market data starting on December 31, 1992, and ending on February 28, 2018
- Indexed to ”100” at the beginning of the period

![case1a](https://github.com/user-attachments/assets/f3b92af7-c614-4e5e-aac3-c33dab097881)
![case1b](https://github.com/user-attachments/assets/3a270736-9a91-484e-9783-c483aaa93653)
![case1c](https://github.com/user-attachments/assets/42c354cf-3a83-45d9-a133-47616eec2c3d)


## Case 2: Rational asset pricing and multifactor models

Data set ([Case2Factors.csv](./data/Case2Factors.csv) and [Case2MSCI.csv](./data/Case2MSCI.csv)) include monthly total return index data over the 1st decade of the 21st century, from January 2000 to December 2009, denominated in EUR for 10 European stock markets and 4 global risk factors.

[Case2.py](./case2.py) analyzes the **relationships between the returns of the stock markets and the changes of the global factors** using the following regressions for each market:
- **Market return on the MSCI World index return** (_single factor model_)
- **Market return on the 4 global factors** (_4-factor model_)

```
================================ Switzerland =================================
                            OLS Regression Results                            
==============================================================================
Dep. Variable:            Switzerland   R-squared:                       0.674
Model:                            OLS   Adj. R-squared:                  0.662
Method:                 Least Squares   F-statistic:                     59.37
Date:                Sat, 10 Aug 2024   Prob (F-statistic):           4.25e-27
Time:                        23:18:03   Log-Likelihood:                 280.69
No. Observations:                 120   AIC:                            -551.4
Df Residuals:                     115   BIC:                            -537.4
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
const            0.0035      0.002      1.565      0.120      -0.001       0.008
FX USD/EUR       0.2081      0.075      2.759      0.007       0.059       0.358
EUR 10Y Rate     0.0626      0.052      1.206      0.230      -0.040       0.165
CRB Index       -0.1146      0.048     -2.383      0.019      -0.210      -0.019
MSCI World       0.7431      0.053     14.017      0.000       0.638       0.848
==============================================================================
Omnibus:                        4.731   Durbin-Watson:                   1.689
Prob(Omnibus):                  0.094   Jarque-Bera (JB):                4.503
...
==============================================================================
```

---

© Carlo Bortolan

> Carlo Bortolan &nbsp;&middot;&nbsp;
> GitHub [carlobortolan](https://github.com/carlobortolan) &nbsp;&middot;&nbsp;
> contact via [carlobortolan@gmail.com](mailto:carlobortolan@gmail.com)
