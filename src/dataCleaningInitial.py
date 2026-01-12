import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# sample = pd.read_csv("2014_us.csv")
# print(sample.columns.str.replace(r'^\d+\.\s*', '', regex=True).str.lower())
#
# yr = 1987
# ten = 1
# while yr < 2023:
#     if ten <= 10:
#         s = pd.read_csv(f"{yr}_us.csv", low_memory=False)
#         s.columns = s.columns.str.replace(r'^\d+\.\s*', '', regex=True).str.lower()
#         df = pd.concat([df, s], ignore_index=True)
#         yr = yr + 1
#         ten = ten + 1
#     if ten >10:
#         df.to_csv(f"{yr-10}_{yr-1}.csv", index=False)
#         print(yr-10, yr-1)
#         df = pd.DataFrame()
#         ten = 1

# for a in range(2017, 2023):
#     s = pd.read_csv(f"{a}_us.csv", low_memory=False)
#     s.columns = s.columns.str.replace(r'^\d+\.\s*', '', regex=True).str.lower()
#     df = pd.concat([df, s], ignore_index=True)
# df.to_csv(f"{2017}_{2023}.csv", index=False)
#
# empty = pd.DataFrame()
# for s in string_df:
#     z = pd.read_csv(string_df[0], low_memory=False)
#     z = z.isna().sum()#.sort_values(ascending=False)
#     empty[s[:-4]] = z
# empty.to_csv("empty_values.csv", index=True)
# for a in string_df:
#     z = pd.read_csv(string_df[0], low_memory=False)
#     string_shape.append(z.shape[0])
# print(string_shape) #[833049, 833049, 833049, 833049]

# empty_val = pd.read_csv("empty_values.csv")
# empty_val_proportions = empty_val
# print(empty_val_proportions.iloc[30])
# for i in empty_val:
#     if i in string_csv:
#         for a in empty_val[i]:
#                 #print(a, string_shape[string_csv.index(i)])
#                 empty_val_proportions.iloc[i][v] = a/string_shape[string_csv.index(i)]
# #empty_val_proportions.to_csv("empty_values_proportions.csv", index=True)

# columns_to_remove = ["bia", "tribe",
# "foreign parent co name",
# "foreign parent co db num",
# "standard foreign parent co name",
# "sic 3",
# "sic 4",
# "sic 5",
# "sic 6",
# "naics 2",
# "naics 3",
# "naics 4",
# "naics 5",
# "naics 6",
# "prod_ratio_or_ activity"]
#
#
# for a in string_df:
#     df = pd.read_csv(a)
#     df.drop(columns=[col for col in columns_to_remove if col in df.columns], inplace=True)
#     df.to_csv(f"{a[:-4]}_2.csv")
# df = pd.DataFrame()
# string_csv = ['1987_1996', '1997_2006', '2007_2016', '2017_2023']
# string_shape = [833049, 833049, 833049, 833049]
#
# for s in string_df:
#     z = pd.read_csv(string_df[0], low_memory=False)
#     z = z.isna().sum()#.sort_values(ascending=False)
#     nulls_dict[s[:-4]] = z
# nulls_df = pd.DataFrame(nulls_dict)
# nulls_df.to_csv("empty_values.csv", index=True)

# for a in string_df:
#     df = pd.read_csv(a)
#     zero_counts = (df == 0).sum()
#     zero_counts_dict[a] = zero_counts
# zero_counts_df = pd.DataFrame(zero_counts_dict)
# zero_counts_df.to_csv('zero_counts.csv', index=True)

# nulls_dict = {}
# zero_counts_dict = {}
# zero_col_to_drop = ['5.3 - water','5.4 - underground','5.4.1 - underground cl i',
#                     '5.4.2 - underground c ii-v','5.5.1 - landfills','5.5.1a - rcra c landfill',
#                     '5.5.1b - other landfills','5.5.2 - land treatment','5.5.3 - surface impndmnt',
#                     '5.5.3a - rcra surface im','5.5.3b - other surface i','5.5.4 - other disposal',
#                     'on-site release total','6.1 - potw - trns rlse','6.1 - potw - trns trt',
#                     'potw - total transfers','6.2 - m10','6.2 - m41','6.2 - m62','6.2 - m40 metal',
#                     '6.2 - m61 metal','6.2 - m71','6.2 - m81','6.2 - m82','6.2 - m72','6.2 - m63',
#                     '6.2 - m66','6.2 - m67','6.2 - m64','6.2 - m65','6.2 - m73','6.2 - m79','6.2 - m90',
#                     '6.2 - m94','6.2 - m99','off-site release total','6.2 - m20','6.2 - m24','6.2 - m26',
#                     '6.2 - m28','6.2 - m93','off-site recycled total','6.2 - m56','6.2 - m92',
#                     'off-site energy recovery t','6.2 - m40 non-metal','6.2 - m50','6.2 - m54',
#                     '6.2 - m61 non-metal','6.2 - m69','6.2 - m95','off-site treated total',
#                     '6.2 - unclassified','6.2 - total transfer','total releases','8.1 - releases',
#                     '8.1a - on-site contained','8.1b - on-site other','8.1c - off-site contain',
#                     '8.1d - off-site other r','8.2 - energy recover on','8.3 - energy recover of',
#                     '8.4 - recycling on site']

# for file in string_df:
#     df = pd.read_csv(file)
#     columns_to_drop = [col for col in zero_col_to_drop if col in df.columns]
#     df.drop(columns=columns_to_drop, inplace=True)
#
#     new_file = file[:-6] + '_3.csv'
#     df.to_csv(new_file, index=False)

# dummy_dct = {}
# def mix(column):
#     types = column.apply(type).unique()
#     return len(types) > 1
# for a in string_df:
#     df = pd.read_csv(a)
#     mixed_columns = [col for col in df.columns if mix(df[col])]
#     dummy_dct[a] = mixed_columns
#
# for a, b in dummy_dct.items():
#     if b:
#         print(f"Mixed type columns in {a}: {b}")
# t = pd.read_csv(string_df[0])
#print([a for a in t['parent co name'] if type(a) == float])
# print(set([type(a) for a in t[mixtype_1987_1996_3[0]]]))
# print(set([type(a) for a in t[mixtype_1987_1996_3[1]]]))
# print(set([type(a) for a in t[mixtype_1987_1996_3[2]]]))
# print(set([type(a) for a in t[mixtype_1987_1996_3[3]]]))
# print(set([type(a) for a in t[mixtype_1987_1996_3[4]]]))
# print(set([type(a) for a in t[mixtype_1987_1996_3[5]]]))
# print(set([type(a) for a in t[mixtype_1987_1996_3[6]]]))
# {<class 'str'>, <class 'int'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}
# print("------")
# t = pd.read_csv(string_df[1])
# print([a for a in t[mixtype_1997_2006_3[6]] if type(a) == float])
# print(set([type(a) for a in t[mixtype_1997_2006_3[0]]]))
# print(set([type(a) for a in t[mixtype_1997_2006_3[1]]]))
# print(set([type(a) for a in t[mixtype_1997_2006_3[2]]]))
# print(set([type(a) for a in t[mixtype_1997_2006_3[3]]]))
# print(set([type(a) for a in t[mixtype_1997_2006_3[4]]]))
# print(set([type(a) for a in t[mixtype_1997_2006_3[5]]]))
# print(set([type(a) for a in t[mixtype_1997_2006_3[6]]]))
# {<class 'str'>, <class 'int'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}
# {<class 'float'>, <class 'str'>}



# print("------")
# t = pd.read_csv(string_df[2])
# print(set([type(a) for a in t[mixtype_2007_2016_3[0]]]))
# print(set([type(a) for a in t[mixtype_2007_2016_3[1]]]))
# print(set([type(a) for a in t[mixtype_2007_2016_3[2]]]))
# print(set([type(a) for a in t[mixtype_2007_2016_3[3]]]))
# # {<class 'float'>, <class 'str'>}
# # {<class 'float'>, <class 'str'>}
# # {<class 'float'>, <class 'str'>}
# # {<class 'float'>, <class 'str'>}
#
# print("------")
# t = pd.read_csv(string_df[3])
# print(set([type(a) for a in t[mixtype_2017_2023_3[0]]]))
# print(set([type(a) for a in t[mixtype_2017_2023_3[1]]]))
# print(set([type(a) for a in t[mixtype_2017_2023_3[2]]]))
# print(set([type(a) for a in t[mixtype_2017_2023_3[3]]]))
# # {<class 'float'>, <class 'str'>}
# # {<class 'float'>, <class 'str'>}
# # {<class 'float'>, <class 'str'>}
# # {<class 'float'>, <class 'str'>}

# mixtype_1987_1996_3 = ['zip', 'horizontal datum', 'parent co name', 'parent co db num', 'standard parent co name', 'primary sic', 'sic 2']
# mixtype_1997_2006_3 = ['zip', 'horizontal datum', 'parent co name', 'parent co db num', 'standard parent co name', 'primary sic', 'sic 2']
# mixtype_2007_2016_3 = ['horizontal datum', 'parent co name', 'parent co db num', 'standard parent co name']
# mixtype_2017_2023_3 = ['horizontal datum', 'parent co name', 'parent co db num', 'standard parent co name']
#
# dc = {
#     '1987_1996_3.csv': mixtype_1987_1996_3,
#     '1997_2006_3.csv': mixtype_1997_2006_3,
#     '2007_2016_3.csv': mixtype_2007_2016_3,
#     '2017_2023_3.csv': mixtype_2017_2023_3
# }
#
# for a in string_df:
#     df = pd.read_csv(a)
#     if 'zip' in df.columns:
#         df['zip'] = df['zip'].astype(str)
#     for field in dc[a]:
#         if field in df.columns:
#             df[field] = df[field].fillna('Unlisted')
#     new_file = a[:-6] + '_4.csv'
#     df.to_csv(new_file, index=True)
# brew install gdal
import geopandas as gpd
import geoplots as gplt
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import cartopy.crs as ccrs
import folium
string_df = ['1991_2.csv', '1991_2.csv']
variance_dict = {}

tmp = pd.read_csv(string_df[0])
tmp2 = pd.read_csv(string_df[1])
tmp = pd.concat([tmp, tmp2])

tmp_sub_gpd = gpd.GeoDataFrame(tmp["5.1 - fugitive air"],
                               geometry=gpd.points_from_xy(tmp.longitude, tmp.latitude), crs="EPSG:4326")

map_center = [tmp.latitude.mean(), tmp.longitude.mean()]

m = folium.Map(location=map_center, zoom_start=5)
min_value = tmp["5.1 - fugitive air"].min()
max_value = tmp["5.1 - fugitive air"].max()
#print(min_value, max_value)
norm = mcolors.Normalize(vmin=min_value, vmax=max_value)
#print(norm)
cmap = plt.cm.RdYlGn_r
#print(cmap)
map_center = [tmp.latitude.mean(), tmp.longitude.mean()]
m = folium.Map(location=map_center, zoom_start=5)

for idx, row in tmp_sub_gpd.iterrows():
    air_value = row["5.1 - fugitive air"]
    normalized = np.log(air_value+1) / np.log(max_value+1)
    # if normalized > 0.5:
    #     print(normalized)
    color = cmap(normalized)
    color_hex = mcolors.to_hex(color)

    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=5,
        color=color_hex,
        fill=True,
        fill_color=color_hex,
        fill_opacity=.5
    ).add_to(m)
m.save("tmp_map.html")

# for a in string_df:
#     df = pd.read_csv(a)
#     if "8.6 - treatment on site" in df.columns:
#         variance_dict[a] = df["8.6 - treatment on site"].var()
#         plt.figure(figsize=(8, 6))
#         sns.scatterplot(x=df.index, y=df["8.6 - treatment on site"],
#                         palette="viridis", hue=df["8.6 - treatment on site"],  # Coloring by value
#                         size=4, alpha=0.8)
#         plt.title(f"distribution in variance of '8.6 - treatment on site' between {a[:-6]}")
#         plt.ylabel("freq")
#         plt.xlabel("8.6 - treatment on site")
#         plt.show()
# a = pd.read_csv(string_df[0])
# print(max(a['8.6 - treatment on site']), min(a['8.6 - treatment on site']))