**Problem Statement**

Modify `hello-map.py` so that the eBPF code gets triggered by more than one
syscall. For example, `openat()` is commonly called to open files, and `write()` is
called to write data to a file. You can start by attaching the *hello* eBPF program to
multiple syscall kprobes. Then try having modified versions of the *hello* eBPF
program for different syscalls, demonstrating that you can access the same map
from multiple different programs.