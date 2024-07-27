# ICM
International Capital Markets and Investment Practice Exercises

## Problems and questions 1-10 [21 min]
1. What is the core statement of Fama’s Efficient Market Hypothesis (EMH)?
    > _“A market in which prices always fully reflect available information is called efficient”_
2. What are the implications of the EMH?
    > - _It is impossible to systematically outperform the market by deviating from the market portfolio_
    > - _Passive investing at minimal cost is the rational approach_
    > - _Active strategies are expected to underperform the market by trading costs and management fees_
3. Explain the three forms of market efficiency.
    > - _Strong form: fully reflect public and private information_
    > - _Semi-strong form: fully reflect all public information_
    > - _Weak-strong form: fully reflect past prices_
4. What is the idea behind “efficiently inefficient markets” as formulated by Pedersen?
    > _Suggests markets are inefficient to an extent that compensates professional investors for their costs and risks_
5. Briefly explain the concept of adaptive markets.
    > _Market dynamics are driven by evolutionary forces and behavioral adaptations (behavioral biases, evolution at the speed of thought, survival as ultimate driving force)_
6. Name the three major fields for harvesting risk premiums.
    > _Asset class premiums, style premiums, strategy premiums_
7. Name three economically motivated investment styles.
    > - _Value inveesting: Buy cheap stocks_
    > - _Trend-following investing: Buy securities that have been rising_
    > - _Liquidity provision: Buy securities with high liquidity risk_
    > - _Carry trading; Buy securities with high carry_
    > - _Low-risk investing: Buy safe securities with leverage_
    > - _Quality investing: Buy high-quality securities_
8. From 1 May 2019 to 1 May 2020 the closing price of Apple stocks (NASDAQ: AAPL) increased from
210.52 USD to 289.07 USD. Calculate the simple return and the continuously compounded return.
    > _Simple return: `(P1-P0)/P0 = 0.373`_
    > _Cont. comp. return: `ln(P1/P0) = 0.317`_
9. The yearly volatility of the German stock market index DAX over the period from January 1993 to
February 2018 is 21.12% (see Case 1). Calculate the monthly volatility and the daily volatility of that
index.
    > - `Yearly volatility = monthly volatility * sqrt(12 months) = 0.2112`
    > - `Monthly volatility = daily volatility * sqrt(22 days)_ = 0.0610`
    > - `Daily volatility = 0.0130`
10. The volatility of the S&P500 (US stock market) is 14.29% and the volatility of the Nikkei (Japanese stock
market) is 20.03% (see Case 1). The correlation between the two stock markets is 0.56. Calculate the
volatility of a portfolio with 40% invested in S&P500 and 60% invested in Nikkei.
    > `sqrt( σ(A)² * a² + σ(B)² * b² + 2*a*b*σ(A)*σ(B)*Corr(A,B) )`
    >
    > `= sqrt( .1429²*.4² + .2003²*.6² + 2*.4*.6*.1429*.2003*.56 ) = 0.1594`

## Problems and questions 11-20 [39 min]
11. What is roughly the long-term equity risk premium in accordance with the study of Dimson, Marsh and
Staunton?
    > _Risk and return on capital markets -> 3.8% over the period 1900 to 2010_
12. What is the “typical” correlation between stocks and bonds measured over long periods of time
(approximate value)?
    > _coefficient of 0.24_
13. The correlation between stock and bond returns fluctuates over time: What is the fundamental
explanation of a negative correlation? What is the fundamental explanation of a positive correlation?
    > _Negative correlation for period of 0 interest rate / low inflation; positive correlation for high inflation_
14. Explain the typical relationship between the volatilities on two stock markets and the correlation between
the markets.
    > - _If the risk in a market increases, the correlation with other markets also increases_
    > - _Volatility is higher when markets go down_
    > - _Higher correlations are detected when equity markets go down simultaneously_
15. Volatilities and correlations between markets vary over time: Briefly explain the stylized empirical facts
and the implications for investors.
    > - _Optimal portfolios are unstable because market parameters are time-varying_
    > - _Bad news lead to higher volatility than good news_
    > - _International diversification benefits seem to vanish in exactly those market environments when they are most strongly needed (down-down > up-up)_
    > - _Widely used portfolio risk measures such as VaR, or shortfall, are affected by asymmetric parameters_
16. Explain why returns on international investments are affected by exchange rate movements.
    > - _Directly, because they have to be translated from foreign to domestic currency units (numeraire currency units)_
    > - _Indirectly, because asset prices react to shifts in exchange rates_
17. On 1 June 2018 the closing price of an Apple stock is 190.24 USD and 1 EUR costs 1.17 USD; on 1
June 2020 the closing price of an Apple stock is 321.85 USD and 1 EUR costs 1.11 USD. Calculate the
stock return over that 2-year period in USD and in EUR.
    > - _Return in % EUR:_ `(P1[USD] / EUR1[USD]) / (P0[USD] / EUR0[USD]) - 1 = ($321.85 / 1.11$/€) / ($190.24 * 1.17$/€) - 1 = 0.7833 = 78.33% // EUR[USD] := how much 1 EUR costs in USD`
    > - _Return in % USD:_ `P1[USD] / P0[USD] = $321.85 / $190.24 - 1 = 0.6929 = 69.29%`
18. When does CPP hold?
    > _CPP := Commodity price parity holds in absence of trade barriers for homogeneous goods (e.g., gold, precious metals)_
19. Write down the formula for PPP in relative terms.
    > _PPP := Purchasing power parity ("Average price levels are the same in two countries at any time")_
    > - "Spot exchange rates between currencies adjust to inflation differentials between the respective countries"
    > - `= SUM(weightDomestic(t) * PriceDomestic(t)) = SpotExchangeRate(t) * SUM(weightForeign(t) * PriceForeign(t))`
20. Today 0.90 EUR buy 1 USD. Economists forecast 1.5% inflation in the Eurozone and 3.0% inflation in
the US over the next year. Predict the EUR/USD exchange rate at the end of next year assuming that
PPP holds.
    > - `r0[EUR/USD] = Foreign / Domestic = 1 / 0.90 = 1.1111`
    > - `r1[EUR/USD] = (Foreign * (1+inflationForeign)) / (Domestic * (1+inflationDomestic)) = (1 * 1.03) / (0.90 * 1.015) = 1.1275`

## Problems and questions 21-30 [20 min]
21. What is the implication of PPP for the returns on international assets for investors from different
countries?
    > _Real returns on international assets are identical for investors from different countries denominating returns in different currencies_
22. Why is PPP only a poor explanation of short-term exchange rate movements?
    > - Explains 5-10%
    > - Takes several years before a PPP deviation is adjusted for in the currency market, because:
    >     - _Inflation is not consistently defined across countries_
    >     - _Consumption baskets are different_
    >     - _Changes in relative prices cause consumption substitution_
    >     - _Transaction costs, taxes, and restrictions prevent arbitrage in goods markets_
23. Explain the concept of Economist’s Big Mac Index.
    > _Lighthearted guide to whether currencies are at their “correct” level. The local average price of a Big Mac in a country is always compared with the average price in the reference country USA._
24. In the US the average price of a Big Mac in January 2018 is 5.28 USD. At the same time in China it is
20.40 Yuan which is equivalent to 3.17 USD at market exchange rates, and in Switzerland it is 6.50
Swiss francs which is equal to 6.76 USD. Comment on the relative valuation of the three currencies in
accordance with the Big Mac index.
    > - _US:_ `5.28 USD` _ - _reference_
    > - _China:_ `20.40 Yuan = 3.17 USD` _- undervalued with exchange rate of 6.435 Yuan for one USD, should cost: 33.98 Yuan_
    > - _Switzerland:_ `6.50 CHF = 6.78 USD` _- overvalued with exchange rate of 0.959 CHF for one USD, should cost: 5.06352 CHF_
25. The spot exchange rate between two currencies is 0.80. The domestic interest rate is 1.5% and the
foreign interest rate is 3%. Calculate the forward exchange rate.
    > `S0 = 0.80, rD = 0.015, rF = 0.03 >>> F0 = ((1+rD)/(1+rF)) * St = (1.015/1.03) * 0.80 = 0.7883`
26. Explain the core problem of international asset pricing.
    > _“Investors hedge their consumption by their investment portfolio” meaning that investors in different countries have different expected returns for the same internationally
traded asset_
27. In a closed economy (domestic setting) efficient portfolio diversification brings all investors on the same
efficient frontier which is essential for the derivation of the CAPM. Explain why in the international setting
there exists no unique efficient frontier.
    > - _Foreign exchange rates, interest rates and inflation rates between countries_
    > - _PPP does not hold due to differences across countries concerning composition of national consumption baskets, relative prices of goods and time-evolution of relative prices_
    > - Investment opportunities differ across countries: Restrictions & Capital controls
28. On 20 April 2018 the price of an Apple stock is 172.80 USD and the price of one fresh white bread is
2.52 USD. One year before the stock price was 142.44 USD and the bread price was 2.40 USD.
Calculate the real return on Apple shares.
    > - `Real(APPL) = (172.80/2.52) / (142.44/2.40) - 1 = 0.1554 = 15.54%`
    > - `Nominal(APPL) = 172.80/142.44 - 1 = 0.2131 = 21.31%`
29. What additional assumptions have to be made in order to translate the base-line International CAPM in
real terms into a certain currency?
    > - _Existence of a risk-free asset denominated in the country‘s currency, having a zero world market beta_
    > - _Inflation rate in the country is uncorrelated with nominal returns (inflation risk is not systematic)_
30. Comment on critical assumptions and the practicability of the base-line ICAPM.
    > - _Critical assumption: Inflation rate changes do not systematically affect the cross-section of asset returns (aka assumes zero correlation between inflation and asset returns)_
    > - _Practicability: If the covariance between inflation rate changes and asset returns is small, formula can be used as an approximation_

## Problems and questions 31-40 [20 min]
31. Investors continuously face exchange risk due to unforeseen deviations from PPP. Explain the
implications for investors in different countries and for portfolio choice in the setting of IAPM’s.
    > - _Investors in different countries_
    >     - _are heterogenous regarding consumption and investment opportunities_
    >     - _evaluate real returns from the same internationally traded asset differently_
    >     - _face different settings for portfolio optimization_
    >     - _evaluate the cross-section of internationally traded assets differently_ 
32. What are the investment opportunities in the international asset pricing model of Solnik (1974)?
    > - _Domestic risk-free bond_
    > - _Domestic common stocks_
    > - _Foreign risk-free bonds_
    > - _Foreign common stocks_
33. Describe the portfolio components in the IAPM of Solnik (1974).
    > 1. _World market portfolio hedged against exchange rate risk (representing market risk)_
    > 2. _Portfolio of risk-free bonds of all countries (currency risk hedge fund)_
    > 3. _Risk-free bond of the home country_
34. What is the technical concept behind the world market portfolio hedged against exchange risk in the
IAPM of Solnik (1974)?
    > _Based on exchange rate expectations, international stock positions are hedged by going short in local risk-free bonds (zero-investment portfolio) eliminating the currency risk_
35. Explain the “separation idea” in the model of Solnik (1974).
    > _Market positions are hedged by going short in the currency position_
36. Describe the portfolio choice in the IAPM of Adler and Dumas.
    > 1. _Universal world market portfolio of risky assets (long risky assets)_
    > 2. _Individual inflation hedge portfolio: Individual weighting of assets such that the nominal return of the portfolio is most highly correlated with the inflation rate in the residence country of the investor (short assets correlated with interest rate)_
37. Explain the priced sources of risk in the Adler-Dumas model and the determinants of expected returns in
equilibrium.
    > - _Expected return of an asset depends on its usefulness to hedge PPP risk rather than on its
world market risk alone_
    > _In equilibrium, expected returns must be consistent with the assets‘ hedging potential in
each country as well as the investors‘ willingness to pay for hedging in each country_
38. Write down the asset pricing restriction of Adler and Dumas and explain its components.
    > `E(riDomestic) = rfDomestic + λWM * Cov(riDomestic,rwmDomestic) + SUM(λπj * Cov(riDomestic, πj)`
    > - _`ri` := Interest Rate_
    > - _`rf` := Risk-free Rate_
    > - _`λWM` := Premium for covariance with the world market (MRP)_
    > - _`πj` := Inflation Rate_
    > - _`λπj` := Premium for covariance with the jth country's inflation_
39. Explain the idea of rational asset pricing.
    > - _Asset prices react to economic news and a variety of unanticipated events influence asset prices and hence the co-movements of asset prices suggest the existence of common exogenous driving forces_
    > - _Asset prices depend on their exposures to (latent) state variables which can be modeled empirically using economic variables as proxies_
40. Explain the approach of Chen, Roll and Ross (1986) to capture systematic forces that influence asset
returns.
    > _Idea: Systematic forces that influence returns are those that change discount factors (`rf`) and expected cash flows (`E(C)`) in the dividend discount model `P=E(C)/rf`_
    > - a. _Industrial production: Monthly growth rate industrial production (MP), Yearly growth rate in industrial production (YP)_
    > - b. _Inflation: Unanticipated inflation (UI), Change in expected inflation (DEI)_
    > - c. _Risk premium: Unanticipated change in the risk premium (Baa and under return minus long-term government bond return) (UPR)_
    > - d. _Term structure: Unanticipated change in the term structure (long-term government bond return minus Treasury-bill rate) (UTS)_
    > - e. _Stock market: Return on the value-weighted NYSE index (VWNY), Return on the equally weighted NYSE index (EWNY)_
    > - f. _Innovation in real per capita consumption_
    > - g. _Oil price_

## Problems and questions 41-50 [xx min]
41. Name three macroeconomic state variables applied in the study of Chen, Roll and Ross (1986).
    > _a_
42. Explain the idea of arbitrage pricing in a large capital market.
    > _a_
43. What might disturb arbitrage pricing of assets in the international environment?
    > _a_
44. Describe the components of the return generating model in the International APT.
    > _a_
45. What are the three crucial conditions for arbitrage pricing to hold in an international setting?
    > _a_
46. What is the assumption on exchange rate changes in the IAPT of Solnik?
    > _a_
47. Write down the pricing restriction of Solnik’s IAPT and explain its components.
    > _a_
48. Multifactor models are used to explore the drivers of asset return volatility. Explain the empirical
approach.
    > _a_
49. Explain the difference between volatility drivers and value drivers in capital markets.
    > _a_
50. Explain the two hypothesis of the Wald test procedure discussed in the lecture to identify factors with a
systematic influence on asset returns and potentially also the cross-section of expected returns.
    > _a_

## Problems and questions 51-53 [xx min]
51. A factor model including four uncorrelated global factors is applied to analyze the systematic risk of
selected European stock markets. The results of the analysis are documented in the following table (one
value is missing).
    |                    |            | Factor 1                     | Factor 2 | Factor 3 | Factor 4 |
    |--------------------|------------|------------------------------|----------|----------|----------|
    | Factor volatility  |            | 10.0%                        | 15.0%    | 18.0%    | 16.0%    |
    |                    |            |                              |          |          |          |
    |                    | Volatility | Factor sensitivities (betas) |          |          |          |
    | Germany            | 25.0%      | 0.45                         | -0.25    | 0.15     | 1.20     |
    | UK                 | 16.0%      | 0.15                         | -0.15    | 0.12     | missing  |
    | France             | 19.0%      | 0.40                         | -0.30    | 0.10     | 0.80     |
  - What portion of the variance of the German stock market is captured by factor 1?
    > _a_
51. With reference to the table in question 51: What portion of the variance of the French stock market is
explained by the model?
    > _a_
52. With reference to the table in question 51: 72.25% of the variance of the UK stock market is explained by
factor 4. Calculate the missing value.
    > _a_

## Problems and questions 54-60 [xx min]
54. With reference to the table in question 51: Exposure to the four global risk factors is compensated in
long-term returns. In a cross-sectional analysis the following risk premiums are estimated: 1.5% for
factor 1, -2.5% for factor 2, 1% for factor 3, and 4% for factor 4. Calculate the expected return for the
German and the French stock market assuming a risk-free interest rate of 1%.
    > _a_
55. How do the changes in the slope of the term structure of interest rates correspond to market participants’
business cycle expectations?
    > _a_
56. Explain the concept of intertemporal consumption smoothing in the context of the yield curve.
    > _a_
57. Name the three explanatory variables in the study of Fama and French (1989, Business Conditions and
Expected Returns on Stocks and Bonds).
    > _a_
58. How do expected returns on capital markets relate to economic conditions? Explain the general
message of the study of Fama and French (1989).
    > _a_
59. What is the economic explanation of a time-varying drift in the random walk model? (Part 5, Slide 20)
    > _a_
60. Write down the regression equation of an instrumental forecasting model and explain its components.
    > _a_

## Problems and questions 61-70 [xx min]
61. The dividend discount model is often the starting point for the search of instrumental variables in a
forecasting model. Explain why.
    > _a_
62. Briefly explain the idea of conditional asset pricing.
    > _a_
63. There is a debate on the reason for predictability in asset returns. Briefly summarize the findings of the
study of Ferson and Harvey (1991, The variation of economic risk premium) concerning this debate.
    > _a_
64. Write down the cross-sectional pricing restriction of a conditional beta pricing model including a linear
model capturing the time-variation of risk premiums.
    > _a_
65. Complete the following statement: “Markets are integrated if…”
    > _a_
66. What does market integration imply for the sources of risk and their pricing on global capital markets?
    > _a_
67. How can market integration be measured? Explain indicative as well as theoretically correct measures of
market integration.
    > _a_
68. Explain asset allocation and portfolio choice of conservative and aggressive investors in the framework
of Markowitz (1952). Draw a graph if you like.
    > _a_
69. Briefly explain the “asset allocation puzzle”.
    > _a_
70. Explain the difference between strategic and tactical asset allocation.
    > _a_

## Problems and questions 71-80 [xx min]

71. Describe the 4 quadrants of the framework of Brinson, Hood and Beebower to analyze the determinants
of portfolio performance.
    > _a_
72. The benchmark of a fund features 30% invested in equity markets and 70% invested in fixed income
assets (policy weights). The actual weights imposed by the fund management over the last 12 months
were 40% equity and 60% fixed income. The passive equity return was 4.5% and the passive fixed
income return was 1.5%, while the active returns achieved by the fund management were 5% in equity
and 1.0% in fixed income. Evaluate the active competences of the fund management.
    > _a_
73. Briefly describe the steps of a strategic asset allocation.
    > _a_
74. Explain the difference between a risk-oriented and a market-oriented portfolio overlay.
    > _a_
75. Explain the difference between an asset class risk premium, a style risk premium and a strategy risk
premium.
    > _a_
76. There are different philosophies to invest in stocks. What are the differences between High-conviction
strategies and passive investing in equity?
    > _a_
77. Write down the Gordon growth model and explain its components.
    > _a_
78. Which model could be used to calculate the discount factor in the Gordon model?
    > _a_
79. For a stock, a next dividend of EUR 4.50 and a long-term constant dividend growth of 5% is expected.
What is the intrinsic value of the stock if a discount factor of 8% is applied?
    > _a_
80. With reference to question 79: The market price of the share is EUR 130. How do you rate this current
market price?
    > _a_

## Problems and questions 81-90 [xx min]
81. With reference to question 79: How does the intrinsic value of the stock change if the expected dividend
growth weakens to 4%?
    > _a_
82. With reference to question 79: What dividend growth is implied in a stock price of EUR 180? We still
assume that the next dividend will be EUR 4.50, discounted at 8%.
    > _a_
83. What assumption about information efficiency is contained in the statement: “A stock is undervalued.”
    > _a_
84. Which indicators are used to select value stocks? Name 3 fundamental indicators.
    > _a_
85. What is the value trap?
    > _a_
86. Explain the investment philosophy of Warren Buffett.
    > _a_
87. Write down the empirical version of the CAPM.
    > _a_
88. What is meant by the ’joint hypotheses problem’ in the context of the CAPM?
    > _a_
89. How does the CAPM perform in empirical tests?
    > _a_
90. Name the two theoretical anchor points of multi-factor models.
    > _a_

## Problems and questions 91-99 [xx min]

91. How are equity returns explained in the Fama-French 3-factor model?
    > _a_
92. How are the factors constructed in a multi-factor model?
    > _a_
93. How is the Fama-French 3-factor model related to the ICAPM of Merton? Refer to the role of state
variables.
    > _a_
94. How does Carhart (1997) complement the Fama-French 3 factor model?
    > _a_
95. In the current academic debate there is talk of a ‘factor zoo’. What is this discussion about?
    > _a_
96. Factor-based equity investments have become very popular. What are the risk premiums of factor-based
strategies based on?
    > _a_
97. Comment on the stability of returns of factor strategies in equity markets.
    > _a_
98. What is the idea behind ETFs and why do ETF investments have many advantages?
    > _a_
99. Explain the two methods how ETFs can replicate an index.
    > _a_

