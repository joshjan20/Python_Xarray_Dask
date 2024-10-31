import xarray as xr
import dask.array as da
import matplotlib.pyplot as plt

# 1. Load the dataset with xarray
# Assume 'sst_data.nc' is a NetCDF file with SST data
file_path = 'sst_data.nc'
ds = xr.open_dataset(file_path, chunks={'time': 12, 'lat': 180, 'lon': 360})

# Inspect the dataset
print(ds)

# 2. Select the SST variable and examine its attributes
sst = ds['sst']
print(sst)

# 3. Slice the data for a region (e.g., North Pacific Ocean)
# Specify latitude and longitude bounds for a specific region
region_sst = sst.sel(lat=slice(10, 50), lon=slice(120, 250))

# 4. Calculate the monthly mean over the selected region
# Here, dask is used for lazy evaluation to handle large data
monthly_mean_sst = region_sst.groupby('time.month').mean(dim='time')

# 5. Visualize the monthly mean SST for January
plt.figure(figsize=(10, 6))
monthly_mean_sst.sel(month=1).plot(cmap='coolwarm')
plt.title("Monthly Mean Sea Surface Temperature (January)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# 6. Calculate the yearly mean SST over time
yearly_mean_sst = region_sst.resample(time='1Y').mean(dim='time')

# Plot the yearly mean SST timeseries for a specific point
plt.figure(figsize=(10, 6))
yearly_mean_sst.sel(lat=30, lon=160, method='nearest').plot(marker='o')
plt.title("Yearly Mean SST at (lat=30, lon=160)")
plt.xlabel("Year")
plt.ylabel("Sea Surface Temperature (°C)")
plt.show()
