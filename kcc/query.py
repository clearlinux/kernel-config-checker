'''
Copyright (C) 2018 Intel Corporation

SPDX-License-Identifier: GPL-3.0

Scrape best known kernel config settings from the KSPP WiKi.
'''

import re
import urllib.request
from typing import Tuple, Dict

KSPP_URL = 'https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings'

def KernelSelfProtectionProject():
    with urllib.request.urlopen(KSPP_URL) as f:
        if f.code != 200:
            raise ValueError('Failed to retrieve secure config options')
        text = f.read().decode()
        # Map id's from right before the <pre> tag to their contents
        return kspp_gen_config(dict(zip(
            [block.split('id=')[-1].split('"')[1].strip() \
                    for block in text.split('>\n<pre>')],
            [block[:-2] for block in text.split('pre>') \
                    if block.endswith('</')])))

def kspp_gen_config(sections_and_configs: Dict[str, str]) \
        -> Tuple[Dict[str, str], Dict[str, str], Dict[str, str]]:
    must_be_set: Dict[str, str] = {}
    must_be_set_or_module: Dict[str, str] = {}
    must_be_unset: Dict[str, str] = {}
    data = sections_and_configs['CONFIGs'] + sections_and_configs['x86_64']
    lines = data.split('\n')
    comment = 0
    for i in range(0, len(lines)):
        line = lines[i]
        if line.startswith('#') \
                and not line.startswith('# CONFIG_'):
            comment = i
        if i == comment:
            continue
        if 'is not set' in line:
            opt = 'CONFIG_' + line.split('CONFIG_')[1].split()[0]
            must_be_unset[opt] = lines[comment].replace('#', '').strip()
        elif line.endswith('=y'):
            opt = 'CONFIG_' + line.split('CONFIG_')[1].split('=')[0]
            must_be_set[opt] = lines[comment].replace('#', '').strip()
        elif line.endswith('=m'):
            opt = 'CONFIG_' + line.split('CONFIG_')[1].split('=')[0]
            must_be_set_or_module[opt] = lines[comment].replace('#',
                    '').strip()
    # KSPP Recommends disabling modules. Which is not realistic.
    if 'CONFIG_MODULES' in must_be_unset:
        del must_be_unset['CONFIG_MODULES']
    return must_be_set, must_be_set_or_module, must_be_unset
