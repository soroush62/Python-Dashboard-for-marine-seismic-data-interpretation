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

# Define the grid size
grid_size = 500
grid_x, grid_y = np.mgrid[df['Distance'].min():df['Distance'].max():complex(grid_size),
                          df['Depth'].min():df['Depth'].max():complex(grid_size)]

# Interpolate the amplitude data
grid_z = griddata((df['Distance'], df['Depth']), df['Amplitude'], (grid_x, grid_y), method='linear')

# Handle NaNs if necessary (e.g., replace them with zeros or perform further interpolation)
grid_z = np.nan_to_num(grid_z)

# Convert numpy int to Python float
grid_z = grid_z.astype(float)

# Initialize a chart
chart = lc.ChartXY(theme=lc.Themes.Dark, title='2D Seismic Section')

# Create HeatmapGridSeries
heatmap = chart.add_heatmap_grid_series(
    columns=grid_size,
    rows=grid_size,
)

# Set start and end coordinates
heatmap.set_start(x=float(df['Distance'].min()), y=float(df['Depth'].min()))
heatmap.set_end(x=float(df['Distance'].max()), y=float(df['Depth'].max()))

# Set step size
heatmap.set_step(x=float((df['Distance'].max() - df['Distance'].min()) / grid_size), y=float((df['Depth'].max() - df['Depth'].min()) / grid_size))

# Enable intensity interpolation
heatmap.set_intensity_interpolation(True)

# Invalidate intensity values
heatmap.invalidate_intensity_values(grid_z.tolist())

# Hide wireframe
heatmap.hide_wireframe()

# Customize the color palette similar to the seismic colormap
palette_steps = [
    {'value': float(np.min(grid_z)), 'color': lc.Color(0, 0, 128)},  # Dark Blue
    {'value': float(np.min(grid_z) + (np.max(grid_z) - np.min(grid_z)) * 0.25), 'color': lc.Color(0, 0, 255)},  # Blue
    {'value': float(np.min(grid_z) + (np.max(grid_z) - np.min(grid_z)) * 0.5), 'color': lc.Color(196, 164, 132)},  # White
    {'value': float(np.min(grid_z) + (np.max(grid_z) - np.min(grid_z)) * 0.75), 'color': lc.Color(255, 0, 0)},  # Red
    {'value': float(np.max(grid_z)), 'color': lc.Color(128, 0, 0)},  # Dark Red
]

heatmap.set_palette_colors(
    steps=palette_steps,
    look_up_property='value',
    interpolate=True
)

# Set axis titles
chart.get_default_x_axis().set_title('Distance')
chart.get_default_y_axis().set_title('Depth')

# Set axis limits based on the actual data ranges
chart.get_default_x_axis().set_interval(float(df['Distance'].min()), float(df['Distance'].max()))
chart.get_default_y_axis().set_interval(float(df['Depth'].min()), float(df['Depth'].max()))

# Display chart
chart.open()
