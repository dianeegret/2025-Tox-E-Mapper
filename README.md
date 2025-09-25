
Tox-E-Mapper
=====================================
Author: Diane Egret  
Created: April 2025  

Tableau Public Link to Dashboard: https://public.tableau.com/app/profile/diane.egret/viz/ClusteredMap_17440624844360/Dashboard1

Link to Demo Video: https://www.youtube.com/watch?v=nSbnjFp_rTA

------------------------------------
Project Description
------------------------------------
This project provides a spatial visualization of clustered geospatial data using Tableau. The dashboard highlights how data points are grouped into distinct clusters based on spatial or categorical attributes. This clustering enables clearer insights into regional patterns or relationships between geographic points of interest.

The map makes use of:
- Color-coded clusters for clear spatial segmentation
- Tooltips that display relevant metadata for each datapoint
- A search bar and filters to pinpoint specific locations or zoom to areas of interest.

The analysis can be used for applications like:
- Identifying regions of high concentration or interest
- Visualizing service areas, client distributions, or resource allocation

------------------------------------
Data Description
------------------------------------
This dashboard visualizes facility-level data from the TRI Program, managed by the U.S. Environmental Protection Agency (EPA). The TRI program tracks the management of certain toxic chemicals that may pose a threat to human health or the environment. Facilities in different industries are required to report releases of these chemicals to air, water, and land, as well as waste management practices.

Data fields and filters in this dashboard include:
- Year, State, Zip Code, and City: Geospatial filters to explore local or regional trends.
- Industry Name: Coded using NAICS (North American Industry Classification System) for industry-specific filtering.
- Chemical Name: Select from a range of EPA-listed toxic chemicals tracked in the TRI database.
- Carcinogen (Y/N): Indicates whether the chemical is classified as a known or suspected carcinogen.
- Cluster (0 to 19): Groupings derived from clustering analysis based on spatial and production waste attributes.
- Log(Prod. Waste (Pounds)): Size of the data point is based on the logarithm of production waste in pounds, allowing for visualization across several orders of magnitude. Without transforming this field, some data points would be almost invisible and others would be too far-reaching.

------------------------------------
How to Use the Website
------------------------------------
To view the interactive map locally:

Option 1 — Quick View:
- Double-click `Tox_e_mapper.html` to open it in your browser (requires internet access)

Option 2 — Local Server (Recommended):
1. Open a terminal or command prompt in this folder
2. Run:
   > python -m http.server 8000
3. Open your browser and go to:
   > http://localhost:8000

The dashboard should load and allow basic interactions like zooming, panning, clicking and hovering for details.

------------------------------------
Navigating the Dashboard
------------------------------------
- **Hover** over points to reveal detailed information about the facility, waste quantity, and chemical.
- **Zoom & Pan** to explore the map.
- **Filter Controls (Sidebar)**: Use dropdowns and text boxes to filter by location, industry, chemical, toxicity classification or cluster.
- **Click** on a data point to highlight the selected facility.
- **Search Bar (Top-Left)**: Use the built-in Tableau map search to look up specific addresses or place names and explore TRI activity nearby.

------------------------------------
Notes
------------------------------------
- The visualization is hosted on Tableau Public. It requires an internet connection to load.
- This site is for demo use. Not intended for commercial deployment without further hosting setup.
