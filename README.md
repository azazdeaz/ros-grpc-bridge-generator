:construction: wip

# gRPC API generator
## Experimental gRPC server generator.

This tool can snapshot the running ROS topics and services and build a matching gRPC server
 - The generated server will be implemented as a pyhton ROS package
 - Running topics and services will be saved in a snapshot.ini file which you can edit (or build manually) befor generating the gRPC server
 - It's implemented as a Jupyter notebook and a cookiecutter template so feel free to try changes and suggest modifications :)

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

## Usage
1. ### Start the necessary ROS nodes to make the topics and services visible.

2. ### Generate the server
```
roslaunch grpc_api_generator generate.launch
```
 - see the available arguments in the [generate.launch](launch/generate.launch)

3. ### Run the generated server
```
rosrun <generated pkg name (default=`grpc_api`)> run
```
 - Options: 
    - `address`: 'host:port: host and port of the gRPC server to connect to. default=`[::]:50051`

## Example

You can find an example catkin workspace at https://github.com/azazdeaz/ros-grpc-api-generator-example

## Development
The script is implemented as a Jupyter Notebook, so it's quite easy to poke around and tailor the generator for your project.

To launch the editor, just run:
```
rosrun grpc_api_generator notebook
```
Executing this notebook is equvalent to running `generate`.

## Tests

The end-to-end tests are a bunch of snapshot files in the test/snapshots folder and their pre-generated packages in the test/expected folder.

Running `rostest grpc_api_generator generate.test` will regenerate these packages in the result folder and compare them with the expected folder. It will fail for any changes. To update the tests just override the files in the expected folder.

To add a new test, copy a snapshot file in the test/snapshots, run the tests, and move the generated pkg from the result to the expected folder.

There are also some doctests in the generate.ipynb but only to make the development easier. They will run with the notebook.
