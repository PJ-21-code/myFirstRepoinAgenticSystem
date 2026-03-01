import numpy as np

np.random.seed(42)
x= np.random.randint(1,101,(100,2))
mean_data= x.mean(axis=0)
std_data= x.std(axis=0)

normalize_data= (x-mean_data)/std_data
slicing_part= int(0.8*len(normalize_data))

train= normalize_data[:slicing_part]
test= normalize_data[slicing_part:]

print(f"Original data shape: {x.shape}")
print(f"Mean shape: {mean_data.shape}")
print(f"Stardard deviation shape: {std_data.shape}")
print(f"Traing data shape: {train.shape}")
print(f"Testing data shape: {test.shape}")
print("Note: Modifying the slice affected the original array")
