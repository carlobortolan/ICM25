# Formula Sheet

## Simple return
    (P1-P0)/P0

## Cont. comp. return
    ln(P1/P0) = 0.317

## Volatility of an index
    Yearly volatility = monthly volatility * sqrt(12 months) = 0.2112
    Monthly volatility = daily volatility * sqrt(22 days)_ = 0.0610
    Daily volatility = 0.0130

## Volatility of a portfolio with two positions
    sqrt( σ(A)² * a² + σ(B)² * b² + 2*a*b*Cov(A,B) )
  
    = sqrt( σ(A)² * a² + σ(B)² * b² + 2*a*b*σ(A)*σ(B)*Corr(A,B) )

## Stock return over a person given an exchange rate
    Return in % EUR: (P1[USD] / EUR1[USD]) / (P0[USD] / EUR0[USD]) - 1 // EUR[USD] := how much 1 EUR costs in USD //= real return

    Return in % USD: P1[USD] / P0[USD] //= nominal return

## Predict exchange rate if PPP holds
    r0[EUR/USD] = Foreign / Domestic
    
    r1[EUR/USD] = (Foreign * (1+inflationForeign)) / (Domestic * (1+inflationDomestic))

## Forward exchange rate
    F0 = ((1+rD)/(1+rF)) * St

## Factor model

### Reaction of X to a % increase in Factor Y
    ReactionX  := Factor Exposure * Increase

### Portion of variance captured by factor
    ((Factor Exposure or Sensitivity)² * (Factor Volatility)² + ...) / (Market aka Country Volatility)²

### Expected return for stock market(s) assuming a risk-free interest rate and given risk premiums
    R = rf + SUM(factor exposure * risk premium)

## Intrinsic value / DDM
    V = Dividend / (rf - g)

## Evaluation of active competences of fund management using BHB model
    Passive Timing & Passive Selection: wE(benchmark) * rE(passive) + wFI(benchmark) * rFI(passive)
    
    Actual Timing & Passive Selection: wE(selection) * rE(passive) + wFI(selection) * rFI(passive)
    
    Passive Timing & Actual Selection: wE(benchmark) * rE(active) + wFI(benchmark) * rFI(active)
    
    Actual Timing & Actual Selection: wE(selection) * rE(active) + wFI(selection) * rFI(active)
    
    => Timing contributes: actual timing - passive timing
    => Selection contributes: active selection - passive selection
