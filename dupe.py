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





import os



print(os.getcwd())


def reSize(file):
    filename = file
    dW = 450
    dH = 600
    rW = 3
    rH = 4
    
    path = "Downloads/AppChallenge2019-master/AppChallenge2019-master/Training Images/inputs/stuffs/image" + filename + ".jpg"
    image_case = open_image(path)
        
        
    w, h = image_case.size
    print("Old W: " + str(w) + "\nOld H: " + str(h))
    #image_case = image_case.resize( ( ((w-w%450)/450), ((h-h%600)/600) ), resample=0 )
    
    #print("Old W: " + str(w) + "\nOld H: " + str(h))
    if w>h:
        #image_case = image_case.crop((0,0,(w-w%4),(h-h%3)))
        image_case = (image_case.rotate(90))
    #elif h>w:
        #image_case = image_case.crop((0,0,(w-w%450),(h-h%600)))
    #else:
        #pass #square
        
    w, h = image_case.size
    print("New W: " + str(w) + "\nNew H: " + str(h))
    
    if (dW>w and dH>h):
        image_case = image_case.crop((0,0,(w-w%rW),(h-h%rH)))
    w, h = image_case.size
    print("Newer W: " + str(w) + "\nNewer H: " + str(h))
    
    
    image_case = image_case.resize( (dW,dH), resample=0 )
    #w, h = image_case.size
    #print("Super W: " + str(w) + "\nSuper H: " + str(h))
    
    save_image(  image_case,"Downloads/AppChallenge2019-master/AppChallenge2019-master/Training Images/outputs/stuffs/" + filename + ".jpg"   )
    
    """
    jpg = 1
    
    if jpg == 1:
        print("So saving as jpg")
        save_image(  image_case,"Downloads/AppChallenge2019-master/AppChallenge2019-master/Training Images/outputs/stuffs/" + filename + ".jpg"   )
    else:
        print("haha jfif")
        save_image(  image_case,"Downloads/AppChallenge2019-master/AppChallenge2019-master/Training Images/outputs/stuffs/" + filename + ".jfif"  )
    """                             
                                                                            
                                                                                                                     
                                                                                                                                                                                                       


"""
for i in range(71):
    try:
        reSize(str(i))
    except:
        print("Failed picture " + str(i) + ".")
"""
reSize("1")

print("Completed images.")
