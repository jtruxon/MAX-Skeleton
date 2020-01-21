
#
# Copyright 2018-2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import tensorflow as tf
# from tensorflow.keras.backend import set_session
import tensorflow_hub as hub

import json 
import io
import numpy as np
from PIL import Image

from config import *

from maxfw.model import MAXModelWrapper

import logging

logger = logging.getLogger()


class ModelWrapper(MAXModelWrapper):

    MODEL_META_DATA = {
        'id': 'Image Classification',
        'name': 'Max-fasion-MNIST',
        'description': 'classify clothing and fasion items',
        'type': 'Image Classification',
        'source': 'MODEL SOURCE',
        'license': 'Apache 2.0'
    }

    def __init__(self, path=TFHUB_MODULE_URL):
        logger.info(f'Loading model from: {TFHUB_MODULE_URL}...')

        # Load the graph
        # global sess
        # global graph
        # sess = tf.Session() 
        # graph = tf.get_default_graph()
        # set_session(sess)
        # self.model = tf.keras.models.load_model(path)
        print("Loading Model.")
        self.model = hub.KerasLayer(TFHUB_MODULE_URL)
        print("Model Loaded.")

        # Set up instance variables and required inputs for inference

        logger.info('Loaded model')

    # def _pre_process(self, inp):
    #     # Open the input image
    #     img = Image.open(io.BytesIO(inp))
    #     print('reading image..', img.size)
    #     # Convert the PIL image instance into numpy array and
    #     # get in proper dimension.
    #     image = tf.keras.preprocessing.image.img_to_array(img)
    #     print('image array shape..', image.shape)
    #     image = np.expand_dims(image, axis=0)
    #     print('image array shape..', image.shape)
    #     return image


    # def _post_process(self, result):
    #     # Extract prediction probability using `amax` and
    #     # digit prediction using `argmax`
    #     return [{'probability': np.amax(result),
    #              'prediction': CLASS_DIGIT_TO_LABEL[np.argmax(result)]}]

    def _pre_process(self, inp):
        self._input = inp.split()
        return self._input

    def _post_process(self, result):
        return [{'item': self._input[idx].decode('utf-8'),
                 'embeddingVector': r.numpy().tolist()} for idx,r in enumerate(result)]


    def _predict(self, x):
        # with graph.as_default():
        #   set_session(sess)
        result = self.model(x)
        return result
