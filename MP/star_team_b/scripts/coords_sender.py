#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def sender():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('sender', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        msg = "hello"
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    sender()