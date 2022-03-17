# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import argparse


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='List of commands')

list_parser = subparsers.add_parser('list', help='list contents')
list_parser.add_argument('dirname', action='store', help='Directory to list')

create_parser = subparsers.add_parser('create', help='Create a directory')
create_parser.add_argument('dirname', action='store', help='new directory to create')
create_parser.add_argument(
    '--read-only',
    default=False,
    action='store_true',
    help='Set permissions to prevent writing to the directory'
)
