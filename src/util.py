import pandas as pd
import sqlite3
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt


def retrieve_df():
    # Make connection to the tri data DB
    connection = sqlite3.connect('tri.db')

    df = pd.read_sql_query("SELECT * FROM measurement", connection)
    df = df.replace('', np.nan)
    df = df.fillna(value={'fugitive_air': 0, 'stack_air': 0, 'prod_waste': 0,
                          'single_release': 0, 'prod_ratio': 0, 'year': 0})
    df.astype(dtype={
        'chem_id': 'category', 'facility_id': 'category', 'fugitive_air': np.longdouble, 'stack_air': np.longdouble,
        'prod_waste': np.longdouble,
        'single_release': np.longdouble, 'prod_ratio': np.longdouble, 'year': int, 'primary_sic': 'category',
        'primary_naics': 'category'
    })
    print("Retrieved SQL data")
    facilities = df.groupby('facility_id')['year'].nunique()
    facilities = facilities.loc[facilities >= 30]
    print(f"Facilities: {facilities.size}")
    return df[df['facility_id'].isin(facilities.index.array)]


def generate_lagged(df):
    df = df.set_index(pd.PeriodIndex(df['year'], freq='Y'))
    df = df.drop('year', axis=1)

    df = pd.pivot_table(df, values='prod_waste',
                        index=['chem_id', 'facility_id'],
                        columns=['year'], fill_value=0)
    df = df[~(df == 0).all(axis=1)]
    return df


def generate_xy(df, years=5):
    x = df.iloc[:, :-years]
    y = df.iloc[:, -years:]
    return x, y


def plot_learning_curve(model, x, y, score, run):
    print(f"Generating learning curve for score {score} run {run}")
    train_sizes, train_scores, validation_scores = learning_curve(
        estimator=model,
        X=x,
        y=y, cv=5, shuffle=True, random_state=6242, scoring=score, n_jobs=-1)
    train_scores_mean = train_scores.mean(axis=1)
    validation_scores_mean = validation_scores.mean(axis=1)

    plt.style.use('seaborn')
    plt.plot(train_sizes, train_scores_mean, label=f'Training', marker='o')
    plt.plot(train_sizes, validation_scores_mean, label=f'Validation', marker='o')
    plt.ylabel(score, fontsize=14)
    plt.xlabel('Training Set Size', fontsize=14)
    plt.title(f'Learning curve for {score} predicting 1 year', fontsize=18, y=1.03)
    plt.ylim(-1, 0)
    plt.margins(0.05)
    plt.legend()
    plt.savefig(f"../outputs/hgbr/{score}/learning_curve_a_{run}.png")
    plt.clf()

    plt.style.use('seaborn')
    plt.plot(train_sizes, train_scores_mean, label=f'Training', marker='o')
    plt.plot(train_sizes, validation_scores_mean, label=f'Validation', marker='o')
    plt.ylabel('Mean Absolute Percentage Error', fontsize=14)
    plt.xlabel('Training Set Size', fontsize=14)
    plt.title(f'Learning curve for {score} predicting 1 year', fontsize=18, y=1.03)
    plt.margins(0.05)
    plt.legend()
    plt.savefig(f"../outputs/hgbr/{score}/learning_curve_1_b_{run}.png")
    plt.clf()
