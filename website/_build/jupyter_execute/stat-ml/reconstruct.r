library(faraway)  # For data, sumary(), and vif()
install.packages("corrplot")  # In case not found in conda env
library(corrplot)  # For corrplot()
library(ggplot2)  # Plot multiple ggplots in a grid.
library(gridExtra)  # Plot multiple ggplots in a grid.


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

  if (panels == 4) {
    options(
      repr.plot.width = 6,
      repr.plot.height = 4.5
    )
    par(
      mfrow = c(2, 2),
      mar = c(4, 3, 0, .1) + .2,
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


df <- globwarm[!is.na(globwarm$nhtemp), ]


set_pars(panels=2)
plot(globwarm$year, globwarm$wusa)
plot(globwarm$year, globwarm$mongolia)


options(repr.plot.width = 6, repr.plot.height = 6)
par(mfrow = c(3, 3), mar = c(2.5, 3, 0, .1) + .2, mgp = c(1.8, .8, 0), ps = 10)
summary_plot(df[, !(names(df) %in% 'year')])


set_pars(dim=c(5, 5))
correlations <- cor(df[, !(names(df) %in% 'year')], method = 'spearman')
corrplot(correlations)


set_pars(panels=2)
plot1 <- ggplot(df) + geom_point(aes(jasper, urals, alpha = year)) +
  ggtitle(paste('corr =', round(correlations['jasper', 'urals'], 2)))
plot2 <- ggplot(df) + geom_point(aes(mongolia, tasman, alpha = year)) +
  ggtitle(paste('corr =', round(correlations['mongolia', 'tasman'], 2)))
grid.arrange(plot1, plot2, ncol = 2)


set_pars(panels=2)
plot1 <- ggplot(df) + geom_point(aes(tornetrask, nhtemp, alpha = year)) +
  ggtitle(paste('corr =', round(correlations['tornetrask', 'nhtemp'], 2)))
plot2 <- ggplot(df) + geom_point(aes(mongolia, nhtemp, alpha = year)) +
  ggtitle(paste('corr =', round(correlations['mongolia', 'nhtemp'], 2)))
grid.arrange(plot1, plot2, ncol = 2)


n <- nrow(df)
test <- df[1:floor(n*.3), ]
train <- df[(floor(n*.3)+1):n, ]
lmod <- lm(nhtemp ~ . - year, train)
sumary(lmod)


set_pars(panels=4)
plot(lmod)


tresid <- rstudent(lmod)
which(abs(tresid) > abs(qt(.05/n, lmod$df.residual - 1)))


set_pars(panels=2)
plot(train$year, lmod$residuals)
plot(lmod$residuals[1:(nrow(train)-1)], lmod$residuals[2:nrow(train)])


library(nlme)
glmod <- gls(nhtemp ~ . - year, correlation = corAR1(form = ~ year), train)
summary(glmod$modelStruct)


summary(glmod)$tTable


Sigma <- corMatrix(glmod$modelStruct$corStruct)
S <- t(chol(Sigma))
y <- solve(S) %*% train$nhtemp  # y'
X <- solve(S) %*% model.matrix(nhtemp ~ . - year, train)  # X'
rownames(y) <- rownames(X) <- rownames(train)
glmod <- lm(y ~ X + 0)
sumary(glmod)


set_pars(panels=4)
plot(glmod)


set_pars(panels=2)
plot(train$year, glmod$residuals)
plot(glmod$residuals[1:(nrow(train)-1)], glmod$residuals[2:nrow(train)])


set_pars(panels=4)
wts <- 1/(as.integer(rownames(X)) - min(as.integer(rownames(X))) + 1)**.5
wglmod <- lm(y ~ X + 0, weights = wts)
plot(wglmod)


get_rmse <- function(ypred, yobs) {
  sqrt(mean((ypred - yobs)**2))
}


X_test <- model.matrix(nhtemp ~ . - year, test)
get_rmse(X_test %*% coef(lmod), test$nhtemp)


get_rmse(X_test %*% coef(glmod), test$nhtemp)


get_rmse(X_test %*% coef(wglmod), test$nhtemp)


install.packages('glmnet')
library(glmnet)

set.seed(1)  # For reproducibility (from cross-validation).
ridge_lmod <- cv.glmnet(
  x = as.matrix(train[, !(names(train) %in% c('nhtemp', 'year'))]),
  y = train$nhtemp, alpha = 0, intercept = TRUE
)
get_rmse(X_test %*% coef(ridge_lmod), test$nhtemp)


ridge_glmod <- cv.glmnet(
  X, y, alpha = 0, intercept = FALSE, penalty.factor = c(0, rep(1, ncol(X)-1))
)
get_rmse(X_test %*% coef(ridge_glmod)[2:(ncol(X)+1)], test$nhtemp)


ridge_wglmod <- cv.glmnet(
  X, y, alpha = 0, intercept = FALSE, penalty.factor = c(0, rep(1, ncol(X)-1)),
  weights = wts
)
get_rmse(X_test %*% coef(ridge_wglmod)[2:(ncol(X)+1)], test$nhtemp)


ridge_lmod <- cv.glmnet(
  x = as.matrix(df[, !(names(df) %in% c('nhtemp', 'year'))]),
  y = df$nhtemp, alpha = 0, intercept = TRUE
)

glmod <- gls(nhtemp ~ . - year, correlation = corAR1(form = ~ year), df)


ridge_lmod_pred <- predict(
  ridge_lmod,
  newx = as.matrix(globwarm[, !(names(globwarm) %in% c('nhtemp', 'year'))])
)
glmod_pred <- predict(glmod, globwarm[, !(names(globwarm) %in% c('nhtemp'))])


set_pars(panels=1)
plot(df$year, df$nhtemp)
lines(globwarm$year, ridge_lmod_pred, col = 2)
lines(globwarm$year, glmod_pred, col = 3, lty = 1)
legend('topleft', legend = c('ridge', 'GLS'), lty = 1, col = 2:3)


set_pars(dim=c(8, 3))
plot(globwarm$year, globwarm$nhtemp)
lines(globwarm$year, ridge_lmod_pred, col = 2)
lines(globwarm$year, glmod_pred, col = 3)
legend('topleft', legend = c('ridge', 'GLS'), lty = 1, col = 2:3)
