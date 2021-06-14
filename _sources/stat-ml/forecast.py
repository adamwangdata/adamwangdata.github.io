# ---
# jupyter:
#     jupytext:
#         text_representation:
#             extension: .py
#             format_name: percent
#     kernelspec:
#         language: python
#         name: python3
#         display_name: Python 3.7.6
# ---




#%% [markdown] Macros Setup tags=['remove-cell']
# $$
# \newcommand{\parens}[1]{\mathopen{}\left(#1\right)\mathclose{}}
# \newcommand{\bracks}[1]{\mathopen{}\left[#1\right]\mathclose{}}
# \newcommand{\braces}[1]{\mathopen{}\left\{#1\right\}\mathclose{}}
# \newcommand{\abs}[1]{\mathopen{}\left\lvert#1\right\rvert\mathclose{}}
# \newcommand{\norm}[1]{\mathopen{}\left\lVert#1\right\rVert\mathclose{}}
# \renewcommand{\vec}[1]{\boldsymbol{\mathbf{#1}}}
# \newcommand{\mat}[1]{\mathbf{#1}}
# \newcommand{\tpose}[1]{#1^T}
# \newcommand{\inv}[1]{#1^{-1}}
# \newcommand{\Matrix}[1]{
#   \begin{bmatrix}
#     #1
#   \end{bmatrix}
# }
# \newcommand{\seq}[1]{1, 2, \ldots, #1}
# \newcommand{\reals}{\mathbb{R}}
# \newcommand{\mper}{\,\text{.}}
# \newcommand{\mcom}{\,\text{,}}
# $$

#%% [markdown]

"""
(time-series)=
# Time Series Forecasting

## Summary

Using all recorded annual temperatures averages (from 1850 to 2020), I use [Prophet](https://facebook.github.io/prophet/) to forecast annual temperatures up until 2050.
This results in the following projection:

```{image} ./forecast.png
:align: center
```

```{note}
You can run and modify the code on this page Jupyter Notebook style, but without leaving the page!
Hover over the {fa}`rocket` launch button at the top of the page, then click the {guilabel}`Live Code` button.
Once you see "Launching from mybinder.org: ready", you can run code cells.
Refresh the page to revert to the original view.
```

## Data Source

Average northern hemisphere temperature data was obtained from [https://www.metoffice.gov.uk/hadobs/hadcrut5/](https://www.metoffice.gov.uk/hadobs/hadcrut5/), specifically the "HadCRUT5 analysis time series: ensemble means and uncertainties".
The temperatures are expressed as deviations, or anomalies, from reference temperatures over the period of 1961--1990; for details [see here](https://crudata.uea.ac.uk/cru/data/temperature/#faq5).
Each anomaly is a best estimate calculated from an ensemble of 100 time series, hence confidence intervals are present in the dataset.
For the purposes of this analysis, I will just use the point estimate.

(data-exploration)=
## Data Exploration

Let's load in the data and examine it:
"""

#%%

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./globwarm.csv')
df.head(3)

#%%

df.tail(3)

#%% [markdown]

"""
Since 2021 data collection is still ongoing, the confidence limits are much wider.
For simplicity, I'll drop this point from the analysis.
"""

#%%

df = df[df.Time <= 2020]

#%% [markdown]

"""
Next, let's plot the data:
"""

#%%

fig, ax = plt.subplots()
ax.plot(df.Time, df["Anomaly (deg C)"], 'o')
ax.set(xlabel='Year', ylabel='Temperature (C)')
plt.show()

#%% [markdown]

"""
There is clearly a nonlinear trend amidst the random variation from year to year.
We expect some long term cyclical patterns, for instance [Milankovitch cycles](https://en.wikipedia.org/wiki/Milankovitch_cycles) due to variations in Earth's movement relative to the Sun.
However, these patterns are difficult to extract because we have just under 200 years of data to work with.
These cyclical patterns are very important, however, because we don't have access to more granular data with daily, weekly, and/or yearly variation typically present in business problems.
For this reason, [Prophet](https://facebook.github.io/prophet/) is useful as it can easily implement custom seasonalities.
It's also flexible in its ability to detect changepoints, another crucial parameter affecting model fit as we will see in § [](optimize-forecast)

## Building a Simple Forecast

First, we must format the data appropriately.
Prophet expects a two column dataframe with datestamps `ds` formatted like `YYYY-MM-DD` and numeric data `y`.
"""

#%%

def format_years(years):
    """Convert numeric years to YYYY-MM-DD format, using an arbitrary day."""
    ds = [str(year) + "-12-31" for year in years]
    return ds

df = (
    df[["Time", "Anomaly (deg C)"]]
    .rename(columns={"Time": "ds", "Anomaly (deg C)": "y"})
)
df.ds = format_years(df.ds)
df.head(3)

#%%

df.tail(3)

#%% [markdown]

"""
`df` is now ready for Prophet modeling, but as hinted in § [](data-exploration), a model built from defaults performs poorly:
```{margin}
The INFO messages tell us weekly and daily seasonalities are disabled (by default) as they should be, because our data resolution is on much longer timescales.
```
"""

#%%

from prophet import Prophet

def plot_model_fit(model, df):
    """Fit and plot predictions of a Prophet() model on the training data."""
    model.fit(df)
    predictions = model.predict()
    model.plot(predictions, xlabel='Year', ylabel='Temperature (C)')

model = Prophet()
plot_model_fit(model, df)

#%% [markdown]

"""
The reason is that we need to account for long term cycles over many years.
A yearly seasonality is meaningless in this context, because we don't have sub-year level data.
Let's try again, disabling the usual seasonalities and implementing our own using the `add_seasonality()` method.
From the scatterplot of the raw data, any noticeable variation occurs after at least 50 years.
At the 50 year scale, the variation is relatively small, so we shouldn't make the fit too flexible.
In Prophet's language, we shouldn't include too many Fourier terms, controlled by the `fourier_order` parameter.
"""
#%%

model = Prophet(
    daily_seasonality = False,
    weekly_seasonality = False,
    yearly_seasonality = False,
)
model.add_seasonality('50 years', period=365*50, fourier_order=2)
plot_model_fit(model, df)


#%% [markdown]

"""
The fit's a bit better in terms of smoothness, but still not great.
Increasing `fourier_order` just amounts to more more variation around a similar mean trend line.
Let's try increasing the seasonality period a bit more:
"""

#%%

model = Prophet(
    daily_seasonality = False,
    weekly_seasonality = False,
    yearly_seasonality = False,
)
model.add_seasonality('centuryly', period=365*100, fourier_order=2)
plot_model_fit(model, df)

#%% [markdown]

"""
The fit is much better.
Let's see what it forecasts.
"""

#%%

future = model.make_future_dataframe(periods=30, freq='Y')
forecast = model.predict(future)
model.plot(forecast, xlabel='Year', ylabel='Temperature (C)')
plt.show()

#%% [markdown]

"""
The model stays roughly linear with the latest data, but levels off due to the seasonality built into the model.

(optimize-forecast)=
## Optimizing the Forecast

The previous hand-tuning was insightful, but largely experimental.
A more principled approach tunes the parameters based on some performance metric(s).
Cross-validation is often used for this, but we have to be careful with time series data due to correlations between data points.
One approach preserves the ordering of time by training on the first (say) 100 years of data and testing on the next 20 years of data.
Then we train on the first 110 years of data and test on the next 20 years of data.
We repeat this until we reach the end of the data.
Each batch gives us an estimate of errors of predictions made 1, 2, ..., 20 years in the future while preserving the ordering of time.
This approach can be implemented in Prophet as follows:
"""

#%%

from prophet.diagnostics import cross_validation

df_cv = cross_validation(model, initial='36500 days', horizon='7300 days')
df_cv.head(3)

#%%

df_cv.tail(3)

#%% [markdown]

"""
For example, we see the the first `cutoff` point is in 1951.
The model is trained on data up until the cutoff, then predictions (`yhat`) are made for the next 20 years.
The cutoff points are then incremented by 10 years until 2001.
I'll measure model performance using mean squared error (MSE), but a variety of metrics could be used.
We can plot MSE as a function of horizon length (how far in time the prediction is made) using `plot_cross_validation_metric()`;
unsurprisingly, performance is worse the farther out the window:
"""

#%%

from prophet.plot import plot_cross_validation_metric

fig, ax = plt.subplots(figsize=(10, 6))
plot_cross_validation_metric(df_cv, metric='mse', rolling_window=.1,
                             ax=ax, color='C0')
plot_cross_validation_metric(df_cv, metric='mse', rolling_window=.5,
                             ax=ax, color='C1')
plt.show()

#%% [markdown]

"""
The two curves differ by the amount of averaging used in computing the MSE.
Each point in the blue curved is averaged over 10% of the data while each point in the orange curve is averaged over 50% of the data.
The blue curve is more variable but can give estimates over shorter horizons.
Setting `rolling_window=1` averages over all the data, giving just a single average estimate for the MSE of predictions within a 20 year horizon.
A dataframe of metrics can be extracted with `performance_metrics()`:
"""

#%%

from prophet.diagnostics import performance_metrics

df_performance = performance_metrics(df_cv, rolling_window=1)
df_performance

#%% [markdown]

# The above code with `rolling_window=1` is useful for hyperparameter tuning.
# It allows us to optimize average performance over a fixed horizon window.
# This is done in the code below to find the optimum seasonality period and number of Fourier terms.
# I also optimize over two model parameters `changepoint_prior_scale` and `seasonality_prior_scale` which control the flexibility of the changepoints and seasonalities.
# ```{margin}
# This cell takes a while to run so is not executable, but later cells that analyze `tuning_results.csv` are executable.
# ```
# ```python
# import itertools
#
# def make_grid_combinations(grid):
#     """Turn a dictionary of grid points into a dictionary of all combinations
#     of those grid points."""
#     all_params = []
#     for vals in itertools.product(*grid.values()):
#         all_params.append(dict(zip(grid.keys(), vals)))
#     return all_params
#
# param_grid = {
#     'period': [50, 75, 100],
#     'fourier_order': [2, 4, 6],
#     'changepoint_prior_scale': [.005, .05, .5],
#     'seasonality_prior_scale': [.1, 1, 10],
# }
# all_params = make_grid_combinations(param_grid)
# mses = []
#
# # Cross-validate each combination of grid parameters to estimate MSEs
# for params in all_params:
#     model = Prophet(
#         daily_seasonality = False,
#         weekly_seasonality = False,
#         yearly_seasonality = False,
#         changepoint_prior_scale = params['changepoint_prior_scale'],
#         seasonality_prior_scale = params['seasonality_prior_scale']
#     )
#     model.add_seasonality(
#         name = str(params['period']) + ' year',
#         period = 365 * params['period'],
#         fourier_order = params['fourier_order']
#     )
#     model.fit(df)
#
#     df_cv = cross_validation(model, initial='36500 days', horizon='7300 days')
#     df_performance = performance_metrics(df_cv, rolling_window=1)
#     mses.append(df_performance['mse'].values[0])
#
# tuning_results = pd.DataFrame(all_params)
# tuning_results['mse'] = mses
# tuning_results.to_csv('tuning_results.csv', index=False)
# ```

#%% [markdown]

"""
The result is stored in a dataframe of cross-validated MSEs and the parameters used in the model:
"""

#%%

tuning_results = pd.read_csv('./tuning_results.csv')
tuning_results

#%% [markdown]

"""
The best parameters, measured by MSE, are easily obtained:
"""

#%%
import numpy as np

best_params = tuning_results.iloc[np.argmin(tuning_results['mse']), :]
best_params

#%% [markdown]

"""
Let's see what the optimized model looks like:
"""

#%%

model = Prophet(
    daily_seasonality = False,
    weekly_seasonality = False,
    yearly_seasonality = False,
    changepoint_prior_scale = .5,
    seasonality_prior_scale = 10.0
)
model.add_seasonality('centuryly', period = 365*75, fourier_order = 2)
model.fit(df)
future = model.make_future_dataframe(periods=30, freq='Y')
forecast = model.predict(future)
model.plot(forecast, xlabel='Year', ylabel='Temperature (C)')
plt.show()

#%% [markdown]

"""
## Conclusion

Using Prophet, I modeled atypical seasonal variations estimated from the data itself with the help of cross-validation.
Optimizing over other flexibility tuning parameters yields the above forecast.
Though the projection is made over 30 years, we are most confident in its ability over the next 20 years due to the 20 year horizon used when cross-validating.
The procedure to generate time series forecasts is extendable to other domains, for instance sales data.
It can be easily automated to incorporate the latest data to provide the most up-to-date forecasts.
"""