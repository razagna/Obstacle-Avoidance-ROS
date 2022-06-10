#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(data):
    right = min(min(data.ranges[325:330]), 3.5)
    center = min(data.ranges[0], 3.5)
    left = min(min(data.ranges[25:30]), 3.5)

    if(center > min_fwd and right > min_side and left > min_side):
        state = 'Free!'
        update_velocity_command(linear_vel, 0)
    elif(center > min_fwd and right < min_side and left > min_side):
        state = 'Right Obstacle!'
        update_velocity_command(0, angular_vel) 
    elif(center > min_fwd and right > min_side and left < min_side):
        state = 'Left Obstacle!'
        update_velocity_command(0, -1*angular_vel)
    elif(center < min_fwd):
        state = 'Forward Obstacle!'
        update_velocity_command(0, -1*angular_vel)
    else:
        state = 'Please wait...'
   
    rospy.loginfo(state)

def update_velocity_command(linear, angular):
    cmd_vel = Twist()
    cmd_vel.linear.x = linear
    cmd_vel.angular.z = angular

    velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    velocity_publisher.publish(cmd_vel)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("scan_topic", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    min_fwd = rospy.get_param('/drive_turtlebot3/forward_distance', 0.8)
    min_side = rospy.get_param('/drive_turtlebot3/side_distance', 0.5)
    linear_vel = rospy.get_param('/drive_turtlebot3/forward_speed', 0.5)
    angular_vel = rospy.get_param('/drive_turtlebot3/angular_speed', 1.5)
    listener()
    
