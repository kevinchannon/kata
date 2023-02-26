from tenpin import tenpin


def main():
    pins_knocked_down = input("Enter pins knocked down in each frame:")
    print(f"Game score = {tenpin.score(pins_knocked_down)}")


if __name__ == '__main__':
    main()
