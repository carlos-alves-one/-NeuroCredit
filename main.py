
# Goldsmiths University of London
# Author....: Carlos Manuel de Oliveira Alves
# Student...: cdeol003
# Created...: 15/01/2023
# FYP.......: NeuroCredit

# neural network class definition
class neuralNetwork:

    # initialise the neural network
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes

        # learning rate
        self.lr = learning_rate
    
        pass

    # train the neural network
    def train():
        pass

    # query the neural network
    def query():
        pass
    
# declare the number of input, hidden and output nodes
input_nodes  = 3
hidden_nodes = 3
output_nodes = 3

# declare the learning rate is 0.3
learning_rate = 0.3

# create instance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
