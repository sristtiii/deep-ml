import numpy as np
import math

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):

    updated_weights = initial_weights.copy()
    updated_bias = initial_bias
    mse_values = []

    for epoch in range(epochs):

        grad_weights = [0.0] * len(initial_weights)
        grad_bias = 0.0
        total_loss = 0.0

        for i in range(len(features)):

            z = 0

            for j in range(len(features[0])):
                z += features[i][j] * updated_weights[j]

            z += updated_bias

            sigmoid = 1 / (1 + math.exp(-z))

            total_loss += ((sigmoid - labels[i]) ** 2)

            delta = 2 * (sigmoid - labels[i]) * sigmoid * (1 - sigmoid)

            for j in range(len(updated_weights)):
                grad_weights[j] += delta * features[i][j]

            grad_bias += delta

        mse_values.append(round(total_loss / len(labels), 4))

        for j in range(len(updated_weights)):
            grad_weights[j] = grad_weights[j] / len(labels)

        grad_bias = grad_bias / len(labels)

        for j in range(len(updated_weights)):
            updated_weights[j] = updated_weights[j] - learning_rate * grad_weights[j]

        updated_bias = updated_bias - learning_rate * grad_bias

    return updated_weights, updated_bias, mse_values