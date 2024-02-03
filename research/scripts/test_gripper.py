#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any
import rospy, sys
import moveit_commander
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler

class MoveItIkDemo:
    def __init__(self):
       
        # 初始化ROS节点 
        rospy.init_node('moveit_gripper_demo')
        
        # 实例化一个 "RobotCommander" 对象. 该对象是机器人与外界的接口：
        robot = moveit_commander.RobotCommander()

        # 初始化需要使用move group控制的机械臂中的arm group
        gripper = moveit_commander.MoveGroupCommander('fr3_hand')

        # 设置机械臂和夹爪的允许误差值 
        gripper.set_goal_joint_tolerance(0.001)

        gripper.set_named_target('open')
        gripper.go()

        # 设置夹爪的目标位置，并控制夹爪运动 
        gripper.set_joint_value_target([0.01, 0.01])
        gripper.go()

        gripper.set_named_target('open')
        gripper.go()


if __name__ == "__main__":
    MoveItIkDemo()




