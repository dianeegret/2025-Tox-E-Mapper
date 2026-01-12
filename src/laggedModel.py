import sqlite3

import pandas as pd

from app.util import retrieve_df

if __name__ == "__main__":
    df = retrieve_df()

    # Make connection to the tri data DB
    connection = sqlite3.connect('tri.db')
    fugitive = pd.pivot_table(df, values='fugitive_air',
                              index=['chem_id', 'facility_id', 'primary_sic', 'primary_naics'], columns=['year'], fill_value=0)
    fugitive.to_sql('fugitive_by_year', connection, if_exists='replace')
    print("Created fugitive air table")
    stack = pd.pivot_table(df, values='stack_air', index=['chem_id', 'facility_id', 'primary_sic', 'primary_naics'],
                           columns=['year'], fill_value=0)
    stack.to_sql('stack_by_year', connection, if_exists='replace')
    print("Created stack air table")
    waste = pd.pivot_table(df, values='prod_waste', index=['chem_id', 'facility_id', 'primary_sic', 'primary_naics'],
                           columns=['year'], fill_value=0)
    waste.to_sql('waste_by_year', connection, if_exists='replace')
    print("Created prod waste table")
    release = pd.pivot_table(df, values='single_release',
                             index=['chem_id', 'facility_id', 'primary_sic', 'primary_naics'],
                             columns=['year'], fill_value=0)
    release.to_sql('release_by_year', connection, if_exists='replace')
    print("Created single release table")
    ratio = pd.pivot_table(df, values='prod_ratio',
                           index=['chem_id', 'facility_id', 'primary_sic', 'primary_naics'],
                           columns=['year'], fill_value=0)
    ratio.to_sql('ratio_by_year', connection, if_exists='replace')
    print("Created prod ratio table")
