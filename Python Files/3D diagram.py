import lightningchart as lc
import numpy as np
import pandas as pd
from scipy.interpolate import griddata

# Read the license key from a file
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the data
file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/NRCAN_Laurentian_Basin/Export/Dip-steeredMedianFiltered_Seismic/output.csv'
df = pd.read_csv(file_path)

# Rename columns for convenience
df.columns = ['Distance', 'Depth', 'Amplitude']

# Convert columns to standard Python float type
df['Distance'] = df['Distance'].astype(float)
df['Depth'] = df['Depth'].astype(float)
df['Amplitude'] = df['Amplitude'].astype(float)

# Define the grid size
grid_size = 500
grid_x, grid_y = np.mgrid[df['Distance'].min():df['Distance'].max():complex(grid_size),
                          df['Depth'].min():df['Depth'].max():complex(grid_size)]

# Interpolate the amplitude data
grid_z = griddata((df['Distance'], df['Depth']), df['Amplitude'], (grid_x, grid_y), method='linear')

# Handle NaNs if necessary (e.g., replace them with zeros or perform further interpolation)
grid_z = np.nan_to_num(grid_z)

# Initialize a chart
chart = lc.Chart3D(theme=lc.Themes.Dark, title='3D Seismic Section')

# Create SurfaceGridSeries
surface = chart.add_surface_grid_series(
    columns=grid_size,
    rows=grid_size,
)

# Set start and end coordinates
surface.set_start(df['Distance'].min(), df['Depth'].min())
surface.set_end(df['Distance'].max(), df['Depth'].max())

# Set step size
surface.set_step((df['Distance'].max() - df['Distance'].min()) / grid_size, (df['Depth'].max() - df['Depth'].min()) / grid_size)

# Set the height data to be the amplitude values
surface.invalidate_height_map(grid_z.tolist())

# Enable intensity interpolation
surface.set_intensity_interpolation(True)

# Invalidate intensity values
surface.invalidate_intensity_values(grid_z.tolist())

# Customize the color palette similar to the seismic colormap
surface.set_palette_colors(
    steps=[
        {'value': grid_z.min(), 'color': lc.Color(0, 0, 128)},  # Dark Blue
        {'value': grid_z.min() / 2, 'color': lc.Color(0, 0, 255)},  # Blue
        {'value': 0.0, 'color': lc.Color(255, 255, 255)},  # White
        {'value': grid_z.max() / 2, 'color': lc.Color(255, 0, 0)},  # Red
        {'value': grid_z.max(), 'color': lc.Color(128, 0, 0)},  # Dark Red
    ],
    look_up_property='value',
    interpolate=True
)

# Set axis titles
chart.get_default_x_axis().set_title('Distance')
chart.get_default_y_axis().set_title('Depth')
chart.get_default_z_axis().set_title('Amplitude')

# Display chart
chart.open()
