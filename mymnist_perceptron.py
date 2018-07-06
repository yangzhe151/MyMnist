#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 18/7/6 下午7:31
# @Author  : Zhe Yang
# @File    : mymnist_perceptron.py
import tensorflow as tf
import numpy as  np

## to get the data set
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
mnist = read_data_sets('MNIST_data/', one_hot=True)

x = tf.placeholder([None, 784], dtype = 'tf.float32')
y = tf.placeholder([None, 10], dtype = 'tf.float32')
print '1212d'
#######################################################

def Inference():
    return