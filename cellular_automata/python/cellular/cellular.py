Cell = str
EMPTY = " "
FILLED = "@"

Rule = int
State = str


def make_initial_state(size: int) -> State:
    out = [EMPTY for _ in range(size)]
    out[size // 2] = FILLED

    return "".join(out)


def next_state(state: State, rule: Rule) -> State:
    return EMPTY * len(state)
