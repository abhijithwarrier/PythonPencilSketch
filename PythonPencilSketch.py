# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI APPLICATION TO CONVERT THE USER SELECTED IMAGE INTO PENCIL SKETCH USING THE cv2 MODULE.

# OpenCV-Python is a library of Python bindings designed to solve computer vision problems. OpenCV-Python makes use of
# Numpy, which is a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array
# structures are converted to and from Numpy arrays. This also makes it easier to integrate with other libraries that
# use Numpy such as SciPy and Matplotlib.
#
# The module can be installed using the command - pip install opencv-python

# Importing necessary packages
import os
import cv2
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    root.feedlabel = Label(root, bg="mediumorchid4", fg="white", text="SELECTED IMAGE", font=('Comic Sans MS',20))
    root.feedlabel.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    root.selectImageLabel = Label(root, bg="mediumorchid4", borderwidth=3, relief="groove")
    root.selectImageLabel.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    root.selectImageEntry = Entry(root, width=55, textvariable=imagePath)
    root.selectImageEntry.grid(row=3, column=1, padx=10, pady=10)

    root.browseButton = Button(root, width=10, text="BROWSE", command=imageBrowse)
    root.browseButton.grid(row=3, column=2, padx=10, pady=10)

    root.previewlabel = Label(root, bg="mediumorchid4", fg="white", text="SKETCH IMAGE", font=('Comic Sans MS',20))
    root.previewlabel.grid(row=1, column=4, padx=10, pady=10, columnspan=2)

    root.previewImageLabel = Label(root, bg="mediumorchid4", borderwidth=3, relief="groove")
    root.previewImageLabel.grid(row=2, column=4, padx=10, pady=10, columnspan=2)

    root.convertButton = Button(root, width=10, text="SKETCH", command=convertImageIntoCartoon)
    root.convertButton.grid(row=3, column=4, padx=10, pady=10, columnspan=2)

    imageView = Image.open("/Users/abhijithwarrier/Pictures/RandomImage.png")
    imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
    imageDisplay = ImageTk.PhotoImage(imageResize)
    root.selectImageLabel.config(image=imageDisplay)
    root.selectImageLabel.photo = imageDisplay
    root.previewImageLabel.config(image=imageDisplay)
    root.previewImageLabel.photo = imageDisplay

def imageBrowse():
    # Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in destinationDirectory
    # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
    openDirectory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH")
    # Displaying the directory in the directory textbox
    imagePath.set(openDirectory)
    # Opening saved image using the open() of Image class which takes saved image as argument
    imageView = Image.open(openDirectory)
    # Resizing the image using Image.resize()
    imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.selectImageLabel.config(image=imageDisplay)
    # Keeping a reference
    root.selectImageLabel.photo = imageDisplay

# Defining Capture() to capture and save the image and display the image in the imageLabel
def convertImageIntoCartoon():
    # Loading the image from the specified file
    image = cv2.imread(imagePath.get())
    # Converting the image into Pencil Sketch using the cv2.pencilSketch() method.
    # 4 Parameters are passed - Input Image, sigma_s, sigma_r, shade_factor
    # sigma_s, sigma_r: Sigma_s and sigma_r are smoothing parameter.
    # shade_factor: is a simple factor that controls the intensity of product image.
    # There are two outputs, one is the result of applying the filter to the color input image,
    # and the other is the result of applying it to the grayscale version of the input image
    gray_img, color_img = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
    # Fetching and storing the selected image path
    new_image_path = os.path.dirname(os.path.abspath(imagePath.get())) + "/"
    # Fetching only the name of the selected image without extentsion from the complete path and
    # concatenating the name with keyword _pencilsketech and .jpeg extension
    new_image_name = os.path.splitext(imagePath.get().split('/')[-1])[0] + "_pencilsketch.jpeg"
    # Storing the complete new image name with path
    complete_image_path_name = new_image_path + new_image_name
    # Saving the pencil sketch image with the above name in the same location of original image
    cv2.imwrite(complete_image_path_name, gray_img)
    # Opening the new saved image using open() of Image class which takes saved image as argument
    imageView = Image.open(complete_image_path_name)
    # Resizing the image using Image.resize()
    imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.previewImageLabel.config(image=imageDisplay)
    # Keeping a reference
    root.previewImageLabel.photo = imageDisplay


# Creating object of tk class
root = tk.Tk()
# Setting the title, window size, background color and disabling the resizing property
root.title("PythonPencilSketch")
root.geometry("1340x640")
root.resizable(False, False)
root.configure(background = "mediumorchid4")
# Creating tkinter variables
imagePath = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
