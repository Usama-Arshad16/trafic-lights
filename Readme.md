1. Extract the package into catkin_ws/src.
2. Use following commands to install the package.
	$ cd catkin_ws
	$ catkin_make
	$ source devel/setup.bash
3. Now go into  catkin_ws/src/trafic_lights/gazebo_models and copy all the models
	and paste inside /home/username/.gazebo/models.
	Note: go to home folder and press Ctrl+h to see the hidden folder ".gazebo" .
4. To the packege use the following commands in terminal.
	$ roslaunch trafic_lights gazebo.launch
	 Open another terminal.
	$ rosrun trafic_lights signal_control.py