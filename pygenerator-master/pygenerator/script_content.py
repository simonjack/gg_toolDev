
SCRIPT = """#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if os.getenv('FROM_SOURCE') is not None:
    sys.path.insert(0, '..')
    sys.path.insert(0, '.')


def main():
    pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass


"""
