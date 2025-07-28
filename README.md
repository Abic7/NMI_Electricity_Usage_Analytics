# NMI_Electricity_Usage_Analytics
The repo provides code to enrich &amp; analyse Australian Consumer Electricity Distributer Usage data.

Requirements:
Usage Data : Usages data downloaded from your australian electricity distributer e.g. United Energy https://myenergy.ue.com.au
Weather Data: Download your local weather data from BOM: Bureau of Meteorology http://www.bom.gov.au/
Python: Version 3.5+

Code and what they do..
nmi_Final.py
1. This code snippet reads your downloaed raw usaged data and enriches data headers accordign to NMI12 or NMI13 specifications.
2. Once enrichment is done the code will specifically extract exact usage data. 

energy_analysis.py
1. This code snippet analysis your electricity usage & weather data and creates a animated GIF on a plot chart
2. it will also provide high level analytics about the data set.

