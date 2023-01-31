# Copyright (c) 2021 Intelligent Robotics Lab (URJC)
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

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription 

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution 

from launch_ros.actions import Node

import yaml

def generate_launch_description():
    ir_robots_dir = get_package_share_directory('ir_robots')

    params_file = os.path.join(ir_robots_dir, 'config', 'kobuki_node_params.yaml')
    with open(params_file, 'r') as f:
        kobuki_params = yaml.safe_load(f)['kobuki_ros_node']['ros__parameters']

    kobuki_cmd = Node(package='kobuki_node',
        executable='kobuki_ros_node',
        output='screen',
        parameters=[kobuki_params],
        remappings=[
            ('/commands/velocity', '/cmd_vel'),
        ]
        )

    ld = LaunchDescription()

    ld.add_action(kobuki_cmd)
  
    return ld
