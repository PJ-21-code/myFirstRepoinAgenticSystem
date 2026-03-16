import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

epochs= np.array(range(1,11))
loss= np.array([0.9,0.85,0.83,0.76,0.72,0.70,0.64,0.56,0.52,0.47])

plt.figure(figsize=(14,4))

plt.subplot(1,3,1)
plt.plot(loss,epochs,marker='s',color='red',markerfacecolor='black')
plt.grid(True)
plt.xlabel("Training losses")
plt.ylabel("No of iterations")
plt.title("loss vs epoch graph")

plt.subplot(1,3,2)
plt.scatter(epochs,loss)
plt.xlabel("epochs")
plt.ylabel("Losses made by model")
plt.title("loss vs epoch graph")

data= {
    "model": ["model_A","model_B","model_C"],
    "accuracy": [0.85,0.90,0.88]
}
df= pd.DataFrame(data)

plt.subplot(1,3,3)
plt.bar(df["model"],df["accuracy"],color= "green")
plt.xlabel("models")
plt.ylabel("Accuracy")
plt.title("Accuracy bar chart")
plt.show()
