



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
#
# (reconstruct)=
# # Time Series Reconstruction
#
# ## Summary
#
# TODO...
#
# ## Data Source
#
# TODO...
#
# ## Preliminaries
#
# First, a few package imports:

#%%

library(faraway)  # For data, sumary(), and vif()
library(corrplot)  # For corrplot()

#%% [markdown]
#
# Next, a few functions that will be frequently used.
# I prefer graphical summaries of a data frame over numerical summaries provided by summary().
# `summary_plot()` a dataframe and plots each predictor: barplots for categorical data and histograms for continuous data;
# `cond_num()` computes condition numbers from a model object;
# finally, `set_pars()` sets default figure parameters that work well in a notebook setting.

#%% tags = ["hide-input"]

summary_plot <- function(df) {
  for (var in names(df)) {
    data <- df[[var]]
    if (is.factor(data)) {
      plot(data, xlab = var)
    } else {
      hist(data, main = '', xlab = var)
    }
  }
}

cond_num <- function(lmod) {
  X <- model.matrix(lmod)[, -1]
  e <- eigen(t(X) %*% X)
  return(sqrt(e$values[1] / e$values))
}

library(repr)

#' Specify figure parameters
#'
#' Call this function before plots to set the figure dimensions and par()
#' options (if applicable). Defaults are defined for 1- and 2- panel figures;
#' for more complex figures, you should call repr and par() instead.
#' Optionally customize the figure dimensions in a two-element vector
#' `dim`, assumed to be a c(width, height) pair in inches.
set_pars <- function(panels=1, dim=NULL) {
  if (panels == 1) {
    options(
      repr.plot.width = 3.25,
      repr.plot.height = 2.25
    )
    par(
      mar = c(2.5, 3, 0, .1) + .2,
      mgp = c(1.8, .8, 0),
      ps = 10,
      cex = 1,
      cex.lab = 1.05
    )
  }

  if (panels == 2) {
    options(
      repr.plot.width = 6,
      repr.plot.height = 2.25
    )
    par(
      mfrow = c(1, 2),
      mar = c(2.5, 3, 0, .1) + .2,
      mgp = c(1.8, .8, 0),
      ps = 10,
      cex = 1,
      cex.lab = 1.05
    )
  }

  if (!is.null(dim)) {
    options(
      repr.plot.width = dim[1],
      repr.plot.height = dim[2]
    )
  }

}

#%% [markdown]
#
# (data-exploration)=
## Data Exploration

#%%

set_pars(panels=2)
plot(globwarm$year, globwarm$wusa)
plot(globwarm$year, globwarm$mongolia)
