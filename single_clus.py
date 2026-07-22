import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

data = [[0], [3], [6], [9], [11]]

Z = linkage(data, method='single')

print("Linkage Matrix:")
print(Z)

plt.figure(figsize=(6,4))
dendrogram(Z, labels=['0','3','6','9','11'])
plt.title("Single Linkage Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()