## Dependencies
#### ROS Noetic
Follow the official installation guide [here.](http://wiki.ros.org/noetic/Installation/Ubuntu)
=> the stand-alone version of Gazebo is included in the installation

#### Packages
1. Install the ROS packages for Turtlebot3
	```bash
	sudo apt install ros-noetic-turtlebot3
	```
2. Install additional useful ROS packages
	```bash
	sudo apt install ros-noetic-gmapping ros-noetic-map-server ros-noetic-vision-msgs ros-noetic-costmap-2d -y
	```

## Workspace
1. Create workspace
	```bash
	mkdir -p catkin_ws/src
	```
2. Get the `Turtle3` repository
	```bash
	cd catkin_ws/src
	git clone --recursive https://github.com/razagna/Turtle3
	```
3. Install any missing dependencies
	```bash
	cd catkin_ws
	rosdep install --from-paths src --ignore-src -r -y
	```
4. Build the workspace
	```bash
	catkin_make
	```

## Autonomous Obstacle Avoidance
1. Source your workspace
```bash
cd catkin_ws
source devel/setup.bash
```
2. Choose your preferred Turtlebot3 model using the proper keyword among `burger`, `waffle`, `waffle_pi` for the `TURTLEBOT3_MODEL` parameter
```bash
export TURTLEBOT3_MODEL=burger
```
3. Run the simulation in Turtlebot3 world
```bash
roslaunch obstacle_avoidance drive_turtlebot3.launch
```
4. Visualize simulation data in RViz
```bash
roslaunch obstacle_avoidance drive_turtlebot3.launch
```