cmake_minimum_required(VERSION 3.0.2)
project(grpc_api_generator)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package()


include_directories(
  ${catkin_INCLUDE_DIRS}
)


if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(test/generate.test)
endif()

