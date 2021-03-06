import cv2
import urllib3
import numpy as np

print("Computer Vision Verion is: " + cv2.__version__)

# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    image = np.asarray(bytearray(r.data), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image

# initialize the list of image URLs to work with
urls = [
    "https://affoodie73427.blob.core.windows.net/photos/fabianheadshotprof.png",
    "https://affoodie73427.blob.core.windows.net/photos/FabianW.png"
]
# loop over the image URLs
for url in urls:
    # download the image URL and display it
    print("downloading %s" % (url))
    image = url_to_image(url)
    cv2.imshow('Image', image)
    cv2.waitKey(5000)
