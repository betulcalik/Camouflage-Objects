import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from random import *


class C:
    def __init__(self):
        pass

    """
        def centroid_histogram(self, kmeans):
        numLabels = np.arange(0, len(np.unique(kmeans.labels_)) + 1)
        (hist, _) = np.histogram(kmeans.labels_, bins=numLabels)

        hist = hist.astype("float")
        hist /= hist.sum()

        return hist
    """

    def plot_colors(self, hist, centroids):
        patternWidth = 700
        patternHeight = 700

        image = np.zeros((patternWidth, patternHeight, 3), dtype="uint8")
        colorArray = []

        bar = np.zeros((50, 300, 3), dtype="uint8")
        startX = 0

        for(percent, color) in zip(hist, centroids):
            endX = startX + (percent * 300)
            cv.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)

            for i in range(int(endX) - int(startX)):
                colorArray.append(color.astype("uint8").tolist())

            startX = endX

        for a in range(patternHeight):
            for i in range(patternWidth):
                cv.rectangle(image, (int(i), a), (int(i + 1), a + 1), choice(colorArray), -1)

        plt.figure(num='Task 3')
        plt.axis("off")
        plt.imshow(image)

        plt.savefig('pattern.png')

        return bar