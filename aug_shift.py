from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
from cv2 import cv2

def aug_shift(data, filename):
	# Dinh nghia 1 doi tuong Data Generator voi bien phap chinh sua anh dieu chinh do sang tu 0.5% den 2.0%
	myImageGen = ImageDataGenerator(width_shift_range=[-150,150])
	# Batch_Size= 1 -> Moi lan sinh ra 1 anh
	gen = myImageGen.flow(data, batch_size=1)
	# Sinh ra 9 anh va hien thi len man hinh
	for i in range(9):
		myBatch = gen.next()
		image = myBatch[0].astype('uint8')
		cv2.imwrite(str(filename)+'shift'+str(i+1)+'.png', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))