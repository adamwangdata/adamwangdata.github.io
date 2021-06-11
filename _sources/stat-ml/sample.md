(data-analysis)=
# Sample Data Analysis

**Predicting unrecorded temperatures before 1850 via proxy measurements.**
This analysis was inspired by the following exercise from Julian Faraway's book, *Linear Models with R* (2014):

> Reliable records of temperature taken using thermometers are only available back
to the 1850s, but it would be interesting to estimate global temperatures in the
pre-industrial era. It is possible to obtain various *proxy* measures of temperature.
Trees grow faster in warmer years so the width of tree rings (seen in tree cross-sections) provides some evidence of past temperatures. Other natural sources of
proxies include coral and ice cores. Such information can go back for a thousand years or more. The dataset `globwarm` contains information on eight proxy
measures and northern hemisphere temperatures back to 1856. Build a model and
predict temperatures back to 1000 AD. State the uncertainty in your predictions.
Comment on your findings.

The data was already cleaned, so my analysis begins from examination of the data.

```{raw} html
:file: globwarm.html
```
