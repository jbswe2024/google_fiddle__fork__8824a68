# coding=utf-8
# Copyright 2022 The Fiddle-Config Authors.
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

"""Methods to validate Fiddle configs are valid or conform to recommendations.

Please see individual methods' docstrings.
"""

# pylint: disable=unused-import
from fiddle._src.validation.baseline_style import check_baseline_style
from fiddle._src.validation.no_custom_objects import check_no_custom_objects
from fiddle._src.validation.no_custom_objects import get_config_errors
