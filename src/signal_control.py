#!/usr/bin/env python
import rospy 
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState

on = -0.31
off = -0.25

def red(p):
    rospy.init_node('set_pose')
    state_msg = ModelState()

    state_msg.model_name = 'red_light'
    state_msg.pose.position.x = -0.01
    state_msg.pose.position.y = p
    state_msg.pose.position.z = 2.315
    state_msg.pose.orientation.x = 1.1
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 1


    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def black_1(p):
    rospy.init_node('set_pose')
    state_msg = ModelState()

    state_msg.model_name = 'empty_light_1'
    state_msg.pose.position.x = -0.01
    state_msg.pose.position.y = p
    state_msg.pose.position.z = 2.315
    state_msg.pose.orientation.x = 1.1
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 1


    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def yellow(p):
    rospy.init_node('set_pose')
    state_msg = ModelState()


    state_msg.model_name = 'yellow_light'
    state_msg.pose.position.x = -0.01
    state_msg.pose.position.y = p
    state_msg.pose.position.z = 2.08
    state_msg.pose.orientation.x = 1.1
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 1
    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def black_2(p):
    rospy.init_node('set_pose')
    state_msg = ModelState()


    state_msg.model_name = 'empty_light_2'
    state_msg.pose.position.x = -0.01
    state_msg.pose.position.y = p
    state_msg.pose.position.z = 2.08
    state_msg.pose.orientation.x = 1.1
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 1

    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def green(p):
    rospy.init_node('set_pose')
    state_msg = ModelState()


    state_msg.model_name = 'green_light'
    state_msg.pose.position.x = -0.01
    state_msg.pose.position.y = p
    state_msg.pose.position.z = 1.81
    state_msg.pose.orientation.x = 1.1
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 1
    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def black_3(p):
    rospy.init_node('set_pose')
    state_msg = ModelState()


    state_msg.model_name = 'empty_light_3'
    state_msg.pose.position.x = -0.01
    state_msg.pose.position.y = p
    state_msg.pose.position.z = 1.81
    state_msg.pose.orientation.x = 1.1
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 1

    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def light_control():
    request = str(raw_input("Type any of  r y g | a n: "))
    if request ==  "r":
        for i in range(2):
            red(on)
            black_1(off)
            yellow(off)
            black_2(on)
            green(off)
            black_3(on)
    if request ==  "y":
        for i in range(2):
            red(off)
            black_1(on)
            yellow(on)
            black_2(off)
            green(off)
            black_3(on)
    if request ==  "g":
        for i in range(2):
            red(off)
            black_1(on)
            yellow(off)
            black_2(on)
            green(on)
            black_3(off)
    if request ==  "n":
        for i in range(2):
            red(off)
            black_1(on)
            yellow(off)
            black_2(on)
            green(off)
            black_3(on)
    if request ==  "a":
        for i in range(2):
            red(on)
            black_1(off)
            yellow(on)
            black_2(off)
            green(on)
            black_3(off)
    print "-----"

while not rospy.is_shutdown():
    light_control()
    rospy.sleep(0.01)