import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from folium.plugins import MarkerCluster
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# clustering
df = pd.read_csv("measurement_1.csv")
facility = pd.read_csv("facility.csv")
dff = pd.merge(df, facility, left_on='facility_id', right_on='id', how='inner')

numeric_columns = dff.select_dtypes(include=['float64', 'int64']).columns
data = dff[numeric_columns]

imputer = SimpleImputer(strategy='mean')
data_imputed = imputer.fit_transform(data)

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_imputed)

pca = PCA(n_components=0.95)
data_pca = pca.fit_transform(data_scaled)

kmeans = KMeans(n_clusters=5, random_state=42)
dff['cluster'] = kmeans.fit_predict(data_pca)

latitude = dff['latitude']
longitude = dff['longitude']
map_center = [latitude.mean(), longitude.mean()]

# m = folium.Map(location=map_center, zoom_start=10)
#
# folium.CircleMarker(
#     location=[latitude.iloc[0], longitude.iloc[0]],
#     radius=5,
#     color='blue',
#     fill=True,
#     fill_color='blue',
#     fill_opacity=0.5,
#     popup=f"Cluster: {dff['cluster'].iloc[0]}"
# ).add_to(m)

# marker_cluster = MarkerCluster().add_to(m)
# for idx, row in dff.iterrows():
#     lat = row['latitude']
#     lon = row['longitude']
#     cluster_id = row['cluster']
#
#     normalized = (cluster_id - dff["cluster"].min()) / (dff["cluster"].max() - dff["cluster"].min())
#     color = plt.cm.get_cmap("tab20")(normalized)
#     color_hex = mcolors.to_hex(color)
#
#     folium.CircleMarker(
#         location=[lat, lon],
#         radius=5,
#         color=color_hex,
#         fill=True,
#         fill_color=color_hex,
#         fill_opacity=0.5,
#         popup=f"Cluster: {cluster_id}"
#     ).add_to(marker_cluster)
#
# m.save("kmeans_clusters_with_marker_cluster_map.html")
# above is attempt at folium
# aggregate group by year
df1 = pd.read_csv('measurement_1.csv')
df2 = pd.read_csv('measurement_2.csv')
df_fin = pd.concat([df1, df2], ignore_index=True)

grouped_df = df_fin.groupby('facility_id')['year'].nunique().reset_index(name='distinct_year_count')

over_15_yrs = list(grouped_df[grouped_df['distinct_year_count'] > 15]["facility_id"])
lst = []
for index, row in df_fin.iterrows():
    if row['facility_id'] in over_15_yrs:
        lst.append(row)

new_df = pd.DataFrame(lst)
new_df.to_csv('measurement_over_15.csv', index=False)

# data clean/splitting
df1 = pd.read_csv('measurement_over_15.csv')
cnt = len(df1)//3

pt1 = df1.iloc[:cnt]
pt2 = df1.iloc[cnt:2*cnt]
pt3 = df1.iloc[2*cnt:]

pt1.to_csv('measurement_over_15_1.csv', index=False)
pt2.to_csv('measurement_over_15_2.csv', index=False)
pt3.to_csv('measurement_over_15_3.csv', index=False)

# concat
df1 = pd.read_csv('measurement_over_15.csv')
df2 = pd.read_csv('measurement_over_15_1.csv')
df3 = pd.read_csv('measurement_over_15_2.csv')
df4 = pd.read_csv('measurement_over_15_3.csv')
dff = pd.concat([df1, df2, df3, df4], ignore_index=True)
dff.to_csv('measurement_over_15_fin.csv', index=False)

# merge
df = pd.read_csv('measurement_over_15_fin.csv')
facility = pd.read_csv('facility.csv')
industry = pd.read_csv('industry.csv')
chemical = pd.read_csv('chemical.csv')

dff = pd.merge(df, facility, left_on='facility_id', right_on='id', how='left')
dfff = pd.merge(dff, industry, left_on='industry_id', right_on='id', how='left')
df_final = dfff.loc[:, ~dfff.columns.str.contains('_x$|_y$', case=False)]
df_final.to_csv("final_df.csv", index=False)

# decision tree
df = pd.read_csv('final_df.csv')
df['year_group'] = (df['year'] // 7) * 7

quantifiable_fields = ['fugitive_air', 'stack_air', 'prod_waste', 'single_release', 'prod_ratio']
df_avg = df.groupby(['facility_id', 'year_group'])[quantifiable_fields].mean().reset_index()

X = df_avg[['year_group']]
y = df_avg['prod_waste']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

plt.figure(figsize=(15, 10))
plot_tree(model, filled=True, feature_names=['year_group'], fontsize=10, impurity=False, rounded=True)
plt.title('Decision Tree for Production Waste for Fugitive Air Over Time')

import matplotlib.lines as mlines
legend_elements = [
    mlines.Line2D([], [], marker='o', color='red', label='High Fugitive Air'),
    mlines.Line2D([], [], marker='o', color='white', markeredgecolor='black', label='Low Fugitive Air')
]

plt.legend(handles=legend_elements, loc='upper left', fontsize=12)
plt.show()

# pca + kmeans
scaler = StandardScaler()
scaled_data = scaler.fit_transform(dfff)

pca = PCA(n_components=0.95)
reduced_data = pca.fit_transform(scaled_data)

inertia = []
for k in range(1, 20):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(reduced_data)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 20), inertia, color='black')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Inertia vs. Number of Clusters')
plt.grid(color='b', linestyle='--', linewidth=0.5)
plt.show()
#here is the inertia graph if needed
best_k = 20
kmeans = KMeans(n_clusters=best_k, random_state=42)
kmeans.fit(reduced_data)
dfff['cluster'] = kmeans.labels_

cnt = len(dfff)//3
pt1 = dfff.iloc[:cnt]
pt2 = dfff.iloc[cnt:2*cnt]
pt3 = dfff.iloc[2*cnt:]

pt1.to_csv('pca_1.csv', index=False)
pt2.to_csv('pca_2.csv', index=False)
pt3.to_csv('pca_3.csv', index=False)

# Correlation Matrix
df = pd.read_csv('final_df.csv')
quantifiable_fields = ['fugitive_air', 'stack_air', 'single_release', 'prod_ratio']

X = df[quantifiable_fields]
correlation_matrix = X.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True, linewidths=0.5)
plt.title('Correlation Matrix of Quantifiable Fields')
plt.show()

# TrendGraph
df = pd.read_csv('final_df.csv')
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

axs[0].plot(df['year'], df['fugitive_air'], label='Fugitive Air', marker='o', linestyle='-', color='blue')
axs[0].set_title("Fugitive Air Trend Over Years")
axs[0].set_xlabel("Year")
axs[0].set_ylabel("Fugitive Air Value")
axs[0].legend()

axs[1].plot(df['year'], df['stack_air'], label='Stack Air', marker='o', linestyle='-', color='green')
axs[1].set_title("Stack Air Trend Over Years")
axs[1].set_xlabel("Year")
axs[1].set_ylabel("Stack Air Value")
axs[1].legend()

axs[2].plot(df['year'], df['prod_waste'], label='Production Waste', marker='o', linestyle='-', color='red')
axs[2].set_title("Production Waste Trend Over Years")
axs[2].set_xlabel("Year")
axs[2].set_ylabel("Production Waste Value")
axs[2].legend()

plt.tight_layout()
plt.show()

# Region-wise Pie Chart for Production Waste Distribution
df = pd.read_csv('final_df.csv')

def assign_region(row):
    if row['latitude'] > 40:
        return 'North'
    elif row['longitude'] < -90:
        return 'East'
    else:
        return 'West' if row['latitude'] < 40 else 'South'

df['region'] = df.apply(assign_region, axis=1)

region_prod_waste = df.groupby('region')['prod_waste'].sum()

plt.figure(figsize=(8, 8))
plt.pie(region_prod_waste, labels=region_prod_waste.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99','#ffcc99','#ff6666'])
plt.title('Production Waste Distribution by Region of the USA')
plt.axis('equal')
plt.show()
