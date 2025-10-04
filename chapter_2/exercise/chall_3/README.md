**Problem Statement**

The hello-tail.py eBPF program is an example of a program that attaches to the
sys_enter raw tracepoint that is hit whenever any syscall is called. Change hello-
map.py to show the total number of syscalls made by each user ID, by attaching it
to that same sys_enter raw tracepoint.


If you found any issue (you will be), go to this link: https://github.com/lizrice/learning-ebpf/issues/21