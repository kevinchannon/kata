
cmake_minimum_required (VERSION 3.15)

project ("cellular")

set(CMAKE_CXX_STANDARD 20)

add_executable(cellular_automata
  "main.cpp"
)

set_property(TARGET cellular_automata PROPERTY CXX_STANDARD 20)

target_include_directories(cellular_automata
  PRIVATE
    cellular
)

# Include sub-projects.
add_subdirectory ("cellular")

target_link_libraries(cellular_automata
  libcellular
)
