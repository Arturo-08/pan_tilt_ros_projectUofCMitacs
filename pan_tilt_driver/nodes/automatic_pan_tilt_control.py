#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from pan_tilt_msgs.msg import PanTiltCmdDeg

def slowly_movement(rate_hz=20):
    pub = rospy.Publisher('/pan_tilt_cmd_deg', PanTiltCmdDeg, queue_size=10)
    rospy.init_node('continuous_pan_tilt_control', anonymous=True)
    rate = rospy.Rate(rate_hz)  # Rate in Hz
    yaw = -10 
    speed = 1
    pitch_min = -8.0
    pitch_max = 8.0
    direction = 1  # 1 for increasing, -1 for decreasing

    while not rospy.is_shutdown():
        cmd = PanTiltCmdDeg()
        cmd.yaw = yaw
        cmd.pitch = 0
        cmd.speed = speed
        
        rospy.loginfo("Current Yaw: {}, Pitch: {}, Speed: {}".format(yaw, pitch, speed))
        pub.publish(cmd)

        pitch += direction * speed / rate_hz

        # Reverse direction at limits
        if pitch >= pitch_max:
            direction = -1
        elif pitch <= pitch_min:
            direction = 1

        rate.sleep()

if __name__ == '__main__':
    try:
        slowly_movement()
    except rospy.ROSInterruptException:
        pass
