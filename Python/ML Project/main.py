import numpy as np
import pandas as pd
from keras.models import Sequential
from keras import layers
import time as t
from matplotlib import pyplot as plt
import tflearn
import gym
import tensorflow as tf

### Network class
class Network:
    # list w, empty
    w = []
    # list b, empty
    b = []
    # list activations, empty
    activations = []
    # alpha of .001 for ???
    alpha = 0.001

    # self in python is not a reference to the function itself, but the class
    # in this case, self references the class Network
    # function Relu(), takes x, returns np.maximum(0,x) (TYPE??? prob int or float)
    def Relu(self, x):
        return np.maximum(0, x)

    # function derRelu(), takes x, returns boolean
    def derRelu(self, x):
        return x > 0

    # function sigmoid(), takes x, returns integer
    def sigmoid(self, x):
        s = 1 / (1 + np.exp(-x))
        return s

    # function derSigmoid(), takes x, returns integer
    def derSigmoid(self, X):
        sigmoid = self.sigmoid(X)
        return sigmoid * (1 - sigmoid)

    # function error(), takes prediction and y, returns integer(?)
    def error(self, prediction, y):
        y = y.reshape(len(y), 1)
        e = (prediction - y) ** 2
        return e

    # function derError(), takes prediction and y, returns integer (?)
    def derError(self, prediction, y):
        y = y.reshape(len(y), 1)
        return prediction - y

    #
    activationFunctions = {
        "Relu": Relu,
        "sigmoid": sigmoid
    }

    #
    derivativeFunctions = {
        "Relu": derRelu,
        "sigmoid": derSigmoid
    }

    #
    def __init__(self, layerWeights, activations, alpha):

        for i in range(0, len(layerWeights) - 1):
            self.w.append(np.random.rand(layerWeights[i + 1], layerWeights[i])-0.5)
            self.b.append(np.random.rand(layerWeights[i + 1]).reshape(layerWeights[i + 1], 1)-0.5)
            self.activations = activations
            self.alpha = alpha

    #
    def feedforward(self, x):
        z = []
        a = []

        x = np.asarray(x)
        x = x.reshape(len(x), 1)

        # print(x.shape)

        z.append(np.matmul(self.w[0], x) + self.b[0])
        a.append(self.activationFunctions[self.activations[0]](self, z[0]))

        for i in range(1, len(self.w)):
            z.append(np.matmul(self.w[i], a[i - 1]) + self.b[i])
            a.append(self.activationFunctions[self.activations[i]](self, z[i]))

        #print(z)
        return z, a

    #
    def scalar_to_array(self, x):
        if np.squeeze(x).size == 1:
            return np.array([np.squeeze(x)])
        else:
            return x

    #
    def fit(self, X, y, epochs):

        for iterations in range(0, epochs):

            error = 0

            for i in range(0, len(X)):
                # print(X[i])
                # x = np.asarray(X[i])
                x = X[i].reshape(len(X[i]), 1)

                z, a = self.feedforward(x)

                a1_w1 = np.matmul(self.derSigmoid(z[1]), a[0].T)

                de = self.derError(a[1], y[i])

                self.w[1] += -self.alpha * np.einsum('i,ij->ij', de, (a1_w1))

                a1_b1 = self.derSigmoid(z[1])
                self.b[1] += -self.alpha * np.einsum('i,ij->ij', de, self.derSigmoid(a1_b1))

                a1_a0 = np.matmul(self.w[1].T, np.einsum('i,ij->ij', de, self.derSigmoid(z[1])))
                a0_w0 = np.matmul(self.derRelu(z[0]), x.T)
                a0_b0 = self.derRelu(z[0])

                self.w[0] += -self.alpha * np.einsum('i,ij->ij', self.scalar_to_array(np.squeeze(a1_a0)), (a0_w0))
                self.b[0] += -self.alpha * np.einsum('i,ij->ij', self.scalar_to_array(np.squeeze(a1_a0)), (a0_b0))

            if (iterations % 1 == 0):
                print("Error: "+ str(np.sum(self.error(a[1], y[i]).T)))
                #print("Accuracy: "+ str(self.getAccuracy(self.getPredictions(a[1]), y[i])))
                #print(self.getPredictions(a[1]))
                #pass

    #
    def fit2(self, X, Y, epochs, X_test=None, y_test=None):

        train_acc = []
        val_acc = []
        train_err = []
        val_err = []

        for iterations in range(0, epochs):
            error = 0

            for x, y in zip(X, Y):
                x = x.reshape(len(x), 1)

                z, a = self.feedforward(x)

                tmp = self.derError(a[-1], y)
                for layer in range(len(self.w)-1, 0, -1):

                    dcw = np.matmul(self.derivativeFunctions[self.activations[layer]](self, z[layer]), a[layer-1].T)
                    dcb = self.derivativeFunctions[self.activations[layer]](self, z[layer])

                    self.w[layer] += -self.alpha * np.einsum('i,ij->ij', np.squeeze(np.asarray(tmp)), dcw)
                    self.b[layer] += -self.alpha * np.einsum('i,ij->ij', np.squeeze(np.asarray(tmp)), dcb)

                    tmp = np.matmul(np.einsum('i,ij->ij', np.squeeze(np.asarray(tmp)), self.derivativeFunctions[self.activations[layer]](self, z[layer])).T, self.w[layer])

                dlw = np.matmul(self.derivativeFunctions[self.activations[0]](self, z[0]), x.T)
                dlb = self.derivativeFunctions[self.activations[0]](self, z[0])

                self.w[0] += -self.alpha * np.einsum('i,ij->ij', np.squeeze(np.asarray(tmp)), dlw)
                self.b[0] += -self.alpha * np.einsum('i,ij->ij', np.squeeze(np.asarray(tmp)), dlb)

                error += np.sum(self.error(a[-1], y).T)

            if iterations % 1 == 0:
                #print("Iteration: "+ str(iterations) +", Error: "+ str(error/len(X)))
                train_err.append(error/(len(X)))

                terr = 0
                p = self.predict(X_test)
                for i in range(0, len(p)):
                    terr += np.sum(self.error(p[i], y_test[i]).T)
                terr /= len(X_test)
                val_err.append(terr)

                if error < 0.0000001:
                    print("Error too small")
                    return

            val_acc.append(self.getAccuracy(X_test, y_test))
            train_acc.append(self.getAccuracy(X_train, y_train))

        return val_acc, train_acc, val_err, train_err

    #
    def predict(self, X):
        result = []
        for x in X:
            result.append(self.feedforward(x)[1][-1])
        return result

    #
    def getAccuracy(self, X, Y):
        predictions = self.predict(X)
        vals = []

        for x in predictions:
            vals.append(np.argmax(x))

        correct = 0
        for i in range(0, len(vals)):
            if vals[i] == np.argmax(Y[i]):
                correct += 1
        return correct / len(X)
### end of class

#
def oneHot(Y):
    array = []
    for y in Y:
        oneHotY = np.zeros(10)
        oneHotY[y] = 1
        array.append(oneHotY)
    return array

# beginning of execution
if __name__ == "__main__":

    #print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

    data = pd.read_csv('mnist_train.csv')
    data = np.array(data)
    np.random.shuffle(data)

    examples = 50000
    X = data[1:examples, 1:]/255.
    Y = oneHot(data[1:examples, 0])
    layer = [784, 10, 10]

    train = 1000
    test = 1000

    X_train = np.array(X[:train])
    y_train = np.array(Y[:train])
    X_test = np.array(X[train:train+test])
    y_test = np.array(Y[train:train+test])

    model = Sequential()
    model.add(layers.Dense(10, input_dim=784, activation="relu"))
    model.add(layers.Dense(10, activation="sigmoid"))

    model.summary()

    model.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])

    time = t.time()
    model.fit(X_train, y_train, epochs=100)
    keras = t.time() - time

    functions = ["Relu", "sigmoid"]
    net = Network(layer, functions, alpha=10/train)

    time = t.time()
    val_acc, train_acc, val_err, train_err = net.fit2(X_train, y_train, 100, X_test, y_test)
    wish = t.time() - time

    print(val_acc)
    print(train_acc)
    print(val_err)
    print(train_err)

    plt.plot(val_acc, color="red")
    plt.plot(train_acc, color="blue")
    plt.show()
    plt.plot(val_err, color="red")

    plt.plot(train_err, color="blue")
    plt.show()

    wish_prediction = []
    k_prediction = []
    real = []
    wish_predictions_as_vector = net.predict(X_test)
    k_predictions_as_vector = model.predict(X_test)
    for i in range(0, len(wish_predictions_as_vector)):
        wish_prediction.append(np.argmax(wish_predictions_as_vector[i]))
        k_prediction.append(np.argmax(k_predictions_as_vector[i]))
        real.append(np.argmax(y_test[i]))
    print(wish_prediction)
    print(k_prediction)
    print(real)


    print("Accuracy Wish: "+ str(net.getAccuracy(X_test, y_test)))
    model.evaluate(X_test, y_test)

    print("Keras: "+ str(keras) +"s, Wish: "+ str(wish) +"s")
