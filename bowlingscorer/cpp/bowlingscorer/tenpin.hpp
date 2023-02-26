#pragma once

#include <cstdint>
#include <string_view>

namespace ten_pin {
  [[nodiscard]] uint16_t score(std::string_view pins_knocked_down);
}