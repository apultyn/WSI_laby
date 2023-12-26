import mnist
import argparse
import sys
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score


class SVM:
    def __init__(self, epochs=50, learning_rate=0.001, lambda_param=0.01):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.lambda_param = lambda_param
        self.weights = None
        self.bias = None

    def train(self, X, y, class_label):
        n_samples, n_features = X.shape
        y_ = np.where(y <= 0, -1, 1)

        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.epochs):
            for image in range(n_samples):
                condition = y_[image] * (np.dot(X[image], self.weights) - self.bias) >= 1
                if condition:
                    self.weights -= self.learning_rate * (2 * self.lambda_param * self.weights)
                else:
                    self.weights -= self.learning_rate * (
                        2 * self.lambda_param * self.weights - np.dot(X[image], y_[image])
                    )
                    self.bias -= self.learning_rate * y_[image]
                print(f"Label {class_label}, epoch {epoch}, image {image}")

    def predict(self, X):
        linear_output = np.dot(X, self.weights) - self.bias
        return np.sign(linear_output)

    def evaluate(self, X, y):
        y_pred = self.predict(X)
        accuracy = np.mean(y_pred == y)
        print("Accuracy:", accuracy)


class MulticlassSVM:
    def __init__(self, epochs=100, learning_rate=0.001, lambda_param=0.01):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.lambda_param = lambda_param
        self.classifiers = {}  # Dictionary to store binary classifiers

    def train(self, X, y):
        unique_classes = np.unique(y)

        for class_label in unique_classes:
            # Convert to binary classification (class vs. rest)
            binary_labels = np.where(y == class_label, 1, -1)

            # Train a binary classifier for the current class
            svm = SVM(self.epochs, self.learning_rate, self.lambda_param)
            svm.train(X, binary_labels, class_label)
            self.classifiers[class_label] = svm

    def predict(self, X):
        class_scores = {}

        for class_label, svm in self.classifiers.items():
            class_scores[class_label] = svm.predict(X)

        # Choose the class with the highest decision function output
        predicted_class = max(class_scores, key=lambda k: class_scores[k])

        return predicted_class

    def evaluate(self, X, y):
        y_pred = np.array([self.predict(sample) for sample in X])
        accuracy = accuracy_score(y, y_pred)
        print("Accuracy:", accuracy)

        # Create and print the confusion matrix with labels
        confusion_mat = confusion_matrix(y, y_pred, labels=np.unique(y))
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

    # train_images = train_images[:1000]
    # train_labels = train_labels[:1000]
    # test_images = test_images[:100]
    # test_labels = test_labels[:100]



    multiclass_svm = MulticlassSVM(epochs, lambda_param, learning_rate)
    multiclass_svm.train(train_images, train_labels)
    multiclass_svm.evaluate(test_images, test_labels)

    unique_labels, label_counts = np.unique(test_labels, return_counts=True)
    print("Tests:")
    for label, count in zip(unique_labels, label_counts):
        print(f"Label {label}: {count} occurrences")


if __name__ == "__main__":
    main(sys.argv)
