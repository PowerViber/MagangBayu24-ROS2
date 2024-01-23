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
from std_msgs.msg import String, Bool

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher1 = self.create_publisher(String, 'pub1', 10)
        self.publisher2 = self.create_publisher(String, 'pub2', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.i += 1

        cek1 = self.i % 2 == 0 #ngecek pub 1 setiap true
        cek2 = self.i % 3 == 0 #ngecek pub 2 setiap true

        # publisher 1
        msg1 = String()
        msg1.data = str(cek1)
        self.publisher1.publish(msg1)
        self.get_logger().info('Publisher - 1 - (%d sec) -> %s' % (self.i,msg1.data))

        # publisher 2
        msg2 = String()
        msg2.data = str(cek2)
        self.publisher2.publish(msg2)
        self.get_logger().info('Publisher - 2 - (%d sec) -> %s' % (self.i,msg2.data))



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
