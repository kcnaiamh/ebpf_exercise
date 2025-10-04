#!/usr/bin/python3
from bcc import BPF
from time import sleep

with open("./chall_5.c", "r") as fp:

  b = BPF(text=fp.read())
  b.attach_raw_tracepoint(tp="sys_enter", fn_name="hello")

  while True:
    sleep(2)
    s = []
    for k,v in b["counter_table"].items():
      s.append(f"Syscall ID {k.value}: {v.value}\t")
    s.append("\n")
    print(''.join(s))