#! /usr/bin/python3

# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import argparse
import os
import time

FORMAT_COMMAND = 'clang-format -i -style=file'
FILE_TARGETS = ['.cpp', '.h', '.hpp', '.cc', '.cxx']

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    END = '\033[0m'


class Timer:
    def __init__(self):
        self.tics = [time.perf_counter()]

    def add_tic(self) -> None:
        self.tics.append(time.perf_counter())

    def get_elapsed(self) -> str:
        try:
            return str('{:.3f}'.format(self.tics[-1] - self.tics[-2]))
        except IndexError:
            print('Elapsed is null')


def do_format_file(fname: str) -> bool:
    for target in FILE_TARGETS:
        if fname.endswith(target):
            return True

    return False


def format_current_dir() -> None:
    file_count = 0
    formatting_timer = Timer()

    for dirpath, _, filenames in os.walk('.'):
        for filename in filenames:
            if do_format_file(filename):
                print(f'Formatting {filename}...')
                os.system(f'{FORMAT_COMMAND} {dirpath}/{filename}')
                file_count += 1

    formatting_timer.add_tic()
    desired_color = Colors.GREEN if file_count > 0 else Colors.YELLOW

    print(f'{desired_color}Formatted {file_count} files in {formatting_timer.get_elapsed()}{Colors.END}')


def search_for_src() -> bool:
    for dirpath, _, _ in os.walk('.'):
        if 'src' in dirpath:
            answer = input(f'Found src/ in ~{os.getcwd()}/\nIs this the desired directory? [y/n]: ')

            if answer != 'y' and answer != 'Y':
                answer = input('Continue search? [y/n]: ')

                if answer != 'y' and answer != 'Y':
                    return True
            else:
                print(f'Formatting directory {dirpath}...')
                format_current_dir()
                return True


def walk_up_dir() -> None:
    backup_count = 0
    MAX_REASONABLE_BACKUPS = 8

    while backup_count <= MAX_REASONABLE_BACKUPS:
        if search_for_src():
            break
        else:
            backup_count += 1
            os.chdir('../')

        if backup_count >= MAX_REASONABLE_BACKUPS:
            print(f'{Colors.YELLOW}Warning: Reached {MAX_REASONABLE_BACKUPS} backups without finding src/{Colors.END}')
            answer = input('Continue search? [y/n]: ')

            if answer == 'y' or answer == 'Y':
                print('Resetting backup count...')
                backup_count = 0
                print('Continuing search...')
                continue
            else:
                print('Exiting...')
                return


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--up', action='store_true', help='Walk up directories to find the first src/ directory')
    args = parser.parse_args()

    if args.up:
        walk_up_dir()
    else:
        format_current_dir()


if __name__ == '__main__':
    main()