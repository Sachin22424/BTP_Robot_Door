# door_state_estimation

This package contains a ROS node that estimates the state of a door using a Bayesian filter.

## Requirements

- ROS (Robot Operating System)
- turtlesim

## How to run the code

```bash
# 1. Build the workspace
cd ~/catkin_ws
catkin_make

# 2. Source the workspace
source devel/setup.bash

# 3. Make sure the script is executable
chmod +x src/door_state_estimation/scripts/turtle_door_bayes.py

# 4. Start ROS core (Terminal 1)
roscore

# 5. Start turtlesim (Terminal 2)
rosrun turtlesim turtlesim_node

# 6. Run the turtle door Bayes filter demo (Terminal 3)
rosrun door_state_estimation turtle_door_bayes.py
```

## How to clone and run this code in a new workspace

```bash
# Clone the repository
cd ~
git clone https://github.com/Sachin22424/BTP_Robot_Door.git

# Create a new catkin workspace and add the package
mkdir -p ~/catkin_ws/src
cp -r ~/BTP_Robot_Door/door_state_estimation ~/catkin_ws/src/

# Build and run as above
cd ~/catkin_ws
catkin_make
source devel/setup.bash
chmod +x src/door_state_estimation/scripts/turtle_door_bayes.py
roscore
rosrun turtlesim turtlesim_node
rosrun door_state_estimation turtle_door_bayes.py
```