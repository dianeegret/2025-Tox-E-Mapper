from sklearn.metrics import mean_absolute_percentage_error, mean_absolute_error, mean_squared_error, \
    root_mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import HistGradientBoostingRegressor
import numpy as np
from app.util import retrieve_df, generate_lagged, plot_learning_curve


def generate_model(df, run):
    print(f"Generating model for {run}")
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1:]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )
    scores = ['neg_mean_absolute_percentage_error', 'neg_mean_squared_error', 'neg_root_mean_squared_error',
              'neg_mean_absolute_error']
    for score in scores:
        print(f"Running {score}")
        best = grid_search(X_train, y_train.values.ravel(), score, run)

        plot_learning_curve(best, X_train, y_train.values.ravel(), score, run)
        best.fit(X_train, y_train.values.ravel())

        y_pred = best.predict(X_test)
        mape = mean_absolute_percentage_error(y_test, y_pred)
        print(f"Run #{run} MAPE is {mape}")

        mae = mean_absolute_error(y_test, y_pred)
        print(f"Run #{run} MAE is {mae}")

        mse = mean_squared_error(y_test, y_pred)
        print(f"Run #{run} MSE is {mse}")

        rmse = root_mean_squared_error(y_test, y_pred)
        print(f"Run #{run} MAE is {rmse}")

        print(f"Running model for predicting for the next year")
        next_year = best.predict(df.iloc[:, 1:])

        f = open(f"../outputs/hgbr/output_run_{run}.txt", "a")
        f.write(f"Ran grid search with scoring function {score}")
        f.write(str(f"MAPE is {mape}\n"))
        f.write(str(f"MAE is {mae}\n"))
        f.write(str(f"MSE is {mse}\n"))
        f.write(str(f"RMSE is {rmse}\n"))
        f.write(str(f"Next year's prediction contains all 0s?  {not np.any(next_year)}\n"))
        f.close()


def grid_search(x, y, score, run):
    mod = HistGradientBoostingRegressor()
    param_grid = {
        'learning_rate': np.arange(0.1, 1, 0.3),
        'max_leaf_nodes': np.arange(5, 100, 15),
        'l2_regularization': np.arange(0, 5, 1),
        'loss': ['squared_error', 'absolute_error', 'poisson', 'quantile'],
    }
    print(f"Starting GridSearch for {score}\n")
    grid = GridSearchCV(mod, param_grid, n_jobs=-1, cv=5, scoring=score)
    grid.fit(x, y)
    print("Best parameters: ", grid.best_params_)
    f = open(f"../outputs/hgbr/output_run_{run}.txt", "a")
    f.write(f"Scoring function: {score} \n")
    f.write("Best parameters: " + str(grid.best_params_) + "\n")
    f.close()
    return grid.best_estimator_


if __name__ == "__main__":
    data = retrieve_df()
    max_year = np.max(data['year'])
    data = generate_lagged(data)
    for r in np.arange(1, 4):
        generate_model(data, r)
