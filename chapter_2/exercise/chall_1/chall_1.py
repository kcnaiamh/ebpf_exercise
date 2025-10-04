#!/usr/bin/python3
from bcc import BPF

# with open("./chall_1.c", "r") as fp:

# b = BPF(text=fp.read())
b = BPF(src_file="chall_1.c")
syscall = b.get_syscall_fnname("execve")
b.attach_kprobe(event=syscall, fn_name="hello")


def print_event(cpu, data, size):
  data = b["output"].event(data)
  print(f"{data.pid} {data.uid} {data.command.decode()} {data.message.decode()}")


b["output"].open_perf_buffer(print_event)
while True:
  b.perf_buffer_poll()
