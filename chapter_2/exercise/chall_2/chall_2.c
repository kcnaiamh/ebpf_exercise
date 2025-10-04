BPF_HASH(counter_table);

int fopen_cntr(void *ctx) {
  u64 counter = 0;
  u64 key = 101;
  u64 *p;

  p = counter_table.lookup(&key);
  if (p != 0) {
    counter = *p;
  }
  counter++;
  counter_table.update(&key, &counter);
  return 0;
}

int write_cntr(void *ctx) {
  u64 counter = 0;
  u64 key = 102;
  u64 *p;

  p = counter_table.lookup(&key);
  if (p != 0) {
    counter = *p;
  }
  counter++;
  counter_table.update(&key, &counter);
  return 0;
}