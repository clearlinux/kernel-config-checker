Kernel Config Checker (kcc)
===========================

**STOP** (*hammer time*) **this project hasn't been maintained as well as we'd like. We've archived it in favor of** `Alexander Popov's <https://github.com/a13xp0p0v>`_  **https://github.com/a13xp0p0v/kconfig-hardened-check. More info here: https://linuxplumbersconf.org/event/7/contributions/775/**

::

  DISCONTINUATION OF PROJECT.  This project will no longer be maintained
  by Intel.  Intel will not provide or guarantee development of or
  support for this project, including but not limited to, maintenance,
  bug fixes, new releases or updates.  Patches to this project are no
  longer accepted by Intel.  If you have an ongoing need to use this
  project, are interested in independently developing it, or would like
  to maintain patches for the community, please create your own fork of
  the project.

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
