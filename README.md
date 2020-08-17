:construction: wip

## Install
Clone the repo into a catkin workspace:
```sh
# in your_catkit_ws/src
git clone git@github.com:azazdeaz/ros-grpc-api-generator.git
```
and run rosdep install
```sh
# in your_catkit_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

## Basic Usage
First, start the necessary ROS nodes to make the topics and services visible.

To generate the server
```
rosrun grpc_api_generator generate
```

To run the generated server
```
rosrun grpc_api_generator run_server
```

## Development
The script is implemented as a Jupyter Notebook, so it's quite easy to poke around and tailor the generator for your project.

To launch the editor, just run:
```
rosrun grpc_api_generator notebook
```
Executing this notebook is equvalent to running `generate`.