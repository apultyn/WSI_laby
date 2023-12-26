import mnist
import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
            condition = y_[image] * (
                np.dot(train_images[image], self.weights) - self.bias) >= 1
            if condition:
                self.weights -= self.learning_rate * (
                    2 * self.lambda_param * self.weights)
            else:
                self.weights -= self.learning_rate * (
                    2 * self.lambda_param * self.weights - np.dot(
                        train_images[image], y_[image])
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
        accuracies = []
        for i in range(epochs):
            for class_label in unique_classes:
                binary_labels = np.where(train_labels == class_label, 1, -1)
                if class_label in self.classifiers:
                    svm = self.classifiers[class_label]
                else:
                    svm = SVM(learning_rate, lambda_param)
                svm.train(train_images, binary_labels)
                self.classifiers[class_label] = svm
            accuracy = self.evaluate(test_images, test_labels)
            print(f"Accuracy for epoch {i}: {accuracy}")
            accuracies.append(accuracy)
        return accuracies

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
        confusion_mat = confusion_matrix(test_labels,
                                         y_pred, labels=np.unique(test_labels))
        return confusion_mat

    def plot_accuracy(self, accuracies):
        plt.plot(range(1, len(accuracies) + 1), accuracies, marker='o')
        plt.title('Accuracy Over Epochs')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.grid(True)
        plt.savefig('results/accuracy_plot.pdf')
        plt.show()

    def plot_confusion_matrix(self, test_images, test_labels):
        predictions = []
        for i in range(len(test_images)):
            pred_class = self.predict(test_images[i])
            predictions.append(pred_class)
            print(f"Creating confusion matrix - image {i} ")

        true_labels = test_labels
        cm = confusion_matrix(true_labels, predictions)
        cm_percentage = (cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100)

        plt.figure(figsize=(15, 6))

        plt.subplot(1, 2, 1)
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                    xticklabels=np.arange(10),
                    yticklabels=np.arange(10))
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.title("Confusion Matrix (Counts)")

        plt.subplot(1, 2, 2)
        sns.heatmap(cm_percentage, annot=True, fmt=".2f", cmap="Blues",
                    xticklabels=np.arange(10),
                    yticklabels=np.arange(10))
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.title("Confusion Matrix (Percentage)")

        plt.tight_layout()
        plt.savefig("results/confusion_matrix.pdf")


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
    accuracies = multiclass_svm.train(train_images,
                                      train_labels, test_images,
                                      test_labels, epochs,
                                      learning_rate, lambda_param)
    multiclass_svm.plot_accuracy(accuracies)

    multiclass_svm.plot_confusion_matrix(test_images, test_labels)


if __name__ == "__main__":
    main(sys.argv)
