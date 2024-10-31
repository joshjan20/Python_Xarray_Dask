import xarray as xr
import numpy as np
import pandas as pd

# Create sample data for lat, lon, time
lat = np.linspace(-90, 90, 180)    # 180 points from -90 to 90 degrees
lon = np.linspace(0, 360, 360)     # 360 points from 0 to 360 degrees
time = pd.date_range("2000-01-01", "2000-12-31", freq="D")  # Daily data for one year

# Generate synthetic SST data (random data)
data = 15 + 10 * np.random.randn(len(time), len(lat), len(lon))  # Mean 15°C, with some noise

# Create the xarray Dataset
ds = xr.Dataset(
    {
        "sst": (["time", "lat", "lon"], data),
    },
    coords={
        "lat": lat,
        "lon": lon,
        "time": time,
    },
)

# Save to NetCDF
ds.attrs['description'] = "Synthetic Sea Surface Temperature data"
ds.to_netcdf("sst_data.nc")
print("Sample SST NetCDF file created as 'sst_data.nc'")
