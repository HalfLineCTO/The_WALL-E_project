import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalSubscriber_raspby(Node):

    def __init__(self):
        super().__init__('py_topic_subscriber_spiral')
        self.subscriber_ = self.create_subscription(Twist, 'turtlebot_cmdVel', self.subscribe_message, 10)
        self.subscriber_  # prevent unused variable warning

    def subscribe_message(self, msg):
        self.get_logger().info('Recieved - Linear Velocity : %f, Angular Velocity : %f' % (self.twist_msg_.linear.x, self.twist_msg_.angular.z))

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber_raspby()
    rclpy.spin(minimal_subscriber)
    print('Recibiendo datos del computador')
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()