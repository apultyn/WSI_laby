import numpy as np
import time
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import sys
import json


class NeuralNetwork:
    def __init__(self, sizes, epochs, learning_rate):
        self.sizes = sizes
        self.epochs = epochs
        self.learning_rate = learning_rate

        input_layer = sizes[0]
        hidden_1 = sizes[1]
        hidden_2 = sizes[2]
        output_layer = sizes[3]

        self.params = {
            "W1": (np.random.randn(hidden_1, input_layer) *
                   np.sqrt(1. / hidden_1)),
            "W2": (np.random.randn(hidden_2, hidden_1) *
                   np.sqrt(1. / hidden_2)),
            "W3": (np.random.randn(output_layer, hidden_2) *
                   np.sqrt(1. / output_layer))
        }

    def forward_pass(self, x_train):
        params = self.params
        params["A0"] = x_train

        # input to hidden 1
        params["Z1"] = np.dot(params["W1"], params["A0"])
        params["A1"] = self.sigmoid(params["Z1"])

        # input to hidden 2
        params["Z2"] = np.dot(params["W2"], params["A1"])
        params["A2"] = self.sigmoid(params["Z2"])

        # hidden 2 to output
        params["Z3"] = np.dot(params["W3"], params["A2"])
        params["A3"] = self.softmax(params["Z3"])

        return params["A3"]

    def backward_pass(self, y_train, output):
        params = self.params

        change_w = {}

        # calculate W3 update
        error = (2 * (output - y_train) /
                 output.shape[0] * self.d_softmax(params["Z3"]))
        change_w["W3"] = np.outer(error, params["A2"])

        # calculate W2 update
        error = np.dot(params["W3"].T, error) * self.d_sigmoid(params["Z2"])
        change_w["W2"] = np.outer(error, params["A1"])

        # calculate W1 update
        error = np.dot(params["W2"].T, error) * self.d_sigmoid(params["Z1"])
        change_w["W1"] = np.outer(error, params["A0"])

        return change_w

    def update_weights(self, change_w):
        for key, val in change_w.items():
            self.params[key] -= self.learning_rate * val

    def train(self, train_list, train_labels, test_list, test_labels):
        start_time = time.time()
        accuracies = []
        for epoch in range(self.epochs):
            for i in range(len(train_list)):
                output = self.forward_pass(train_list[i])
                change_w = self.backward_pass(train_labels[i], output)
                self.update_weights(change_w)
                print(f"Epoch: {epoch + 1} Image {i}")
            accuracy = self.compute_accuracy(test_list, test_labels)
            accuracies.append(accuracy)
        print(f"Training time: {time.time() - start_time}")
        plt.plot(range(1, self.epochs + 1), accuracies, marker='o')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.title('Accuracy During Training')
        plt.savefig("results/accuracy.pdf")
        plt.show()

    def compute_accuracy(self, test_list, test_labels):
        predictions = []
        for i in range(len(test_list)):
            output = self.forward_pass(test_list[i])
            pred = np.argmax(output)
            predictions.append(pred == np.argmax(test_labels[i]))
            print(f"Evaling accuracy - test image {i}")
        return np.mean(predictions)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def d_sigmoid(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def softmax(self, x):
        exps = np.exp(x - x.max())
        return exps / np.sum(exps, axis=0)

    def d_softmax(self, x):
        exps = np.exp(x - x.max())
        return exps / np.sum(exps, axis=0) * (1-exps / np.sum(exps, axis=0))

    def results(self, matrix, number):
        tp = matrix[number][number]
        fptp = sum(matrix[number])
        tntp = 0
        for i in range(10):
            tntp += matrix[i][number]

        precision = round(tp / fptp, 2) if fptp != 0 else 0
        recall = round(tp / tntp, 2) if tntp != 0 else 0
        f1_score = (round(2 / ((1 / (tp / fptp)) + (1 / (tp / tntp))), 2)
                    if fptp != 0 and tntp != 0 else 0)

        return {
            "number": number,
            "precision": precision,
            "recall": recall,
            "f1-score": f1_score
        }

    def confusion_matrix(self, test_images, test_labels):
        predictions = []
        for i in range(len(test_images)):
            output = self.forward_pass(test_images[i])
            pred = np.argmax(output)
            predictions.append(pred)
            print(f"Creating confusion matrix - image {i} ")

        true_labels = np.argmax(test_labels, axis=1)
        cm = confusion_matrix(true_labels, predictions)
        cm_percentage = (cm.astype('float') /
                         cm.sum(axis=1)[:, np.newaxis] * 100)

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

        dict = []
        for i in range(10):
            dict.append(self.results(cm, i))
        json_filename = 'results/results.json'
        with open(json_filename, 'w') as json_file:
            json.dump(dict, json_file, indent=4)


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("layer_1_size")
    parser.add_argument("layer_2_size")
    parser.add_argument("epochs")
    parser.add_argument("learning_rate")
    args = parser.parse_args(arguments[1:])

    layer_1_size = int(args.layer_1_size)
    layer_2_size = int(args.layer_2_size)
    epochs = int(args.epochs)
    learning_rate = float(args.learning_rate)

    ((train_images, train_labels),
     (test_images, test_labels)) = mnist.load_data()

    # train_images = train_images[:1000]
    # train_labels = train_labels[:1000]
    # test_images = test_images[:100]
    # test_labels = test_labels[:100]

    train_images = train_images.reshape((len(train_images), -1)) / 255
    test_images = test_images.reshape((len(test_images), -1)) / 255

    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)

    nn = NeuralNetwork([784, layer_1_size, layer_2_size, 10],
                       epochs, learning_rate)
    nn.train(train_images, train_labels, test_images, test_labels)
    nn.confusion_matrix(test_images, test_labels)


if __name__ == "__main__":
    main(sys.argv)
