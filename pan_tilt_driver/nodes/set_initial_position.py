#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import JointState

class SetInitialPosition:
    def __init__(self):
        rospy.init_node('set_initial_position', anonymous=True)
        self.get_current_position()

    def get_current_position(self):
        joint_states = rospy.wait_for_message('/joint_states', JointState)
        self.yaw_initial = joint_states.position[0]  # Assuming the yaw joint is the first one
        self.pitch_initial = joint_states.position[1]  # Assuming the pitch joint is the second one
        rospy.loginfo("Nueva posición inicial establecida: Yaw: {}, Pitch: {}"
                      .format(self.yaw_initial,self.pitch_initial))

        with open("/home/ablubuntu/ros_ws/src/pan_tilt_ros/pan_tilt_driver/nodes/initial_position.txt", "w") as f:
            f.write("{},{}".format(self.yaw_initial,self.pitch_initial))

if __name__ == '__main__':
    try:
        SetInitialPosition()
    except rospy.ROSInterruptException:
        pass
