import os
import pandas as pd
import sqlite3
import numpy as np
from pandas import DataFrame

columnsToDrop = ['frs id', 'horizontal datum', 'sic 2', 'doc_ctrl_num', 'elemental metal included',
                 'pbt', 'pfas', 'form type', '8.5 - recycling off sit', '8.6 - treatment on site',
                 '8.7 - treatment off site']
facilityCols = ['trifd', 'facility name', 'street address', 'city', 'county', 'st', 'zip', 'latitude', 'longitude',
                'parent co db num', 'parent co name', 'standard parent co name', 'federal facility',
                'industry sector code',  'year']
chemCols = ['chemical', 'tri chemical/compound id', 'cas#', 'srs id', 'clean air act chemical', 'classification',
            'metal', 'metal category', 'carcinogen', 'unit of measure', 'year']
measureCols = ['trifd', 'tri chemical/compound id', '5.1 - fugitive air', '5.2 - stack air', '8.8 - one-time release',
               '8.9 - production ratio', 'production wste (8.1-8.7)','year', 'primary sic',
                'primary naics']
dtypes = {'year': int,
          'trifd': 'string',
          'frs id': 'string',
          'facility name': 'string',
          'street address': 'string',
          'city': 'string',
          'county': 'string',
          'st': 'string',
          'zip': 'string',
          'latitude': float,
          'longitude': float,
          'horizontal datum': 'string',
          'parent co name': 'string',
          'parent co db num': 'string',
          'standard parent co name': 'string',
          'federal facility': 'string',
          'industry sector code': 'string',
          'industry sector': 'string',
          'primary sic': 'string',
          'sic 2': 'string',
          'primary naics': 'string',
          'doc_ctrl_num': 'string',
          'chemical': 'string',
          'elemental metal included': 'string',
          'tri chemical/compound id': 'string',
          'cas#': 'string',
          'srs id': 'string',
          'clean air act chemical': 'string',
          'classification': 'string',
          'metal': 'string',
          'metal category': 'string',
          'carcinogen': 'string',
          'pbt': 'string',
          'pfas': 'string',
          'form type': 'string',
          'unit of measure': 'string',
          '5.1 - fugitive air': float,
          '5.2 - stack air': float,
          '8.5 - recycling off sit': float,
          '8.6 - treatment on site': float,
          '8.7 - treatment off site': float,
          'production wste (8.1-8.7)': float,
          '8.8 - one-time release': float,
          '8.9 - production ratio': float}


'''
Create 4 distinct tables to avoid storing duplicate data'''
def create_schema(cur):
    # Unique industries (31)
    cur.execute(
        "CREATE TABLE IF NOT EXISTS industry(id varchar(4) PRIMARY KEY, name varchar(120), source_year integer)")

    # Unique facilities determined by TRIF ID and latitude/longitude (63413)
    cur.execute(
        "CREATE TABLE IF NOT EXISTS facility(id VARCHAR(15) PRIMARY KEY , name VARCHAR(62), address VARCHAR(62), "
        "city VARCHAR(28), "
        "county VARCHAR(50), state VARCHAR(2), zip VARCHAR(9), latitude INTEGER, longitude INTEGER, "
        "federal varchar(3), industry_id VARCHAR(4),  "
        "source_year integer, parent_co_id varchar, parent_name varchar(60), parent_standard_name varchar,"
        "foreign key (industry_id) references industry(id))")

    # Unique chemicals by ID (676)
    cur.execute("CREATE TABLE IF NOT EXISTS chemical(id varchar(10) primary key, name varchar(70), "
                "cas_num varchar(12), srs_id varchar(9), caa_chem varchar(3), classification varchar(6), "
                "metal varchar(3), metal_category varchar, carcinogen varchar(6), unit varchar(6), "
                "source_year integer)")

    # All measurements (2979617)
    cur.execute("CREATE TABLE IF NOT EXISTS measurement(chem_id varchar(10), facility_id varchar(15),"
                " fugitive_air real, stack_air real, prod_waste real, "
                "single_release real, prod_ratio real, year integer,primary_sic VARCHAR(4), primary_naics VARCHAR(6),"
                "FOREIGN KEY (facility_id) references facility(id), "
                "foreign key (chem_id) references chemical(id))")


def populate_data(con, cur):
    df = get_data()

    industries = df[['industry sector code', 'industry sector', 'year']]
    insert_industries(con, cur, industries)

    facilities = df[facilityCols]
    insert_facilities(con, cur, facilities)

    chemicals = df[chemCols]
    insert_chemicals(con, cur, chemicals)

    measurements = df[measureCols]
    insert_measurements(con, cur, measurements)


def get_data():
    df = None
    for file in os.listdir('../data'):
        print("file: {}".format(file))
        temp = pd.read_csv('../data/' + file, dtype=dtypes)
        if df is None:
            df = temp
        else:
            df = pd.concat([df, temp], ignore_index=True)
    # SQLite can only store none as null
    return df.drop(columns=columnsToDrop).replace([np.nan], [None])


def insert_industries(con, cur, industries: DataFrame):
    sort = industries.sort_values(['industry sector code', 'year'], ascending=False)
    # Drop any duplicates by code keeping the most recent
    deduped = sort.drop_duplicates(subset=['industry sector code'], keep='first')
    data = [tup[0:] for tup in deduped.itertuples(index=False)]
    try:
        cur.executemany("insert into industry ('id', 'name', 'source_year') values (?, ?, ?)",
                        data)
        con.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")


def insert_facilities(con, cur, facilities: DataFrame):
    sort = facilities.sort_values(['trifd', 'year'], ascending=False)
    # Drop any duplicates by ID, lat/long keeping the most recent
    deduped = sort.drop_duplicates(subset=['trifd', 'latitude', 'longitude'], keep='first')
    data = [tup[0:] for tup in deduped.itertuples(index=False)]
    try:
        cur.executemany("insert into facility ('id', 'name', 'address', 'city', 'county', 'state', 'zip', 'latitude', "
                        "'longitude', 'parent_co_id', 'parent_name', 'parent_standard_name', 'federal', 'industry_id', "
                        " 'source_year') values ( ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?)",
                        data)
        con.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")


def insert_chemicals(con, cur, chemicals: DataFrame):
    sort = chemicals.sort_values(['tri chemical/compound id', 'year'], ascending=False)
    # Drop any duplicates by ID keeping the most recent
    deduped = sort.drop_duplicates(subset=['tri chemical/compound id'], keep='first')
    data = [tup[0:] for tup in deduped.itertuples(index=False)]
    try:
        cur.executemany(
            "insert into chemical ( 'name', 'id', 'cas_num', 'srs_id', 'caa_chem', 'classification', 'metal', "
            "'metal_category', 'carcinogen', 'unit','source_year') values (?, ?, ?,?, ?, ?,?, ?, ?,?, ?)",
            data)
        con.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")


def insert_measurements(con, cur, measurements: DataFrame):
    data = [tup[0:] for tup in measurements.itertuples(index=False)]
    try:
        cur.executemany("insert into measurement ('facility_id', 'chem_id', 'fugitive_air', 'stack_air',"
                        "'single_release','prod_ratio','prod_waste',"
                        "'year','primary_sic', 'primary_naics') values (?, ?, ?,?, ?, ?,?, ?, ?,?)",
                        data)
        con.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Make connection to the tri data DB
    connection = sqlite3.connect('tri.db')
    cursor = connection.cursor()

    create_schema(cursor)
    populate_data(connection, cursor)
    connection.close()
