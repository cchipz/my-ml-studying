from scipy.io import loadmat
#Use .mat file
import matplotlib.pyplot as plt

mnist_raw = loadmat("mnist-original.mat")

mnist ={
    'data':mnist_raw['data'].T,
    'target':mnist_raw['label'][0],
}

x,y = mnist['data'],mnist['target']
number = x[35000]
number_image = number.reshape(28,28)

print(y[35000])
plt.imshow(number_image, 
           cmap=plt.cm.binary,
           interpolation='nearest')
plt.show()