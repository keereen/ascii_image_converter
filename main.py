from PIL import Image

# Grayscale from dark to light ascii characters I found on Stack Overflow
characters = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,"^`'. """
characterList = list(characters)

#print(characterList)

# Open the image
image = Image.open('thumb_cat.jpg')

# Resize the image
def resizeImage(image, imageWidth):
    width, height = image.size
    ratio = height / width
    imageHeight = int(imageWidth * ratio)
    resizedImage = image.resize((imageWidth, imageHeight))
    return resizedImage

# Turn an image to greyscale
def greyImage(image):
    greyscaleImage = image.convert("L")
    return greyscaleImage

# Turn the pixels in the image to an ascii character
def pixelsToAscii(image, characterList):
    pixels = image.getdata()
    characters = "".join([characterList[pixel//15] for pixel in pixels]) # Code from the internet... for now
    return characters

imageWidth = 100
image = resizeImage(image, imageWidth)
image = greyImage(image)
unformattedCharacters = pixelsToAscii(image, characterList)
pixel_count = len(unformattedCharacters)
formattedImageList = [unformattedCharacters[i:i+imageWidth] for i in range(0, len(unformattedCharacters), imageWidth)]
formattedImage = ''

for line in formattedImageList:
    formattedImage += line + '\n'
    
print(formattedImage)



'''
todo: 
virtual environments and that [X]
decipher line 28 []
output a single string []
object orientify[]
save output to a file []
add any image as input []
'''

