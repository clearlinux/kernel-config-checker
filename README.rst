Kernel Config Checker (kcc)
===========================

.. contents:: **Table of Contents**
    :backlinks: none

Install
-------

.. code-block:: console

    pip install kcc

Usage
-----

Currently running kernel config (enabled with CONFIG_IKCONFIG_PROC).

.. code-block:: console

    zcat /proc/config.gz | kcc

Config from ``/boot``. Common on Debian based distros.

.. code-block:: console

    kcc /boot/config-$(uname -r)

Building kernel from source or release.

.. code-block:: console

    kcc .config

Hacking
-------

.. code-block:: console

    git clone https://github.com/clearlinux/kernel-config-checker kcc
    cd kcc
    pip install --user -e .

License
-------

kcc is distributed under the terms of the `GPL-3.0 License
<https://choosealicense.com/licenses/gpl-3.0>`_
