import rclpy 
import numpy as np
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32


class My_Listener(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.sub = self.create_subscription(Float32, 'signal_sender', self.listener_callback, 10)
        self.publisher = self.create_publisher(Float32, 'process_signal', 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.process_signal_callback)
        self.r_signal = Float32();

        self.get_logger().info('Listener of sin working')

    def listener_callback(self,msg):
        self.r_signal.data = msg.data

    def process_signal_callback(self):
        self.r_signal.data = self.r_signal.data * 4.0;
        self.publisher.publish(self.r_signal)


def main(args=None):
    rclpy.init(args=args)
    m_s = My_Listener()
    rclpy.spin(m_s)
    m_s.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
