from PIL import Image
import os

size = 970, 1296
oldimages = 'images'
count = 0

for path in os.listdir(oldimages):
    # check if current path is a file
    if os.path.isfile(os.path.join(oldimages, path)):
        count += 1
print('File count:', count)

for num in range(count):
    im = Image.open("images/light{num}.jpg".format(num = num+91))
    img = im.rotate(0, expand=True)
    im_resized = img.resize(size)
    im_resized.save("new_images/light{num}.jpg".format(num = num+33), "JPEG")

