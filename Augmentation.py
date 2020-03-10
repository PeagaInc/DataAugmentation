from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

import aug_brightness
import aug_flip
import aug_rotate
import aug_shear
import aug_shift

imgname = "Test"

class Augmentation:
    def Augmentation():
        for i in range(1):
            img = load_img('./'+imgname+'/'+imgname+str(i+1)+'.jpg')
            img = img_to_array(img)
            data = expand_dims(img, 0)
            aug_brightness.aug_brightness(data,imgname+str(i))
            aug_rotate.aug_rotate(data,imgname+str(i))
            aug_shear.aug_shear(data,imgname+str(i))
            aug_shift.aug_shift(data,imgname+str(i))
