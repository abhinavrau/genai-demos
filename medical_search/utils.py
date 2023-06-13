# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import requests


def get_env_project_id() -> str:
    """Returns the Project ID from GAE or Cloud Run"""
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
    if not project_id:
        project_id = 'vijay-sandbox-335018'
        # project_id = requests.get(
        #    "http://metadata.google.internal/computeMetadata/v1/project/project-id",
        #    headers={"Metadata-Flavor":"Google"}
        # ).text

    return project_id


def get_search_engine_id() -> str:
    """Returns the Search Engine ID from GAE or Cloud Run"""
    search_engine_id = os.getenv('SEARCH_ENGINE_ID')
    if not search_engine_id:
        search_engine_id = 'bioasq_0'
    return search_engine_id


def get_region() -> str:
    """Returns the Region from GAE or Cloud Run"""
    region = os.getenv('REGION')
    if not region:
        region = 'us-central1'
    return region