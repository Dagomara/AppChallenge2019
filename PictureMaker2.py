from PIL import *
from PIL import Image
#functions provided by codementor.io, but I had to edit them for our cause

# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  #add the dynamic resizer from stackoverflow.com/questions/10607468/how-to-reduce-the-image-file-size-using-pil
  image.save(path, optimize=True, quality=85)

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

# Create a Grayscale version of the image
def convert_picture(image, color):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to grayscale
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Set Pixel in new image
      if color == "r":
        pixels[i, j] = (red, 0, 0)
      elif color == "g":
        pixels[i, j] = (0, green, 0)
      elif color == "b":
        pixels[i,j] = (0,0,blue)

    # Return new image
  return new
def combine_pictures_check(image, image2, image3):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to grayscale
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = get_pixel(image2, i, j)[1]
      blue =  get_pixel(image3, i, j)[2]

      # Set Pixel in new image
      pixels[i,j] = (red, green, blue)

    # Return new image
  return new

"""
Pollock = open_image("Training Images/jackson20pollock.png")
convertedPollock = convert_picture(Pollock, "r")
save_image(convertedPollock, "Training Images\pollockRed.png")
"""
import os

def mkRGB(file):
  filename = file
  path = "Training Images/inputs/" + filename + ".jpg" #input("Image path? ")
  image_case = open_image(path)

  os.mkdir(("Training Images/outputs/" + filename))

  save_image(convert_picture(image_case, "r"),("Training Images/outputs/" + filename + "/r.jpg"))
  save_image(convert_picture(image_case, "g"),("Training Images/outputs/" + filename + "/g.jpg"))
  save_image(convert_picture(image_case, "b"),("Training Images/outputs/" + filename + "/b.jpg"))

  print("File " + filename + " created")

def sizeImages(file):
    filename = file
    path = "Training Images/inputs/" + filename + ".jpg"
    image_case = open_image(path)
    width, height = image_case.size
    if width > height:
        fixedWidth = (width - (width%4))
        fixedHeight = (height - (height%3))
        image_case = image_case.crop( (0, 0, fixedWidth, fixedHeight) )
        width, height = image_case.size
        image_case_2 = image_case.resize(( (150 * (width/4)),(150 * (height/3))) )
    elif height > width:
        image_case = image_case.crop( (width - (width%3)), (height - (height%4)) )
        width, height = image_case.size
        image_case_2 = image_case.resize(( (150 * (width/3)),(150 * (height/4))) )
    else:
        image_case_2 = image_case.resize(512, 512)
    save_image( (image_case_2), ("Training Images/outputs/" + filename + "_scaled.jpg") )
    #image_case_2.save(path, optimize=True, quality=85)

#test image code
    #x = combine_pictures_check( (open_image("Training Images\\" + filename + "_r.png")), (open_image("Training Images\\" + filename + "_g.png")), (open_image("Training Images\\" + filename + "_b.png")) )
    #save_image(x, ("Training Images\\" + filename + "_concat.png"))

sizeImages(str(8))
for i in range(3):
    try:
        sizeImages(str(i)) #used to be makePictures()
    except:
        print("Failed picture " + str(i) + ".")

print("Completed images.")
