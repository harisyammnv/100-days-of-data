import tensorflow as tf
import numpy as np
from tensorflow import keras


class LinearNN:

    def __init__(self, num_units: int, input_shape: int):
        self.num_units = num_units
        self.input_shape = input_shape

    def build_model(self):
        model = tf.keras.Sequential([keras.layers.Dense(units=self.num_units, input_shape=[self.input_shape])])
        return model


lnn = LinearNN(1, 1)
linear_model = lnn.build_model()

linear_model.compile(optimizer='sgd', loss='mean_squared_error')

xx = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
yx = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)


linear_model.fit(x=xx, y=yx, epochs=500)

print(linear_model.predict([10.0]))
