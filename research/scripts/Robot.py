#!/usr/bin/env python
# 本文件描述机械臂

# Python 2/3 compatibility imports
from __future__ import print_function
from six.moves import input

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg



class Robot:
    # fr3机器人类，里面包括了描述储存机器人的各种属性，定义移动机器人的各种方法

    # 下面是一些属性
    
    # 当前笛卡尔位置
    self.current_cartesian_position = 
    # 目标笛卡尔位置
    self.target_cartesian_position = 
    # home位置
    self.__home = 

    # 储存机械爪状态
    self.gripper_state = 


    #================================初始化函数
    #初始化机器人
    def __init__(self):



        
    #================================移动相关函数

    #运动停止函数


    #清除轨迹函数

    #回到初始状态函数
    def home(self):


        return 0 



    #================================夹爪相关函数


    #打开


    #关闭


    #加持到宽度h





    #================================高级任务函数


    #取几号工具



    #放置几好工具


    #放置几号拆卸的零件
















    # 机械臂状态打印函数，打印机械臂各个关节位置和机械爪的状态
    def print_robot_state():

        print("当前机械臂状态是：" +self.current_cartesian_position)
        print("当前机械爪状态是：" +self.current_cartesian_position)
        return 0

    # 回到home位置
    def move_to_home(self, self.__home):

        return 0
    
    # 刷新机械臂最新位置
    def set_current_cartesian_position(self):

        return 0

    # 设置机械臂目标位置
    def set_target_cartesian_position(self):

        return 0
    
    # 移动到目标位置
    def move_to_target(self, self.target_cartesian_position):
    
        return 0

    # 夹爪闭合函数，参数h为闭合后两个爪之间的宽度
    def gripper_closure(self, h):

        
        return 0
    

    # 夹爪释放函数，参数h为闭合后两个爪之间的宽度
    def gripper_release(self, h):

        return 0
    

    # 拿取工具函数，tool_name为要拿取工具的名字
    def take_tool(self，tool_name):
        
        return 0

    # 归还工具函数，tool_name为要拿取工具的名字
    def return_tool(self，tool_name):
        
        return 0


    # turn函数为将螺丝拧下来的函数，实际上就算转动jion_7关节
    def turn(self):
    
        return 0

        
    # 存放拧下来的零件的函数
    def store_part(self, part_name):


        return 0

    # 机械臂末端移动到相对word坐标系的x, y, z位置
    def move_point(self, x, y, z):



        return 0

    def move_(direction, distance):


        return 0





if __name__ == "__main__":
    myrobot = Robot()
    myrobot.he()
    myrobot.home()
    myro