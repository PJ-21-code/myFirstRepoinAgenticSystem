import numpy as np

data= np.array([23,34,56,78])

mean= np.mean(data)
std= np.std(data)
normalized_data= (data-mean)/std

print(f"Original Data: {data}")
print(f"Mean: {mean}")
print(f"Standard deviation: {std}")
print(f"Normalized data: {normalized_data}")

n_data_re= normalized_data.reshape((2,2))

print(f"Reshape: {n_data_re.shape}")
print(f"Reshaped normalized data: {n_data_re}")