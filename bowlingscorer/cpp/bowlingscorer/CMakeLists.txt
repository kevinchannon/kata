include(FetchContent)

add_library(libbowl
  "tenpin.cpp"
)

add_executable(tests
  "tenpin.tests.cpp"
)

FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG v3.3.1
)

FetchContent_MakeAvailable(Catch2)

set_property(TARGET tests PROPERTY CXX_STANDARD 20)

target_link_libraries(tests
  Catch2::Catch2WithMain
  libbowl
)
