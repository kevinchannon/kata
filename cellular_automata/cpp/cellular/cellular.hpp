#pragma once

#include <string>
#include <cstdint>

namespace ca {

  using Cell = char;
  constexpr auto EMPTY = Cell(0x20);
  constexpr auto FILLED = Cell(0xFE);

  using State = std::string;
  using Rule = uint8_t;

  [[nodiscard]] State make_initial_state(size_t size);
  [[nodiscard]] State next(State state, Rule rule);
}
