'''
Copyright (C) 2018 Intel Corporation

SPDX-License-Identifier: GPL-3.0

Kernel config checker defaults for what must be set and what must not be set
'''
from typing import Dict

MUST_BE_SET: Dict[str, str] = {}
MUST_BE_SET_OR_MODULE: Dict[str, str] = {}
MUST_BE_UNSET: Dict[str, str] = {}

MUST_BE_SET["CONFIG_RANDOMIZE_BASE"] = "KASLR is required as a basic security hardening"
MUST_BE_SET["CONFIG_RANDOMIZE_MEMORY"] = "KASLR is required as a basic security hardening"
MUST_BE_SET["CONFIG_STRICT_KERNEL_RWX"] = "NX is important for buffer overflow exploit hardening"
MUST_BE_SET["CONFIG_CC_STACKPROTECTOR"] = "Stack Protector is for buffer overflow detection and hardening"
MUST_BE_SET["CONFIG_STACKPROTECTOR"] = "Stack Protector is for buffer overflow detection and hardening"

MUST_BE_UNSET["CONFIG_DEVMEM"] = "/dev/mem is dangerous and has no legitimate users anymore"

MUST_BE_SET["CONFIG_DEBUG_CREDENTIALS"] = "Needed to protect against targeted corruption by rootkits"
MUST_BE_SET["CONFIG_DEBUG_NOTIFIERS"] = "Needed to protect against targeted corruption by rootkits"
MUST_BE_SET["CONFIG_DEBUG_LIST"] = "Needed to protect against targeted corruption by rootkits"
MUST_BE_SET["CONFIG_DEBUG_SG"] = "Needed to protect against targeted corruption by rootkits"
MUST_BE_SET["CONFIG_SCHED_STACK_END_CHECK"] = "Needed to protect against targeted corruption by rootkits"
MUST_BE_SET["CONFIG_RETPOLINE"] = "Needed to protect against Spectre V2"


MUST_BE_SET["CONFIG_SECCOMP"] = "Seccomp is a security feature needed by systemd"
MUST_BE_SET["CONFIG_SECCOMP_FILTER"] = "Seccomp is a security feature needed by systemd"

MUST_BE_SET["CONFIG_HARDENED_USERCOPY"] = "Protect against ioctl buffer overflows"
MUST_BE_UNSET["CONFIG_HARDENED_USERCOPY_FALLBACK"] = "Protect against ioctl buffer overflows"

MUST_BE_SET["CONFIG_SLAB_FREELIST_RANDOM"] = "Harden the slab free list with randomization"
MUST_BE_SET["CONFIG_SLAB_FREELIST_HARDENED"] = "Harden the slab free list with randomization"

MUST_BE_SET["CONFIG_VMAP_STACK"] = "Guard pages for kernel stacks"

MUST_BE_SET["CONFIG_REFCOUNT_FULL"] = "Perform extensive checks on reference counting"
MUST_BE_SET["CONFIG_FORTIFY_SOURCE"]= "Check for memory copies that might overflow a structure in str*() and mem*() functions both at build-time and run-time."
MUST_BE_UNSET["CONFIG_ACPI_CUSTOM_METHOD"] = "Dangerous; enabling this allows direct physical memory writing"
MUST_BE_UNSET["CONFIG_COMPAT_BRK"] = "Dangerous; enabling this disables brk ASLR"
MUST_BE_UNSET["CONFIG_DEVKMEM"] = "Dangerous; enabling this allows direct kernel memory writing."
MUST_BE_UNSET["CONFIG_PROC_KCORE"] = "Dangerous; exposes kernel text image layout"
MUST_BE_UNSET["CONFIG_COMPAT_VDSO"] = "Dangerous; enabling this disables VDSO ASLR"
MUST_BE_UNSET["CONFIG_INET_DIAG"] = "Prior to v4.1, assists heap memory attacks; best to keep interface disabled"
MUST_BE_UNSET["CONFIG_LEGACY_PTYS"] = "Use the modern PTY interface (devpts) only"
MUST_BE_SET["CONFIG_DEBUG_SET_MODULE_RONX"] = "Ensure modules have NX enabled"
MUST_BE_SET["CONFIG_STRICT_MODULE_RWX"] = "Ensure modules have NX enabled"
MUST_BE_SET["CONFIG_MODULE_SIG"] = "Signing of kernel modules is required"
MUST_BE_SET["CONFIG_MODULE_SIG_FORCE"] = "Enforce module signing"
MUST_BE_SET["CONFIG_MODULE_SIG_SHA512"] = "Use SHA512 for kernel module signing"

MUST_BE_SET["CONFIG_LEGACY_VSYSCALL_NONE"] = "Modern libc no longer needs a fixed-position mapping in userspace, remove it as a possible target."
MUST_BE_SET["CONFIG_PAGE_TABLE_ISOLATION"] = "Enable Kernel Page Table Isolation to remove an entire class of cache timing side-channels."
MUST_BE_UNSET["CONFIG_X86_X32"] = "X32 is rarely used and provides only attack surface"
MUST_BE_UNSET["CONFIG_MODIFY_LDT_SYSCALL"] = "Unused dangerous option"
