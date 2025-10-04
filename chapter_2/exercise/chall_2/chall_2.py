#!/usr/bin/python3
from bcc import BPF
from time import sleep

with open("./chall_2.c", "r") as fp:

  b = BPF(text=fp.read())
  syscall_opat = b.get_syscall_fnname("openat")
  syscall_wrt = b.get_syscall_fnname("write")

  b.attach_kprobe(event=syscall_opat, fn_name="fopen_cntr")
  b.attach_kprobe(event=syscall_wrt, fn_name="write_cntr")

  while True:
    sleep(2)
    s = []
    for k,v in b["counter_table"].items():
      if k.value == 101:
        s.append(f"Openat Count: {v.value}\t")
      elif k.value == 102:
        s.append(f"Write Count: {v.value}\t")
    print(''.join(s))
