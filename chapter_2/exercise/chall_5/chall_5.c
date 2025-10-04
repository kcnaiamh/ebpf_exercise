#pragma clang diagnostic ignored "-Wint-conversion"
BPF_PROG_ARRAY(syscall, 300);
BPF_HASH(counter_table);

int hello(struct bpf_raw_tracepoint_args *ctx) {
  u64 opcode;
  u64 counter = 0;
  u64 *p;

  opcode = ctx->args[1];
  p = counter_table.lookup(&opcode);
  if (p != 0) {
    counter = *p;
  }
  counter++;
  counter_table.update(&opcode, &counter);
  return 0;
}