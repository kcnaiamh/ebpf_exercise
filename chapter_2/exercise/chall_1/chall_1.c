BPF_PERF_OUTPUT(output);

struct data_t {
  int pid;
  int uid;
  char command[16];
  char message[12];
};

static __always_inline void strcpy(char *msg_dst, char *msg_src) {
  int i = 0;
  while (msg_src[i] != '\0') {
    msg_dst[i] = msg_src[i];
    i++;
  }
  msg_dst[i] = '\0';
}

int hello(void *ctx) {
  struct data_t data = {};
  char message[5];

  data.pid = bpf_get_current_pid_tgid() >> 32;
  data.uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;

  if (data.pid & 1) {
    strcpy(message, "ODD\0");
  } else {
    strcpy(message, "EVEN\0");
  }

  bpf_get_current_comm(&data.command, sizeof(data.command));
  bpf_probe_read_kernel(&data.message, sizeof(data.message), message);

  output.perf_submit(ctx, &data, sizeof(data));

  return 0;
}