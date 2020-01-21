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

import os

# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'list'

# API metadata
API_TITLE = 'MAX'
API_DESC = 'An API for serving models'
API_VERSION = '0.1'

# default model
MODEL_NAME = 'fashion_mnist.h5'
# DEFAULT_MODEL_PATH = 'assets/{}'.format(MODEL_NAME)
TFHUB_MODULE_URL = os.environ["TFHUB_MODULE_URL"]

# # used in the prediction post-processing
# CLASS_DIGIT_TO_LABEL = {
#   0: "T-shirt/top",
#   1: "Trouser",
#   2: "Pullover",
#   3: "Dress",
#   4: "Coat",
#   5: "Sandal",
#   6: "Shirt",
#   7: "Sneaker",
#   8: "Bag",
#   9: "Ankle boot"
# }
