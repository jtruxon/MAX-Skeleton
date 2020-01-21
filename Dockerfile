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

FROM codait/max-base:v1.1.3


WORKDIR /workspace

RUN apt-get update && apt-get install nano && echo alias ll='ls -al' >>~/.bashrc
COPY requirements.txt /workspace
COPY .bashrc /root
RUN cat requirements.txt && pip install -r requirements.txt


# Fill in these with a link to the bucket containing the model and the model file name
ARG model_bucket=https://tfhub.dev/google/nnlm-en-dim128
ARG model_version=2
ARG model_name="Neural network language model"

ARG model_file=${model_version}.tar.gz
ARG model_url=${model_bucket}/${model_version} 
#?tf-hub-format=compressed
ARG use_pre_trained_model=true

ENV TFHUB_CACHE_DIR=/workspace/assets
ENV TFHUB_MODULE_URL=${model_url}
ENV TFHUB_MODULE_NAME=${model_name}

RUN touch ${model_file}.txt

# RUN if [ "$use_pre_trained_model" = "true" ] ; then\
#      # download pre-trained model artifacts from Cloud Object Storage
#      wget -nv --show-progress --progress=bar:force:noscroll ${model_url} --output-document=assets/${model_file} &&\
#      tar -x -C assets/ -f assets/${model_file} -v && rm assets/${model_file} ; \
#     fi

#PRELOAD MODEL
COPY tfhub_cache.py /workspace
RUN python tfhub_cache.py

COPY . /workspace

RUN if [ "$use_pre_trained_model" = "true" ] ; then \
      if [ -f "./md5sums.txt" ] ; then \
        # validate downloaded pre-trained model assets
        md5sum -c md5sums.txt ; \
      fi \
    else \
      # rename the directory that contains the custom-trained model artifacts
      if [ -d "./custom_assets/" ] ; then \
        rm -rf ./assets && ln -s ./custom_assets ./assets ; \
      fi \
    fi

EXPOSE 5000

CMD python app.py
