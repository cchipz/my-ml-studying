import matplotlib.pyplot as plt
from sklearn import datasets
# Load the MNIST SET dataset
digit_dataset = datasets.load_digits()
# print(digit_dataset.images.shape)
# print(digit_dataset.images[9])
print(digit_dataset.target[0])

plt.imshow(digit_dataset.images[0], cmap=plt.get_cmap('gray'))
plt.show()
