import lightningchart as lc
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

lc.set_license('my-license-key')

file_path = '3d-XY.xlsx'
df = pd.read_excel(file_path)

# Convert the DataFrame to numpy arrays for X, Y, Z
X = df['X'].values
Y = df['Y'].values
Z = df['Z'].values

# Create a grid of points
grid_x, grid_y = np.meshgrid(
    np.linspace(X.min(), X.max(), 100),
    np.linspace(Y.min(), Y.max(), 100)
)

# Interpolate Z values on the grid using linear interpolation
grid_z = griddata((X, Y), Z, (grid_x, grid_y), method='linear')

# Fill any remaining NaN values with nearest method
grid_z = np.where(np.isnan(grid_z), griddata((X, Y), Z, (grid_x, grid_y), method='nearest'), grid_z)

# Create a 3D chart
chart = lc.Chart3D(
    theme=lc.Themes.Dark,
    title='Seabed Coordinates'
)

# Set 3D bounding box dimensions to highlight the X axis (10 times longer)
chart.set_bounding_box(x=1.0, y=1.0, z=8.0)

# Add a surface grid series
series = chart.add_surface_grid_series(columns=grid_x.shape[1], rows=grid_y.shape[0])

# Set the start, end, and step coordinates with adjusted scaling
series.set_start(x=grid_x.min(), z=grid_y.min()).set_end(x=grid_x.max(), z=grid_y.max()).set_step(
    x=(grid_x.max() - grid_x.min()) / grid_x.shape[1],
    z=(grid_y.max() - grid_y.min()) / grid_y.shape[0]
)

# Set the surface data for height and intensity
series.invalidate_height_map(grid_z.tolist())
series.invalidate_intensity_values(grid_z.tolist())

# Define a color palette
series.set_palette_colors(
    steps=[
        {'value': np.min(grid_z), 'color': lc.Color(0, 0, 255)},  # Blue
        {'value': np.percentile(grid_z, 25), 'color': lc.Color(0, 128, 255)},  # Light Blue
        {'value': np.percentile(grid_z, 50), 'color': lc.Color(255, 255, 255)},  # White
        {'value': np.percentile(grid_z, 75), 'color': lc.Color(255, 255, 0)},  # Yellow
        {'value': np.max(grid_z), 'color': lc.Color(255, 0, 0)},  # Red
    ],
    look_up_property='value',
    percentage_values=False
)
chart.add_legend(data=series)

chart.open()





import lightningchart as lc
import numpy as np
import pandas as pd
from scipy.interpolate import griddata

# Read the license key from a file
lc.set_license('my-license-key')

# Load and preprocess data
file_path = 'path_to_your_file.xlsx'
df = pd.read_excel(file_path)
X, Y, Z = df['X'].values, df['Y'].values, df['Z'].values
grid_x, grid_y = np.meshgrid(np.linspace(X.min(), X.max(), 100), np.linspace(Y.min(), Y.max(), 100))
grid_z = griddata((X, Y), Z, (grid_x, grid_y), method='linear')
grid_z = np.where(np.isnan(grid_z), griddata((X, Y), Z, (grid_x, grid_y), method='nearest'), grid_z)

# Create 3D chart
chart = lc.Chart3D(theme=lc.Themes.Dark, title='Seabed Coordinates')
series = chart.add_surface_grid_series(columns=grid_x.shape[1], rows=grid_y.shape[0])
series.set_start(x=grid_x.min(), z=grid_y.min()).set_end(x=grid_x.max(), z=grid_y.max())
series.invalidate_height_map(grid_z.tolist())
series.invalidate_intensity_values(grid_z.tolist())
series.set_palette_colors(steps=[{'value': np.min(grid_z), 'color': lc.Color(0, 0, 255)},
                                 {'value': np.percentile(grid_z, 25), 'color': lc.Color(0, 128, 255)},
                                 {'value': np.percentile(grid_z, 50), 'color': lc.Color(255, 255, 255)},
                                 {'value': np.percentile(grid_z, 75), 'color': lc.Color(255, 255, 0)},
                                 {'value': np.max(grid_z), 'color': lc.Color(255, 0, 0)}], look_up_property='value', percentage_values=False)
chart.add_legend(data=series)
chart.open()

