#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from pan_tilt_msgs.msg import PanTiltCmdDeg

def continuous_movement(yaw, speed, pitch_min, pitch_max, rate_hz=20):
    pub = rospy.Publisher('/pan_tilt_cmd_deg', PanTiltCmdDeg, queue_size=10)
    rospy.init_node('continuous_pan_tilt_control', anonymous=True)
    rate = rospy.Rate(rate_hz)  # Rate in Hz

    pitch = pitch_min
    direction = 1  # 1 for increasing, -1 for decreasing

    while not rospy.is_shutdown():
        cmd = PanTiltCmdDeg()
        cmd.yaw = yaw
        cmd.pitch = pitch
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
        yaw = float(input("Input the yaw value (-55 to 55): "))
        speed = float(input("Input the speed value (1 to 30): "))
        pitch_min = float(input("Input minimum pitch value (minimun -60): "))
        pitch_max = float(input("Input maximum pitch value (maximum 60): "))
        continuous_movement(yaw, speed, pitch_min, pitch_max)
    except rospy.ROSInterruptException:
        pass
