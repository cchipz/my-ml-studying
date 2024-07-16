import pylab as pl
from sklearn import datasets
# Load the MNIST SET dataset
digit_dataset = datasets.load_digits()
# print(digit_dataset.images.shape)
# print(digit_dataset.images[9])
print(digit_dataset.target[0])

pl.imshow(digit_dataset.images[0], cmap=pl.cm.gray_r)
pl.show()
