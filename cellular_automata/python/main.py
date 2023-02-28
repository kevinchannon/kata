from cellular import cellular


ITERATIONS = 50
SIZE = 61
RULE = 30


def main():
    state = cellular.make_initial_state(SIZE)
    print(state)

    for _ in range(ITERATIONS):
        state = cellular.next_state(state, RULE)
        print(state)


if __name__ == '__main__':
    main()
