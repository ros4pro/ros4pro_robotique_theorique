#!/usr/bin/env python
import rospy
import tf2_ros
import tf2_geometry_msgs
from  math import cos, sin, atan2, sqrt
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PointStamped
global a1, a2, d3
a1 = 0
a2 = 0
d3 = 0

R1 = 1
R2 = 1

if __name__ == '__main__':
    rospy.init_node('geometrique_direct', anonymous=True)
    tf_buffer = tf2_ros.Buffer(rospy.Duration(1200.0))
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    joint_state_pub =rospy.Publisher("/joint_states", JointState, queue_size=100)
    rate = rospy.Rate(1) # 1hz

    #tableau des [x, y, z] qui seront utilises pour tester votre modele geometrique inverse
    test_value = [[2, 0, 0], [-0.2, 0.6, -0.6], [0.2, -0.8, -0.15], [0.99, 1.2, -0.05]]
    for p_test in test_value:
        x = p_test[0]
        y = p_test[1]
        z = p_test[2]
        
        # utilisez votre modele geometrique inverse pour calculer a1, a2 et d3
        # aide python:
        #   cosinus : cos()
        #   sinus : sin()
        #   atan2 : atan2(y, x)
        #   racine carre : sqr(x*x) = x
        # exemple:  a = sin(alpha * theta) * D + cos(beta - alpha)
        
        a1 = 1
        a2 = 1
        d3 = 1
        

        # envoie les angles / commandes au noeud qui controle le bras
        js = JointState()
        js.header.stamp = rospy.Time.now()
        js.name = ["link1_to_base", "link2_to_link1", "link3_to_link2"]
        js.position = [a1, a2, d3]
        js.velocity = []
        js.effort = []
        r_pub = rospy.Rate(50)
        for i in range(100):
            joint_state_pub.publish(js)
            r_pub.sleep()

        # recupere les valeurs de x, y et z calculees par ROS
        transform = tf_buffer.lookup_transform("base_link",
                                       "link_3", #source frame
                                       rospy.Time(0), #get the tf at first available time
                                       rospy.Duration(1.0)) #wait for 1 second

        diff_x = - transform.transform.translation.x + x
        diff_y = - transform.transform.translation.y + y
        diff_z = - transform.transform.translation.z + z
        print("x: {} diff_x: {}".format(transform.transform.translation.x, diff_x))
        print("y: {} diff_y: {}".format(transform.transform.translation.y, diff_y))
        print("z: {} diff_z: {}".format(transform.transform.translation.z, diff_z))
        rate.sleep()