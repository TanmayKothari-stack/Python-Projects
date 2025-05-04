from PIL import Image,ImageTk

image = Image.open('car.jpg')
image = (image)
image.save('car_images/car.jpg')
print(image)