#include "tenpin.hpp"

#include <catch2/catch_test_macros.hpp>

TEST_CASE("score tests") {
  SECTION("20 gutter balls returns zero") {
    REQUIRE(0 == ten_pin::score("00 00 00 00 00 00 00 00 00 00"));
  }
}
