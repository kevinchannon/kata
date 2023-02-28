#include "cellular.hpp"

namespace ca {

  State make_initial_state(size_t size)
  {
    auto state = ca::State(size, ca::EMPTY);
    state[size / 2] = ca::FILLED;

    return state;
  }

  State next(State state, Rule rule) {
    return State(state.size(), EMPTY);
  }

}
