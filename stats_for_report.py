import dask.dataframe as dd
from dask.diagnostics import ProgressBar
import pandas as pd
import os

# Config
files = ['data1.csv/data1.csv', 'data2.csv/data2.csv']
valid_files = [f for f in files if os.path.exists(f)]
services = ['smsin', 'smsout', 'callin', 'callout', 'internet']

print("Loading data...")
ddf = dd.read_csv(valid_files, assume_missing=True)

# 1. Date Range
ddf['Timestamp'] = dd.to_datetime(ddf['TimeInterval'], unit='ms')
min_date = ddf['Timestamp'].min().compute()
max_date = ddf['Timestamp'].max().compute()

print(f"START_DATE: {min_date}")
print(f"END_DATE: {max_date}")

# 2. Monthly aggregations (to find busiest month)
ddf['Month'] = ddf['Timestamp'].dt.to_period('M')
# We need to compute strict sums.
# Since period isn't supported purely in dask groupby sometimes easily, let's use string 'YYYY-MM'
ddf['MonthStr'] = ddf['Timestamp'].dt.strftime('%Y-%m')
ddf['total_traffic'] = ddf[services].sum(axis=1)

monthly_traffic = ddf.groupby('MonthStr')['total_traffic'].sum().compute()
print("\nMONTHLY_TRAFFIC:")
print(monthly_traffic.sort_values(ascending=False))

# 3. Top Days (Re-confirming)
ddf['DateStr'] = ddf['Timestamp'].dt.strftime('%Y-%m-%d')
daily_traffic = ddf.groupby('DateStr')['total_traffic'].sum().compute()
print("\nTOP_DAYS:")
print(daily_traffic.nlargest(5))

# 4. Top Zones Global
zone_traffic = ddf.groupby('GridID')['total_traffic'].sum().compute()
print("\nTOP_ZONES:")
print(zone_traffic.nlargest(5))
