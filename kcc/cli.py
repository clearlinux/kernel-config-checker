'''
Copyright (C) 2018 Intel Corporation

SPDX-License-Identifier: GPL-3.0

cli for kernel config checker
'''
import sys
import argparse
from typing import Iterator

from .kconfig import Kconfig
from .query import KernelSelfProtectionProject
from .defaults import MUST_BE_SET, MUST_BE_SET_OR_MODULE, MUST_BE_UNSET

def run(*,
        config_file: str = '',
        query: bool = False,
        missings: bool = False):
    if query:
        must_be_set, must_be_set_or_module, must_be_unset = \
                KernelSelfProtectionProject()
        must_be_set.update(MUST_BE_SET)
        must_be_set_or_module.update(MUST_BE_SET_OR_MODULE)
        must_be_unset.update(MUST_BE_UNSET)

    kconfig = Kconfig.default()
    results, missing_keys = kconfig.check(config_file)
    if not results and not missing_keys:
        return
    for opt, msg in results.items():
        print(opt, msg)
    if missings:
        for key in missing_keys:
            print(key)
    return 1

def cli() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file', nargs='?', type=argparse.FileType('r'),
            default=sys.stdin)
    parser.add_argument('--query', default=False, action='store_true')
    parser.add_argument('--missings', default=False, action='store_true')
    args = parser.parse_args()
    ret = run(**vars(args))
    args.config_file.close()
    if isinstance(ret, int):
        sys.exit(ret)
