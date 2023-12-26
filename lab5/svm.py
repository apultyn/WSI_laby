import mnist
import argparse
import sys
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score


class SVM:
    def __init__(self, learning_rate, lambda_param):
        self.learning_rate = learning_rate
        self.lambda_param = lambda_param
        self.weights = None
        self.bias = 0

    def train(self, train_images, train_labels):
        n_samples, n_features = train_images.shape
        y_ = np.where(train_labels <= 0, -1, 1)

        if self.weights is None:
            self.weights = np.zeros(n_features)

        for image in range(n_samples):
            condition = y_[image] * (np.dot(train_images[image], self.weights) - self.bias) >= 1
            if condition:
                self.weights -= self.learning_rate * (2 * self.lambda_param * self.weights)
            else:
                self.weights -= self.learning_rate * (
                    2 * self.lambda_param * self.weights - np.dot(train_images[image], y_[image])
                )
                self.bias -= self.learning_rate * y_[image]

    def predict(self, X):
        linear_output = np.dot(X, self.weights) - self.bias
        return np.sign(linear_output)


class MulticlassSVM:
    def __init__(self):
        self.classifiers = {}  # Dictionary to store binary classifiers

    def train(self, train_images, train_labels,
              test_images, test_labels,
              epochs, learning_rate=0.001, lambda_param=0.01):
        unique_classes = np.unique(train_labels)
        svm = None
        for i in range(epochs):
            for class_label in unique_classes:
                binary_labels = np.where(train_labels == class_label, 1, -1)
                if class_label in self.classifiers:
                    svm = self.classifiers[class_label]
                else:
                    svm = SVM(learning_rate, lambda_param)
                svm.train(train_images, binary_labels)
                self.classifiers[class_label] = svm
            print(f"Accuracy for epoch {i}: {self.evaluate(test_images, test_labels)}")

    def predict(self, image):
        class_scores = {}

        for class_label, svm in self.classifiers.items():
            class_scores[class_label] = svm.predict(image)

        predicted_class = max(class_scores, key=lambda k: class_scores[k])

        return predicted_class

    def evaluate(self, test_images, test_labels):
        y_pred = np.array([self.predict(sample) for sample in test_images])
        return accuracy_score(test_labels, y_pred)

    def confusion_matrix(self, test_images, test_labels):
        y_pred = np.array([self.predict(sample) for sample in test_images])
        confusion_mat = confusion_matrix(test_labels, y_pred, labels=np.unique(test_labels))
        print("Confusion Matrix:")
        print(confusion_mat)


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("epochs")
    parser.add_argument("lambda_param")
    parser.add_argument("learning_rate")
    args = parser.parse_args(arguments[1:])

    epochs = int(args.epochs)
    lambda_param = float(args.lambda_param)
    learning_rate = float(args.learning_rate)

    train_images = mnist.train_images()
    train_labels = mnist.train_labels()
    test_images = mnist.test_images()
    test_labels = mnist.test_labels()

    train_images = train_images.reshape(len(train_images), -1) / 255
    test_images = test_images.reshape(len(test_images), -1) / 255

    multiclass_svm = MulticlassSVM()
    multiclass_svm.train(train_images, train_labels, test_images,
                         test_labels, epochs, learning_rate, lambda_param)
    multiclass_svm.confusion_matrix(test_images, test_labels)

    unique_labels, label_counts = np.unique(test_labels, return_counts=True)
    print("Tests:")
    for label, count in zip(unique_labels, label_counts):
        print(f"Label {label}: {count} occurrences")


if __name__ == "__main__":
    main(sys.argv)
