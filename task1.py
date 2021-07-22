import cv2 as cv
import matplotlib.pyplot as plt


class A:
    def __init__(self):
        pass

    def object(self, image):
        image = cv.imread(image, 0)
        (thresh, black) = cv.threshold(image, 80, 255, cv.THRESH_BINARY_INV)

        color = {"white": 0, "black": 0}

        for i in black:
            for a in i:
                if a == 255:
                    color["white"] +=1
                else:
                    color["black"] += 1

        if color["white"] > color["black"]:
            balance = 256 / (int(color["white"] / color["black"]))
        else:
            balance = 256 / (int(color["black"] / color["white"]))

        if balance < 80:
            balance = 127

        if color["black"] > color["white"]:
            (thresh, black) = cv.threshold(image, balance, 255, cv.THRESH_BINARY)
        else:
            (thresh, black) = cv.threshold(image, balance, 255, cv.THRESH_BINARY_INV)

        cv.imwrite('black_image.jpg', black)

        image = cv.imread('black_image.jpg')

        plt.figure(num='Task 1')
        plt.axis("off")
        plt.imshow(image)

        return image
