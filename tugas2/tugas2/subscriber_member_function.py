# Copyright 2016 Open Source Robotics Foundation, Inc.
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

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription1 = self.create_subscription(
            String,
            'pub1',
            self.listener_callback1,
            10)
        self.subscription1  # prevent unused variable warning

        self.subscription2 = self.create_subscription(
            String,
            'pub2',
            self.listener_callback2,
            10)
        self.subscription2  # prevent unused variable warning
        
        self.recieve1 = None
        self.recieve2 = None

    def listener_callback1(self, msg):
        self.recieve1 = msg.data
    
    def listener_callback2 (self, msg):
        self.recieve2 = msg.data
        self.cek()
    
    def cek(self):
        if self.recieve1 == 'True' and self.recieve2 == 'True':
            self.get_logger().info(f"pub1 - {self.recieve1} | pub2 - {self.recieve2} -> sudah siap nih, gass min!")
        else:
            self.get_logger().info(f"pub1 - {self.recieve1} | pub2 - {self.recieve2} -> tunggu dulu, kami belum ready!")           
        self.recieve1 = None
        self.recieve2 = None



def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
