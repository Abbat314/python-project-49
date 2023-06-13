#!/usr/bin/env python3
from brain_games import launcher
from brain_games.games import gcd


def main():
    launcher.start_game(gcd)


if __name__ == '__main__':
    main()
