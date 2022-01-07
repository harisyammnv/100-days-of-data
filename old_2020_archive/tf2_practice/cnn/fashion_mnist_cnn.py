import tensorflow as tf
import numpy as np
from tensorflow import keras


class CNNUserDefinedCallback(tf.keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.95:
            self.model.stop_training = True


def create_model():
    return tf.keras.Sequential([tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu',
                                                       input_shape=(28, 28, 1)),
                                tf.keras.layers.MaxPool2D(2, 2),
                                tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu',
                                                       input_shape=(28, 28, 1)),
                                tf.keras.layers.MaxPool2D(2, 2),
                                tf.keras.layers.Flatten(),
                                tf.keras.layers.Dense(128, activation='relu'),
                                tf.keras.layers.Dense(10, activation='softmax')
                                ])


callbacks = CNNUserDefinedCallback()

fashion_mnist = tf.keras.datasets.fashion_mnist
# obtains the dataset from the keras api
(training_images, training_labels), (test_images, test_labels) = fashion_mnist.load_data()

# scales the images between 0 to 1
training_images = training_images.reshape(60000, 28, 28, 1)
training_images = training_images / 255.0
test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images / 255.0

model = create_model()

print(model.summary())

model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x=training_images, y=training_labels, epochs=40, callbacks=[callbacks])

model.evaluate(x=test_images, y=test_labels)