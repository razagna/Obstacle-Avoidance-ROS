## Set Up
### Dependencies
1. Follow the official ROS Noetic installation guide [here](http://wiki.ros.org/noetic/Installation/Ubuntu) (Gazebo included)
2. Install the ROS packages for **TurtleBot3**
```bash
sudo apt install ros-noetic-turtlebot3
```

### Workspace
1. Create a workspace
```bash
mkdir -p catkin_ws/src
cd catkin_ws/src
```
2. Clone this repository
```bash
git clone --recursive https://github.com/razagna/Obstacle-Avoidance-ROS
```
3. Install any missing dependencies
```bash
cd ..
rosdep install --from-paths src --ignore-src -r -y
```
4. Build the workspace
```bash
catkin_make
```

## Autonomous Obstacle Avoidance
1. Open a new terminal & source your workspace
```bash
source devel/setup.bash
```
2. Choose your preferred **TurtleBot3** model using the proper keyword among `burger`, `waffle` & `waffle_pi`
```bash
export TURTLEBOT3_MODEL=burger
```
3. Run the simulation in the standard world
```bash
roslaunch obstacle_avoidance drive_turtlebot3.launch
```

### Parameters
- `show_rviz`: (bool) indicates whether to visualize the simulation data in RViz
- `forward_distance`: (float) minimum obstacle distance to the front
- `side_distance`: (float) minimum obstacle distance to the left & right
- `forward_speed`: (float) forward speed of the robot
- `angular_speed`: (float) angular speed of the robot
