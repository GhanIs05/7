import numpy as np
# Define a square array (replace this with your own array)
square_array = np.array([[4, -2, 1],
[1, 1, 1],
[1, -2, 4]])
# Compute eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(square_array)
# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues.tolist())
# Print the right eigenvectors
print("\nRight Eigenvectors:")
print(eigenvectors)
