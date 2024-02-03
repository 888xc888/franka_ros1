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
        rospy.init_node('moveit_ik_demo')
        
        # 实例化一个 "RobotCommander" 对象. 该对象是机器人与外界的接口：
        robot = moveit_commander.RobotCommander()

        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('fr3_manipulator')
    
        # 实例化一个 "PlanningSceneInterface" 对象。这个对象是机器人与周围环境的接口:
        scene = moveit_commander.PlanningSceneInterface()

        # 获取终端link的名称
        end_effector_link = arm.get_end_effector_link()

        # 设置目标位置所使用的参考坐标系
        reference_frame = 'world'
        arm.set_pose_reference_frame(reference_frame)

        # 当运动规划失败后，允许重新规划
        arm.allow_replanning(True)

        # 设置位置(单位：米)和姿态（单位：弧度）的允许误差 
        arm.set_goal_position_tolerance(0.01)
        arm.set_goal_orientation_tolerance(0.05)

        # 控制机械臂先回到初始化位置 
        arm.set_named_target('ready')
        arm.go()
        rospy.sleep(2)


        # print("============ Printing robot state")
        # print(robot.get_current_state())
        # print("")

        # 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述
        # 姿态使用四元数描述，基于world坐标系
        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()
        target_pose.pose.position.x = 0.4
        target_pose.pose.position.y = 0
        target_pose.pose.position.z = 0.3

        # 欧拉角转四元数
        q = quaternion_from_euler(3.14, 0, 0)

        target_pose.pose.orientation.x = q[0]
        target_pose.pose.orientation.y = q[1]
        target_pose.pose.orientation.z = q[2]
        target_pose.pose.orientation.w = q[3]

        # 设置机器臂当前的状态作为运动初始状态 
        arm.set_start_state_to_current_state()

        # 设置机械臂终端运动的目标位姿 
        arm.set_pose_target(target_pose, end_effector_link)

        # 现在，我们调用规划器计算路径并执行：
        plan = arm.go(wait=True)
        # 调用 stop() 命令以确认是否还有未完成的运动。
        arm.stop()

        # 在规划完成后，清除目标位姿总是有益的。
        # 注意：没有任何函数与 clear_joint_value_targets() 等价。
        arm.clear_pose_targets()

        # 控制机械臂回到初始化位置
        arm.set_named_target('ready') 
        arm.go()

if __name__ == "__main__":
    MoveItIkDemo()




