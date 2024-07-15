import lightningchart as lc
import numpy as np
import pandas as pd
from scipy.interpolate import griddata

lc.set_license('my-license-key')

file_path = 'Cross-line-654.csv'
data = pd.read_csv(file_path, header=None)

# Extract distance and amplitude values
distances = data.iloc[:, 0].values
amplitudes = data.iloc[:, 3:].values

# Handle NaNs if necessary (e.g., replace them with zeros or perform further interpolation)
amplitudes = np.nan_to_num(amplitudes)

# Create interpolated grid
grid_size = 1000  # Reduced grid size for faster processing
x_values = distances.astype(float).tolist()
y_values = np.arange(amplitudes.shape[1]).astype(float).tolist()
grid_x, grid_y = np.mgrid[min(x_values):max(x_values):complex(grid_size), min(y_values):max(y_values):complex(grid_size)]
grid_z = griddata((np.repeat(distances, amplitudes.shape[1]), np.tile(y_values, distances.size)), amplitudes.ravel(), (grid_x, grid_y), method='linear')

# Convert numpy int to Python int
grid_z = grid_z.astype(float)

# Rotate the grid by 180 degrees
grid_z = np.flip(grid_z, axis=(0, 1)).tolist()

# Initialize a chart
chart = lc.ChartXY(theme=lc.Themes.Dark, title='GeologicalStrataHeatmap-Cross-line-654')

# Create HeatmapGridSeries
heatmap = chart.add_heatmap_grid_series(
    columns=grid_size,
    rows=grid_size,
)

# Set start and end coordinates
heatmap.set_start(x=min(x_values), y=min(y_values))
heatmap.set_end(x=max(x_values), y=max(y_values))

# Set step size
heatmap.set_step(x=(max(x_values) - min(x_values)) / grid_size, y=(max(y_values) - min(y_values)) / grid_size)

# Enable intensity interpolation
heatmap.set_intensity_interpolation(True)

# Invalidate intensity values
heatmap.invalidate_intensity_values(grid_z)

# Hide wireframe
heatmap.hide_wireframe()

# Define custom palette to match the second image
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

# Set axis titles
chart.get_default_x_axis().set_title('Distance')
chart.get_default_y_axis().set_title('Depth')

# Set axis limits based on the actual data ranges
chart.get_default_x_axis().set_interval(min(x_values), max(x_values))
chart.get_default_y_axis().set_interval(min(y_values), max(y_values))
chart.add_legend(data=heatmap)

chart.open()



