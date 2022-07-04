from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model = load_model('model/model1.h5')

model.make_predict_function()


dic = {0: 'blight', 1: 'common rust', 2: 'gray leaf spot', 3: 'healthy'}


def predict_label(img_path):
    i = image.load_img(img_path, target_size=(100,100))
    i = image.img_to_array(i)/255.0
    i = i.reshape(1,100,100,3)
    p = model.predict(i)
    p = np.argmax(p, axis=1)
    return dic[p[0]]