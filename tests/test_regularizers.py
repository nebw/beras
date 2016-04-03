# Copyright 2016 Leon Sixt
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

import numpy as np

from beras.regularizers import ActivityInBoundsRegularizer
from keras.layers.core import Layer
import theano


def test_activity_in_bounds_regularizer():
    layer = Layer()
    input = theano.shared(np.array([0, 0], dtype='float32'))
    layer.input = input
    reg = ActivityInBoundsRegularizer()
    reg.set_layer(layer)
    assert reg(0).eval() == 0

    input.set_value(np.array([2], dtype='float32'))
    assert reg(0).eval() > 0