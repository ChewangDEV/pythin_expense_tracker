from tracker import Tracker


def main():
    tracker = Tracker()
    is_on = True

    while is_on:
        is_on = tracker.menu()


if __name__ == "__main__":
    main()
