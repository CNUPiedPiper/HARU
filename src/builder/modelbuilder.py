import os.path
import numpy as np

class ModelBuilder:
    def __init__(self, model_number):
        self.w0 = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/w:0']), delimiter=',' ).reshape([100, 1])
        self.b0 = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/b:0']), delimiter=',' ).reshape([1])
        self.c0w0 = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/rnn/multi_rnn_cell/cell_0/basic_rnn_cell/weights:0']), delimiter=',' )
        self.c0b0 = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/rnn/multi_rnn_cell/cell_0/basic_rnn_cell/biases:0']), delimiter=',' )
        self.c1w0 = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/rnn/multi_rnn_cell/cell_1/basic_rnn_cell/weights:0']), delimiter=',' )
        self.c1b0 = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/rnn/multi_rnn_cell/cell_1/basic_rnn_cell/biases:0']), delimiter=',' )
    
    def run(self, input_vector, status_1, status_2):
        input_vector = np.append(input_vector, status_1).reshape([1, 200])
        new_status_1 = np.tanh(np.matmul(input_vector, self.c0w0) + self.c0b0)

        mid_vector = np.append(new_status_1, status_2).reshape([1, 200])
        new_status_2 = np.tanh(np.matmul(mid_vector, self.c1w0) + self.c1b0)

        output = 1. / (1 + np.exp( -(np.matmul(new_status_2.reshape([1, 100]), self.w0) + self.b0) ) )

        return output, new_status_1, new_status_2
