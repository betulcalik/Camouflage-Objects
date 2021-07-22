import cv2 as cv
import numpy as np


class B:
    def __init__(self):
        pass

    def centroid_histogram(self, kmeans):
        numLabels = np.arange(0, len(np.unique(kmeans.labels_)) + 1)
        (hist, _) = np.histogram(kmeans.labels_, bins=numLabels)

        hist = hist.astype("float")
        hist /= hist.sum()

        return hist

    def plot_colors(self, hist, centroids):
        bar = np.zeros((50, 300, 3), dtype="uint8")
        startX = 0

        for(percent, color) in zip(hist, centroids):
            endX = startX + (percent * 300)
            cv.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)

            startX = endX

        return bar