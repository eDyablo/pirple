cmake_minimum_required(VERSION 3.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(assignments)

add_executable(getting-to-know-your-ide getting-to-know-your-ide/main.cpp)

add_executable(data-types-and-variables data-types-and-variables/main.cpp)

add_executable(basic-input-and-output basic-input-and-output/main.cpp)

add_executable(conventions-and-operators conventions-and-operators/main.cpp)

add_executable(statements-switches-and-loops statements-switches-and-loops/main.cpp)

add_executable(tic-tac-toe tic-tac-toe/main.cpp)

add_executable(engine engine/main.cpp)
