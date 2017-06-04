import tensorflow as tf
import numpy as np
import codecs
from os import listdir, makedirs
from os.path import abspath, exists, dirname
from sentence2vec import sentence2vec

class Trainer:
    def __init__(self):
        self.s2v = sentence2vec.Sentence2Vec()

    def training(self, model_number, iteration_number):
        sentences = []
        with codecs.open(''.join([dirname(__file__), '/res/model', model_number]), 'r', encoding='utf8') as f:
            for line in f:
                sentences.append(self.s2v.sentence2vec(line))
                
        temp_set = np.zeros([1, 10, 100])
        len_set = []
        for sentence in sentences:    
            temp = np.array(sentence).reshape([1, -1, 100])

            len_set.append(temp.shape[1])
            if (temp.shape[1] > 10):
                temp_set = np.append(temp_set, temp[:, 0:10, :], axis=0)
            elif (temp.shape[1] < 10):
                temp = np.append(temp, np.zeros([1, 10-temp.shape[1], 100]), axis=1)
                temp_set = np.append(temp_set, temp, axis=0)
            else:
                temp_set = np.append(temp_set, temp, axis=0)
    
        true_set = np.ones([temp_set.shape[0]-1, temp_set.shape[1], temp_set.shape[2]+1])
        true_set[:, :, :-1] = temp_set[1:, :, :]
    
        for i in xrange(len(len_set)):
            true_set[i, len_set[i]:10, 100] = 0
    
    #    print(true_set.shape)
    #    print(true_set[:, :, 100])
    
        sentences = []
        for file_name in filter( lambda x: x != 'model'+model_number, listdir( ''.join([dirname(__file__), '/res']) ) ):
            with codecs.open(''.join([dirname(__file__), '/res/', file_name]), 'r', encoding='utf8') as f:
                for line in f:
                    sentences.append(self.s2v.sentence2vec(line))
    
        temp_set = np.zeros([1, 10, 100])
        for sentence in sentences:
            temp = np.array(sentence).reshape([1, -1, 100])

            if (temp.shape[1] > 10):
                temp_set = np.append(temp_set, temp[:, 0:10, :], axis=0)
            elif (temp.shape[1] < 10):
                temp = np.append(temp, np.zeros([1, 10-temp.shape[1], 100]), axis=1)
                temp_set = np.append(temp_set, temp, axis=0)
            else:
                temp_set = np.append(temp_set, temp, axis=0)
    
        false_set = np.zeros([temp_set.shape[0]-1, temp_set.shape[1], temp_set.shape[2]+1])
        false_set[:, :, :-1] = temp_set[1:, :, :]
    
    #    print(false_set.shape)
    #    print(false_set[:, :, -1])
    
        training_set = np.append(true_set, false_set, axis=0)
        np.random.shuffle(training_set)
        
        x_data = training_set[:, :, :-1]
        y_data = training_set[:, :, -1]
        batch_size = x_data.shape[0]
    
    #    print(x_data.shape)
    #    print(y_data.shape)
    
        X = tf.placeholder(tf.float32, [None, 10, 100])
        Y = tf.placeholder(tf.float32, [None, 10])
    
        cell = tf.contrib.rnn.BasicRNNCell(num_units=1)
        rnn_outputs, states = tf.nn.dynamic_rnn(cell,
                                                X,
                                                initial_state=cell.zero_state(batch_size, tf.float32),
                                                dtype=tf.float32)
        output = tf.reshape(rnn_outputs, [-1, 1])
        label = tf.reshape(Y, [-1, 1])
        W_output = tf.Variable(tf.random_normal([1]), name='w')
        b_output = tf.Variable(tf.random_normal([1]), name='b')
    
        hypothesis = output * W_output + b_output
        cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=hypothesis, labels=label))
        train = tf.train.AdamOptimizer(learning_rate=0.03).minimize(cost)
        
    #    prob = tf.sigmoid(hypothesis)
    
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
    
        for epoch in range(iteration_number):
            _, c = sess.run([train, cost], feed_dict={X: x_data, Y: y_data})
            if epoch % 20 == 0:
                print 'cost :', np.transpose(c)
    
    #    result = sess.run(prob, feed_dict={X: x_data}).reshape([-1])
    #    answer = y_data.reshape([-1])
    #    for i in xrange(result.shape[0]):
    #        print(result[i], answer[i])
    
        variables_names = [v.name for v in tf.trainable_variables()]
        values = sess.run(variables_names)
        for n, v in zip(variables_names, values):
            if not exists(''.join([dirname(__file__), '/../model/', model_number, '/']) + '/'.join(n.split('/')[:-1])):
                makedirs(''.join([dirname(__file__), '/../model/', model_number, '/']) + '/'.join(n.split('/')[:-1]))
            np.savetxt(''.join([dirname(__file__), '/../model/', model_number, '/', n]), v, delimiter=',')
