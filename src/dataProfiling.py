import pandas as pd
from ydata_profiling import ProfileReport
import glob

dtypes = {'year': int,
          'trifd': 'category',
          'frs id': 'category',
          'facility name': 'category',
          'street address': 'string',
          'city': 'category',
          'county': 'category',
          'st': 'category',
          'zip': 'category',
          'latitude': float,
          'longitude': float,
          'horizontal datum': 'category',
          'parent co name': 'string',
          'parent co db num': 'category',
          'standard parent co name': 'string',
          'federal facility': 'string',
          'industry sector code': 'category',
          'industry sector': 'string',
          'primary sic': 'category',
          'sic 2': 'category',
          'primary naics': 'category',
          'doc_ctrl_num': 'category',
          'chemical': 'category',
          'elemental metal included': 'category',
          'tri chemical/compound id': 'category',
          'cas#': 'string',
          'srs id': 'string',
          'clean air act chemical': 'category',
          'classification': 'category',
          'metal': 'category',
          'metal category': 'category',
          'carcinogen': 'category',
          'pbt': 'category',
          'pfas': 'category',
          'form type': 'category',
          'unit of measure': 'category',
          '5.1 - fugitive air': float,
          '5.2 - stack air': float,
          '8.5 - recycling off sit': float,
          '8.6 - treatment on site': float,
          '8.7 - treatment off site': float,
          'production wste (8.1-8.7)': float,
          '8.8 - one-time release': float,
          '8.9 - production ratio': float}
columnsToKeep = ['year', 'trifd', 'latitude', 'longitude', 'horizontal datum', 'parent co name', 'federal facility',
                 'industry sector code', 'primary sic', 'primary naics', 'cas#', 'srs id',
                 'clean air act chemical', 'classification', 'metal category', 'carcinogen', 'pfas',
                 '5.1 - fugitive air', '5.2 - stack air', 'production wste (8.1-8.7)', '8.8 - one-time release',
                 '8.9 - production ratio']
df = None
print(f"Keeping {len(columnsToKeep)} columns")
for yr in range(1987, 2023):
    print(f"Year: {yr}")
    df = None
    for file in glob.glob(f"../data/{yr}*.csv"):
        print("file: {}".format(file))
        temp = pd.read_csv('../data/' + file, na_values=["nan"], dtype=dtypes)[columnsToKeep]
        if df is None:
            df = temp
        else:
            df = pd.concat([df, temp], ignore_index=True)
    if df is not None:
        profile = ProfileReport(df, title=f"Pandas Profiling Report for {yr}")
        profile.to_file(f"../outputs/profilingReport{yr}.html")

