# Copyright 2018, OpenCensus Authors
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

import threading

_thread_local = threading.local()


def get_measure_to_view_map():
    return getattr(_thread_local, 'measure_to_view_map', {})


def set_measure_to_view_map(measure_to_view_map):
    setattr(_thread_local, 'measure_to_view_map', measure_to_view_map)


def clear():
    _thread_local.__dict__.clear()
