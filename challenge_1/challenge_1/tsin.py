import rclpy 
import numpy as np
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32


class My_Publisher(Node):
    def __init__(self):
        super().__init__('tsin_node')
        self.publisher = self.create_publisher(Float32, 'signal_sender', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Signal sender initialized!!!')
        self.msg = Float32()
        self.x = 0

    def timer_callback(self):
        self.x += 0.1
        self.msg.data = np.sin(self.x)
        self.publisher.publish(self.msg)



def main(args=None):
    rclpy.init(args=args)
    m_p = My_Publisher()
    rclpy.spin(m_p)
    m_p.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
