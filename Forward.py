import math

input_matrix =      [0.9, 0.1, 0.8]
w_input_hidden =    [[0.9, 0.3, 0.4],
                    [0.2, 0.8, 0.2],
                    [0.1, 0.5, 0.6]]
w_hidden_output =   [[0.3, 0.7, 0.5],
                    [0.6, 0.5, 0.2],
                    [0.8, 0.1, 0.9]]
x_hidden = []
o_hidden = []       
x_output = []  
o_output = []   

# y = sigmoid(x)
def sigmoid(x, y):
    for i in range(len(x)):
        sig_funct = 1/(1 + math.exp((-1) * x[i]))
        # format the result to only 3 digits after decimal points
        format_sig_funct = "{:.3f}".format(sig_funct)
        y.append(float(format_sig_funct))

# z = x * y
def matrix_mul(x, y, z):
    for i in range(len(x)):
        element = 0
        for j in range(len(x[i])):
            element =  element + (x[i][j] * y[j])
        z.append(element)

print("Input : " + str(input_matrix))

# find matrix X_hidden
matrix_mul(w_input_hidden, input_matrix, x_hidden)

# find matrix O_hidden
sigmoid(x_hidden, o_hidden)

# find matrix X_output
matrix_mul(w_hidden_output, o_hidden, x_output)

# find matrix O_output
sigmoid(x_output, o_output)
print("Output : " + str(o_output))