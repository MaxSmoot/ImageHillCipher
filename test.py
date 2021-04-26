import ImageManip as IManip
import numpy as np
from PIL import Image

image = Image.open("58.jpg")
imagepixels = np.array(image)

print(imagepixels.shape)
print(imagepixels)
print(IManip.padImage(imagepixels))

padded = Image.fromarray(IManip.padImage(imagepixels))
padded.save("padded.jpg")
