import lightningchart as lc
import numpy as np
import pandas as pd
from scipy.interpolate import griddata

lc.set_license('my-license-key')

file_path = 'in-line-47.csv'
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
chart = lc.ChartXY(theme=lc.Themes.Dark, title='GeologicalStrataHeatmap-in-line47')

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




import lightningchart as lc
import numpy as np
import pandas as pd
from scipy.interpolate import griddata

# Read the license key from a file
lc.set_license('my-license-key')

# Load and preprocess data
file_path = 'in-line-47.csv'
data = pd.read_csv(file_path, header=None)

data = pd.read_csv(file_path, header=None)
data.columns = ['X', 'Y', 'Z']
X, Y, Z = data['X'].values, data['Y'].values, data['Z'].values
grid_x, grid_y = np.meshgrid(np.linspace(X.min(), X.max(), 500), np.linspace(Y.min(), Y.max(), 500))
grid_z = griddata((X, Y), Z, (grid_x, grid_y), method='linear')
grid_z = np.where(np.isnan(grid_z), griddata((X, Y), Z, (grid_x, grid_y), method='nearest'), grid_z)

# Create heatmap
chart = lc.ChartXY(theme=lc.Themes.Dark, title='GeologicalStrataHeatmap-In-line47')
heatmap = chart.add_heatmap_grid_series(columns=grid_x.shape[1], rows=grid_y.shape[0])
heatmap.set_start(x=0, y=0).set_end(x=1300, y=100)
heatmap.invalidate_intensity_values(grid_z)
heatmap.set_palette_colors(steps=[{"value": -1.0, "color": lc.Color(255, 0, 0)},
                                  {"value": -0.5, "color": lc.Color(50, 50, 50)},
                                  {"value": 0, "color": lc.Color(255, 255, 255)},
                                  {"value": 0.33, "color": lc.Color(150, 75, 0)},
                                  {"value": 0.66, "color": lc.Color(0, 0, 255)},
                                  {"value": 1.0, "color": lc.Color(0, 0, 0)}], look_up_property='value', interpolate=True)
chart.get_default_x_axis().set_title('X')
chart.get_default_y_axis().set_title('Y')
chart.add_legend(data=heatmap)
chart.open()

