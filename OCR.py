from keras.models import load_model
import tensorflow as tf
from keras.utils.generic_utils import CustomObjectScope

with CustomObjectScope({'softmax_v2': tf.nn.softmax}):    #Maybe due to mismatch between TF2.0 and keras
    model = load_model('Model.h5')