import lightningchart as lc
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

# Read the license key from a file
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the data
file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/Blake_Ridge_Hydrates_3D/Export/Z-slice-4700.csv'
data = pd.read_csv(file_path, header=None)

# Split the data into columns based on the expected format
data.columns = ['X', 'Y', 'Z']

# Extract X, Y, Z values
X = data['X'].values
Y = data['Y'].values
Z = data['Z'].values

# Create a grid of points
grid_x, grid_y = np.meshgrid(
    np.linspace(X.min(), X.max(), 500),  # Increase resolution for better clarity
    np.linspace(Y.min(), Y.max(), 500)
)

# Interpolate Z values on the grid using linear interpolation
grid_z = griddata((X, Y), Z, (grid_x, grid_y), method='linear')

# Fill any remaining NaN values with nearest method
grid_z = np.where(np.isnan(grid_z), griddata((X, Y), Z, (grid_x, grid_y), method='nearest'), grid_z)

# Create a chart
chart = lc.ChartXY(theme=lc.Themes.Dark, title='2D Seismic Section')

# Add a Heatmap Grid Series
heatmap = chart.add_heatmap_grid_series(
    columns=grid_x.shape[1],
    rows=grid_y.shape[0]
)

# Set the start and end coordinates for the heatmap
heatmap.set_start(x=0, y=0)  # Start at 0 for both axes
heatmap.set_end(x=1300, y=100)  # Set end to 1300 for x-axis and 100 for y-axis

# Set the intensity values
heatmap.invalidate_intensity_values(grid_z)

# Define custom palette to better match the expected result
custom_palette = [
    {"value": -1.0, "color": lc.Color(255, 0, 0)},     # Black  
    {"value": -0.5, "color": lc.Color(50, 50, 50)},  # Dark Gray   
    {"value": 0, "color": lc.Color(255, 255, 255)},  # White  
    {"value": 0.33, "color": lc.Color(150, 75, 0)},  # Brown
    {"value": 0.66, "color": lc.Color(0, 0, 255)},   # Blue   
    {"value": 1.0, "color": lc.Color(0, 0, 0)},    # Red    
]

heatmap.set_palette_colors(
    steps=custom_palette,
    look_up_property='value',
    interpolate=True
)

# Customize axes
chart.get_default_x_axis().set_title('X')
chart.get_default_y_axis().set_title('Y')
chart.add_legend(data=heatmap)
chart.open()



