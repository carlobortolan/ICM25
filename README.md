# ICM25

Analysis of the long-term evolution of international equity markets (average returns, volatilities, long-term correlations) and economic risks of European stock markets.

![note]
This project has been inspired by the _International Capital Markets
and Investment Practice_ lecture held during S2024 by _Prof. Dr. Peter Oertmann_.

## Case 1: Analyzing 25 years of stock market returns

Analysis of the **longterm evolution of international equity markets**, i.e.
- Average returns
- Volatilities
- Long-term correlations between markets
- Correlation regimes

Data set ([Case1.csv](./data/Case1.csv)) includes 16 stock market indices in local currencies covering developed markets in North America, Europe and Asia-Pacific
- Monthly stock market data starting on December 31, 1992, and ending on February 28, 2018
- Indexed to ”100” at the beginning of the period

## Case 2: Rational asset pricing and multifactor models

Data set ([Case2Factors.csv](./data/Case2Factors.csv) and [Case2MSCI.csv](./data/Case2MSCI.csv)) include monthly total return index data over the 1st decade of the 21st century, from January 2000 to December 2009, denominated in EUR for 10 European stock markets and 4 global risk factors.

[Case2.py](./case2.py) analyzes the **relationships between the returns of the stock markets and the changes of the global factors** using the following regressions for each market:
- **Market return on the MSCI World index return** (_single factor model_)
- **Market return on the 4 global factors** (_4-factor model_)

---

© Carlo Bortolan

> Carlo Bortolan &nbsp;&middot;&nbsp;
> GitHub [carlobortolan](https://github.com/carlobortolan) &nbsp;&middot;&nbsp;
> contact via [carlobortolan@gmail.com](mailto:carlobortolan@gmail.com)
