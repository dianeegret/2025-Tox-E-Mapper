# Tox-E-Mapper

**Enterprise Analytics Pipeline for Environmental Risk Monitoring**

## Project Overview

Tox-E-Mapper is an end-to-end analytics project designed to improve access to and analysis of the U.S. EPA’s Toxics Release Inventory (TRI) data. The project supports data-driven monitoring of toxic chemical releases by identifying geographic hotspots, facility-level patterns, and temporal trends that can inform environmental risk assessment, operational planning, and policy decisions.

The focus of the project is not only interactive visualization, but also data quality, analytical rigor, and clear translation of complex data into actionable insights.

---

## Data Description

The analysis is based on TRI data published by the U.S. Environmental Protection Agency, covering millions of annual records reported by industrial facilities across the United States.

Key characteristics:

* Over **3 million structured records** spanning multiple decades
* Facility, chemical, geographic, and time-based attributes
* Data suitable for aggregation, validation, clustering, and trend analysis

Raw data files are not included in this repository due to size constraints. The expected schema, validation logic, and transformation steps are documented in the code and notebooks.

---

## Pipeline Architecture

The project follows a structured analytics pipeline:

1. **Data Ingestion**

   * Importing TRI data into a lightweight analytical database
   * Initial schema checks and record count validation

2. **Data Profiling and Validation**

   * Null and duplicate detection
   * Distribution profiling to identify anomalies and zero-heavy features
   * Basic integrity checks to support data quality and governance

3. **Cleaning and Transformation**

   * Standardization of geographic and categorical fields
   * Feature engineering for aggregation and modeling
   * Preparation of analysis-ready datasets

4. **Exploratory Data Analysis**

   * Temporal trend analysis of chemical releases
   * Geographic aggregation to surface regional patterns
   * Facility-level comparisons across industries

5. **Modeling and Segmentation**

   * Dimensionality reduction using Principal Component Analysis (PCA)
   * K-Means clustering to group facilities with similar release profiles
   * Interpretation of clusters to highlight pollution hotspots and outliers

6. **Visualization and Reporting**

   * Interactive dashboard for exploratory analysis and stakeholder use
   * Clear, filterable views to support decision-making

---

## Key Outputs and Insights

* Identification of geographic regions with concentrated toxic releases
* Facility-level clustering revealing patterns not visible in raw data
* Temporal trends showing changes in emissions over time
* Aggregated views suitable for KPI-style monitoring and reporting

These outputs are designed to support exploratory analysis, performance tracking, and downstream forecasting or risk assessment workflows.

---

## Dashboard

An interactive Tableau dashboard was developed to allow non-technical users to explore toxic release trends, geographic distributions, and cluster groupings.

Due to file size limits, Tableau Prep (`.tflx`) and packaged workbook (`.twbx`) files are not stored directly in this repository.

A public, view-only version of the dashboard is available here:
**[https://public.tableau.com/app/profile/diane.egret/viz/ClusteredMap_17440624844360/Dashboard1](https://public.tableau.com/app/profile/diane.egret/viz/ClusteredMap_17440624844360/Dashboard1)**

A local HTML export of the dashboard is also included for offline viewing.

Below is a screenshot of the dashboard for illustrative purposes:

<img src="image/Screenshot.png" width="1000">

---

## Tools and Technologies

* **Python** (data ingestion, profiling, feature engineering, modeling)
* **SQL / SQLite** (data storage, validation, and aggregation)
* **Pandas, NumPy, scikit-learn** (EDA, PCA, clustering)
* **Tableau** (interactive visualization)
* **Git/GitHub** (version control and documentation)

---

## Enterprise Extensions

In a production analytics environment, this project could be extended by:

* Automating ingestion, validation, and refresh cycles using workflow orchestration tools
* Scaling transformations and aggregations using Spark-based pipelines
* Persisting curated datasets for downstream machine learning or forecasting models
* Formalizing data quality checks within a governance framework
* Integrating KPIs into operational dashboards for ongoing monitoring

---

## Repository Structure

```
src/        Core Python scripts for ingestion, profiling, and modeling  
dashboard/  Dashboard documentation
docs/       Project report and poster for additional context  
```

---

## Notes for Reviewers

While this project originated in an academic setting, it is presented here as an **end-to-end analytics system** to demonstrate how I approach data ingestion, validation, analysis, and communication in an enterprise-style environment.
