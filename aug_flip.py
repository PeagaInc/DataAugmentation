from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
from cv2 import cv2

def aug_flip(data, filename):
	# Dinh nghia 1 doi tuong Data Generator voi bien phap chinh sua anh lat ngang doc
	myImageGen = ImageDataGenerator(horizontal_flip=True, vertical_flip=True)
	# Batch_Size= 1 -> Moi lan sinh ra 1 anh
	gen = myImageGen.flow(data, batch_size=1)
	# Sinh ra 9 anh va hien thi len man hinh
	for i in range(9):
		myBatch = gen.next()
		image = myBatch[0].astype('uint8')
		cv2.imwrite(str(filename)+'flip'+str(i+1)+'.png', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))