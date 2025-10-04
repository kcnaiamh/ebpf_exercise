The RAW_TRACEPOINT_PROBE macro provided by BCC simplifies attaching to raw tracepoints, telling the user space BCC code to automatically attach it to a specified tracepoint. Try it in hello-tail.py, like this:

- Replace the definition of the hello() function with RAW_TRACEPOINT_PROBE(sys_enter).
- Remove the explicit attachment call b.attach_raw_tracepoint() from the Python code.

You should see that BCC automatically creates the attachment and the program works exactly the same. This is an example of the many convenient macros that BCC provides.