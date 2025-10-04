#!/usr/bin/python3
# -*- coding: utf-8 -*-
from bcc import BPF
import ctypes as ct

with open("./hello-buffer-config.c", "r") as fp:

  b = BPF(text=fp.read())
  syscall = b.get_syscall_fnname("execve")
  b.attach_kprobe(event=syscall, fn_name="hello")
  b["config"][ct.c_int(0)] = ct.create_string_buffer(b"Hey root!")
  b["config"][ct.c_int(1000)] = ct.create_string_buffer(b"Hi user 1000!")

  def print_event(cpu, data, size):
    data = b["output"].event(data)
    print(f"{data.pid} {data.uid} {data.command.decode()} {data.message.decode()}")

  b["output"].open_perf_buffer(print_event)
  while True:
    b.perf_buffer_poll()