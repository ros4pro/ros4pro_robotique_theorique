#!/usr/bin/env python
import rospy
import tf2_ros
import tf2_geometry_msgs
from  math import cos, sin
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PointStamped
global a1, a2, d3
a1 = 0
a2 = 0
d3 = 0

R1 = 1
R2 = 1

def cb(msg):
    global a1, a2, d3
    a1 = msg.position[0]
    a2 = msg.position[1]
    d3 = msg.position[2]

if __name__ == '__main__':
    rospy.init_node('geometrique_direct', anonymous=True)
    tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0))
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    joint_state_sub =rospy.Subscriber("/joint_states", JointState, cb)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
        
        # utilisez votre modele geometrique direct pour calculer x, y et z
        # aide python:
        #   cosinus : cos()
        #   sinus : sin()
        # exemple:  a = sin(alpha * theta) * D + cos(beta - alpha)

        x = R1*cos(a1)+R2*(cos(a2)*cos(a1)-sin(a2)*sin(a1))
        y = R1*sin(a1)+R2*(cos(a2)*sin(a1)+sin(a2)*cos(a1))
        z = -d3



        # recupere les valeurs de x, y et z calculees par ROS
        transform = tf_buffer.lookup_transform("base_link",
                                       "link_3", #source frame
                                       rospy.Time(0), #get the tf at first available time
                                       rospy.Duration(1.0)) #wait for 1 second
        
        diff_x = transform.transform.translation.x - x
        diff_y = transform.transform.translation.y - y
        diff_z = transform.transform.translation.z - z

        print("x: {} diff_x: {}".format(x, diff_x))
        print("y: {} diff_y: {}".format(y, diff_y))
        print("z: {} diff_z: {}".format(z, diff_z))
        rate.sleep()