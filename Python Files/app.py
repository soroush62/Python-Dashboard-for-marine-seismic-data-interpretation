# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the data
# file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/NRCAN_Laurentian_Basin/Export/Dip-steeredMedianFiltered_Seismic/output.csv'
# data = pd.read_csv(file_path)

# # Assuming your data has three columns: Column1, Column2, Column3
# x = data['Column1']
# y = data['Column2']
# z = data['Column3']

# # Plotting the seismic data
# plt.figure(figsize=(10, 6))
# plt.scatter(x, y, c=z, cmap='viridis', marker='.', s=1)
# plt.colorbar(label='Amplitude')
# plt.xlabel('Distance')
# plt.ylabel('Depth')
# plt.title('2D Seismic Line Visualization')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data
# Load the data
file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/NRCAN_Laurentian_Basin/Export/Seis/output.csv'
data = pd.read_csv(file_path, header=None)

# Verify the content of the data
print(data.head())

# Extract distance and amplitude values
distances = data.iloc[:, 0]
amplitudes = data.iloc[:, 1:].values

# Create a 2D grid
depths = np.arange(amplitudes.shape[1])

# Rotate the image by 90 degrees
amplitudes_rotated = np.rot90(amplitudes)

# Plot the data with improved contrast and color map
plt.figure(figsize=(12, 8))
plt.imshow(amplitudes_rotated, aspect='auto', cmap='seismic', extent=[depths.min(), depths.max(), distances.min(), distances.max()], vmin=-np.max(amplitudes), vmax=np.max(amplitudes))
plt.colorbar(label='Amplitude')
plt.title('2D Seismic Section')
plt.xlabel('Depth')
plt.ylabel('Distance')
plt.gca().invert_yaxis()  # Invert the y-axis to have depth increasing downwards
plt.axis('off')  # Turn off the axis
plt.show()