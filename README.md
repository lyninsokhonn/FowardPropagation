# FowardPropagation
Forward propagation(forwarding) from input layer to output layer in neural network

input_matrix, w_input_hidden, w_hidden_output are the given matrices.

To get Ooutput, we need to find Xhidden, Ohidden, Xoutput, respectively:

- Xhidden = Winput_hidden * I
- Ohidden = sigmoid(Xhidden)
- Xoutput = Whidden_output * Ohidden

At the end, Ooutput is given by: Ooutput = sigmoid(Xoutput)
