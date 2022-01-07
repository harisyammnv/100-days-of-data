import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from pathlib import Path

class CNNUserDefinedCallback(tf.keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.95:
            self.model.stop_training = True


def create_model():
    return tf.keras.Sequential([tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(300, 300, 3)),
                                tf.keras.layers.MaxPool2D(2,2),
                                tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
                                tf.keras.layers.MaxPool2D(2, 2),
                                tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                tf.keras.layers.MaxPool2D(2, 2),
                                tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                tf.keras.layers.MaxPool2D(2, 2),
                                tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                                tf.keras.layers.MaxPool2D(2, 2),
                                tf.keras.layers.Flatten(),
                                tf.keras.layers.Dense(512, activation='relu'),
                                tf.keras.layers.Dense(1, activation='sigmoid')
                                ])


train_horse_images = Path.cwd()/'data'/'horses'
train_human_images = Path.cwd()/'data'/'humans'

validation_horse_images = Path.cwd()/'validation_data'/'horses'
validation_human_images = Path.cwd()/'validation_data'/'humans'

print(f"Number of training horse images: {len(list(train_horse_images.glob('*')))}")
print(f"Number of training human images: {len(list(train_human_images.glob('*')))}")

print(f"Number of validation horse images: {len(list(validation_horse_images.glob('*')))}")
print(f"Number of validation human images: {len(list(validation_human_images.glob('*')))}")

model = create_model()
model.summary()
model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.RMSprop(lr=0.001), metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1/255)
valid_datagen = ImageDataGenerator(rescale=1/255)

train_generator = train_datagen.flow_from_directory(
    directory=str(Path.cwd()/'data'),
    target_size=(300,300),
    batch_size=128,
    class_mode='binary'
)
valid_generator = valid_datagen.flow_from_directory(
    directory=str(Path.cwd()/'validation_data'),
    target_size=(300, 300),
    batch_size=32,
    class_mode='binary'
)

callbacks_user = CNNUserDefinedCallback()

history = model.fit_generator(train_generator, steps_per_epoch=8, epochs=15, verbose=1,
                              validation_data=valid_generator, validation_steps=8,callbacks=[callbacks_user])
