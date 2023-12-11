import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

# Załaduj dane MNIST
(train_images, train_labels), _ = mnist.load_data()

# Przetwórz obraz
sample_image = train_images[0]
processed_image = sample_image.reshape((28, 28, 1)).astype('float32') / 255

# Wyświetl oryginalny i przetworzony obraz
plt.subplot(1, 2, 1)
plt.imshow(sample_image, cmap='gray')
plt.title('Oryginalny obraz')

plt.subplot(1, 2, 2)
plt.imshow(processed_image[:, :, 0], cmap='gray')
plt.title('Przetworzony obraz')

plt.show()
