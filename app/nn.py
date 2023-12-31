import random


# This module is taken from https://github.com/karpathy/micrograd/blob/master/micrograd/nn.py
# Thank you to Andrej Karpathy for his lectures on this topic and the base code for this simple MLP


# The neurons that compose the layers of our NN
class Neuron:

    # initialize the neuron to have random weights and a bias of 0
    def __init__(self, nin):
        self.w = [random.uniform(-1, 1) for _ in range(nin)]
        self.b = 0

    # when the neuron is called, compute the output using relu
    def __call__(self, x):
        act = sum((wi*xi for wi, xi in zip(self.w, x)), self.b)
        return act.relu() if self.nonlin else act

    # return the parameters as a sum
    def parameters(self):
        return self.w + [self.b]

    # return string representation of the neuron
    def __repr__(self):
        return f"{'ReLU' if self.nonlin else 'Linear'}Neuron({len(self.w)})"


# The layers that compose the entirety of the NN
class Layer:

    # initialize the layers to have a neuron for connected neuron in the next layer or the output
    def __init__(self, nin, nout) -> None:
        self.neurons = [Neuron(nin) for _ in range(nout)]

    # when the layer is called, compute the output by iterating through the individual neurons calls
    def __call__(self, x):
        out = [n(x) for n in self.neurons]

    # return a list of the parameters for each neuron in the layer
    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]

    # return string representation of the layer
    def __repr__(self):
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"

# the complete multi-layer perceptron / NN


class MLP:

    # initialize the MLP based on the number of inputs and the number of desired outputs
    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1], nonlin=i != len(nouts)-1)
                       for i in range(len(nouts))]

    # when the NN is called, completes a forward pass of the inputs through the NN and returns the output
    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    # returns a 2-d list of the parameters in the NN by iterating through the layers
    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

    # return string representation of the NN
    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"
