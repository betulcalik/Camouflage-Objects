import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image
from task1 import A
from task2 import B
from task3 import C

# original picture
image = cv.imread('Images/leaf.jpeg')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# show original picture
plt.figure(num='Original Picture')
plt.axis("off")
plt.imshow(image)

# show task 1 : detect object
classA = A()
classA.object('Images/leaf.jpeg')

# show task 2 : dominant colours
classB = B()
image = image.reshape((image.shape[0] * image.shape[1], 3))
kmeans = KMeans(n_clusters=5)
kmeans.fit(image)

histogram = classB.centroid_histogram(kmeans)
bar = classB.plot_colors(histogram, kmeans.cluster_centers_)
plt.figure(num='Task 2')
plt.axis("off")
plt.imshow(bar)

# show task 3
classC = C()
classC.plot_colors(histogram, kmeans.cluster_centers_)

# show task 4
image1 = Image.open('Images/leaf.jpeg')
image2 = Image.open('pattern.png').resize(image1.size)

mask = Image.open('black_image.jpg').resize(image1.size)
composite = Image.composite(image1, image2, mask)

plt.figure(num='Task 4')
plt.axis("off")
plt.imshow(composite)

plt.show()
