# CMakeList.txt : CMake project for cellular, include source and define
# project specific logic here.
#
include(FetchContent)

add_library(libcellular "cellular.cpp")
add_executable(tests "cellular.tests.cpp")

set_property(TARGET libcellular PROPERTY CXX_STANDARD 20)
set_property(TARGET tests PROPERTY CXX_STANDARD 20)

FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG v3.3.1
)

FetchContent_MakeAvailable(Catch2)

target_link_libraries(tests
  Catch2::Catch2WithMain
  libcellular
)
