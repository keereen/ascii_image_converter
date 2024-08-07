from PIL import Image

class ImageAsciifier:
    def __init__(self, image):
        # Grayscale from dark to light ascii characters I found on Stack Overflow
        characters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/()1[]?-_+~<>i!lI;:,^`'. "
        characters = characters[::-1] # invert the colours
        self.characterList = list(characters)
        self.image = image
        #print(self.characterList)

    # Resize the image
    def resizeImage(self, image, imageWidth = 100):
        width, height = image.size
        ratio = height / width
        imageHeight = int(imageWidth * ratio)
        resizedImage = image.resize((imageWidth, imageHeight))
        return resizedImage

    # Turn an image to greyscale
    def greyImage(self, image):
        greyscaleImage = image.convert("L")
        return greyscaleImage

    # Turn the pixels in the image to an ascii character
    def pixelsToAscii(self, image, characterList):
        pixels = image.getdata()
        characters = "".join([characterList[pixel//25] for pixel in pixels]) # List comprehension
        return characters

    def formatCharacters(self, unformattedCharacters, imageWidth = 100):
        pixel_count = len(unformattedCharacters)
        formattedCharacterList = [unformattedCharacters[i:i+imageWidth] for i in range(0, len(unformattedCharacters), imageWidth)]
        formattedCharacters = ''

        for line in formattedCharacterList:
            formattedCharacters += line + '\n'
            
        return formattedCharacters

    def imageAsciify(self, imageWidth = 100):
        
        image = self.image

        # start asciification
        rezisedImage = self.resizeImage(image, imageWidth)
        greyscaleImage = self.greyImage(rezisedImage)
        unformattedCharacters = self.pixelsToAscii(greyscaleImage, self.characterList)

        finalAscii = self.formatCharacters(unformattedCharacters)
        return finalAscii

# open the image
image = Image.open('cat.png')
#print(image)
imageAsciifier = ImageAsciifier(image)
print(imageAsciifier.imageAsciify())


# branch test



