cmake_minimum_required (VERSION 3.15)

project ("bowlingscorer")

set(CMAKE_CXX_STANDARD 20)

add_executable (bowlingscorer
  "main.cpp"
)

target_include_directories(bowlingscorer
  PRIVATE
    "bowlingscorer"
)

set_property(TARGET bowlingscorer PROPERTY CXX_STANDARD 20)

# Include sub-projects.
add_subdirectory ("bowlingscorer")

target_link_libraries(bowlingscorer
  libbowl
)
