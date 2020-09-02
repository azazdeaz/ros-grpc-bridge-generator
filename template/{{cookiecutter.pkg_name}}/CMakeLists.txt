cmake_minimum_required(VERSION 3.0.2)
project({{cookiecutter.pkg_name}})

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package()

catkin_install_python(PROGRAMS
  nodes/server
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_python_setup()

include_directories(
  ${catkin_INCLUDE_DIRS}
)