"""
Author: Do Minh Quang
Date: 29/01/1997
Program: project_05_page_241.py
Problem:
5. Define and test a function named posterize. This function expects an image
and a tuple of RGB values as arguments. The function modifies the image like the
blackAndWhite function, but it uses the given RGB values instead of black.
Solution:


"""
from images import Image

def posterize(image, color=(0, 0, 0)):
    """Converts a color image to two-colors,
    one of which it white and the other of which is
    either a default of black or a user-specified
    RGB value."""
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, color)
            else:
                image.setPixel(x, y, whitePixel)

def main():
    filename = input("Enter the image file name: ")
    red = int(input("Enter an integer [0..255] for red: "))
    green = int(input("Enter an integer [0..255] for green: "))
    blue = int(input("Enter an integer [0..255] for blue: "))
    image = Image(filename)
    posterize(image, (red, green, blue))
    image.draw()

main()
