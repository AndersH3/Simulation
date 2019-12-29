cmake_minimum_required(VERSION 2.6)
project(simulation)

add_executable(simulation main.cpp)

install(TARGETS simulation RUNTIME DESTINATION bin)
