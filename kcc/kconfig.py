'''
Copyright (C) 2018 Intel Corporation

SPDX-License-Identifier: GPL-3.0

Check a kernel config file against a set of best known settings
See also https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings
'''

import re
import sys
from typing import Dict, Iterable

from .defaults import MUST_BE_SET, MUST_BE_SET_OR_MODULE, MUST_BE_UNSET

class Kconfig(object):
    '''
    Reads and checks a kernel config file.
    '''

    N_MUST_Y = "is not set but is required to be set to y (%s)"
    N_MUST_Y_OR_M = "is not set but is required to be set to y or m (%s)"
    Y_MUST_N = "is set but is required to be not set (%s)"
    M_MUST_Y = "is set as =m but is required to be set to y (%s)"
    M_MUST_N = "is set as =m but is required to be not set (%s)"

    def __init__(self, *,
            must_be_set: Dict[str, str] = {},
            must_be_set_or_module : Dict[str, str] = {},
            must_be_unset: Dict[str, str] = {}) -> None:
        self.must_be_set = must_be_set
        self.must_be_set_or_module = must_be_set_or_module
        self.must_be_unset = must_be_unset

    @classmethod
    def default(cls):
        return cls(must_be_set=MUST_BE_SET,
                   must_be_set_or_module=MUST_BE_SET_OR_MODULE,
                   must_be_unset=MUST_BE_UNSET)

    def check(self, stream: Iterable[str]) -> Dict[str, str]:
        results: Dict[str, str] = {}
        for line in stream:
            results.update(self.check_line(line))
        return results

    def check_line(self, line: str) -> Dict[str, str]:
        line = line.strip()
        match = re.search("^# (CONFIG_.*) is not set", line)
        if match:
            notset = match.group(1)
            if notset in self.must_be_set:
                return {notset: self.N_MUST_Y % \
                        (self.must_be_set[notset])}
            if notset in self.must_be_set_or_module:
                return {notset: self.N_MUST_Y_OR_M % \
                        ('', self.must_be_set_or_module[notset])}
        match = re.search("^(CONFIG_.*)=y", line)
        if match:
              notset = match.group(1)
              if notset in self.must_be_unset:
                    return {notset: self.Y_MUST_N % \
                            (self.must_be_unset[notset])}
        match = re.search("^(CONFIG_.*)=m", line)
        if match:
            notset = match.group(1)
            if notset in self.must_be_set:
                return {notset: self.M_MUST_Y % \
                        (self.must_be_set[notset])}
            if notset in self.must_be_unset:
                return {notset: self.M_MUST_N % \
                        (self.must_be_unset[notset])}
        return {}
