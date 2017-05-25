import os.path
import numpy as np

class ModelBuilder:
    def __init__(self, model_number):
        self.w_hy = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/w:0']) ).reshape([1])
        self.b_hy = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/b:0']) ).reshape([1]) 
        temp = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/rnn/basic_rnn_cell/weights:0']) ).reshape([101, 1])
        self.rnn_w_xh = temp[1:, :]
        self.rnn_w_hh = temp[1, :]
        self.rnn_b_xh = np.loadtxt( ''.join([os.path.dirname(__file__), '/../model/', model_number, '/rnn/basic_rnn_cell/biases:0']) ).reshape([1])
    
    def run(self, input_vector, status):
        input_vector = np.reshape(input_vector, [1, 100])
        status = np.reshape(status, [1])

        new_status = np.tanh(np.matmul(status, self.rnn_w_hh) + np.matmul(input_vector, self.rnn_w_xh) + self.rnn_b_xh)
        output = 1. / (1 + np.exp( -(np.matmul(self.w_hy, new_status) + self.b_hy) ) )

        return output, new_status
