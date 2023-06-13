#!/usr/bin/env python3
from brain_games import launcher
from brain_games.games import even


def main():
    launcher.start_game(even)


if __name__ == '__main__':
    main()
