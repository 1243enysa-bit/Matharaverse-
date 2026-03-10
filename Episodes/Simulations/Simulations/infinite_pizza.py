import matplotlib.pyplot as plt

# Number of slices
n_slices = 10  

# Initial pizza slice size
slice_size = 1  

# Store positions and sizes
sizes = []
positions = []

current_position = 0

# Compute slices
for i in range(n_slices):
    sizes.append(slice_size)
    positions.append(current_position)
    current_position += slice_size
    slice_size /= 2  # each slice is half of the previous

# Plot rectangles representing pizza slices
plt.figure(figsize=(10,2))
for i in range(n_slices):
    plt.barh(0, sizes[i], left=positions[i], height=0.5, color='orange', edgecolor='black')

# Labels
plt.title("Infinite Pizza: Geometric Series Approaching 2")
plt.yticks([])
plt.xlabel("Pizza slices")
plt.xlim(0, 2)  # Shows series approaching 2
plt.show()
