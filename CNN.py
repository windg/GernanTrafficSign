from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Imports
import numpy as np
import tensorflow as tf
ImageSize = 32
NumChannel = 3
NumClasses = 43
NumExampleTrain = 50000
NumExampleEval = 10000
filterSize = 5

if __name__ == "__main__":
    tf.app.run()


def weight_variable(shape):
    # Random initial values
    initial = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv_layer(x,filter):
    W = weight_variable(shape=filter)
    b = bias_variable(shape=filter)
    conv2d = tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
    # Batch Normalization Layer #1
    batch = tf.layers.batch_normalization(conv2d + b)
    # Relu Layer #1
    relu = tf.nn.relu(batch)
    # Max Pooling Layer #1
    pooling = tf.nn.max_pool(relu,ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1], padding='SAME')
    return pooling

def full_layer(x, size):
    in_size = int(x.get_shape()[1])
    W = weight_variable([in_size, size])
    b = bias_variable([size])
    return tf.matmul(x, W) + b

def main_model(image):
    c1 = conv_layer(x=image, filter=[filterSize, filterSize, NumChannel, 32])
    c2 = conv_layer(x=c1, filter=[filterSize, filterSize, 32, 32])
    c3 = conv_layer(x=c2, filter=[filterSize, filterSize, NumChannel, 64])

    dropout = tf.layers.dropout(c3, rate=0.3)
    # Softmax Layer
    soft = tf.nn.softmax(dropout)
    flat = tf.reshape(soft,[-1, 4*4*64])
    return full_layer(flat,NumClasses)
