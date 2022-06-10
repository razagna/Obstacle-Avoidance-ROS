## Set Up
### Dependencies
1. Follow the official ROS installation guide [here](http://wiki.ros.org/noetic/Installation/Ubuntu) (Gazebo included)
2. Install the ROS packages for Turtlebot3
```bash
sudo apt install ros-noetic-turtlebot3
```

### Workspace
1. Create workspace
```bash
mkdir -p catkin_ws/src
```
1. Get the `Turtle3` repository
```bash
cd catkin_ws/src
git clone --recursive https://github.com/razagna/Turtle3
```
1. Install any missing dependencies
```bash
cd ..
rosdep install --from-paths src --ignore-src -r -y
```
1. Build the workspace
```bash
catkin_make
```

## Autonomous Obstacle Avoidance
1. Open a new terminal in your workspace & source your workspace
```bash
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

### Parameters
- `show_rviz`: (bool) indicates whether to visualize the simulation data in RViz
- `forward_distance`: (float) minimum obstacle distance to the front
- `side_distance`: (float) minimum obstacle distance to the left & right
- `forward_speed`: (float) forward speed of the robot
- `angular_speed`: (float) angular speed of the robot