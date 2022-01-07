import tensorflow as tf
import numpy as np
from tensorflow import keras


class UserDefinedCallback(tf.keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.99:
            print('Reached 99% accuracy so cancelling training!')
            self.model.stop_training = True


def create_model():
    return tf.keras.Sequential([tf.keras.layers.Flatten(),
                                tf.keras.layers.Dense(256, activation=tf.nn.relu),
                                tf.keras.layers.Dense(10, activation=tf.nn.softmax)])


callbacks = UserDefinedCallback()

mnist = tf.keras.datasets.mnist
# obtains the dataset from the keras api
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# scales the images between 0 to 1
training_images = training_images/255.0
test_images = test_images/255.0

model = create_model()

model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x=training_images, y=training_labels, epochs=10, callbacks=[callbacks])

model.evaluate(x=test_images, y=test_labels)