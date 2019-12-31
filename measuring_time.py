# correct example
import time

start = time.monotonic()
time.sleep(5)  # 5 sec
print(f"Time is {time.monotonic() - start}")


# not correct
import time

start = time.time()
time.sleep(5)  # 5 sec
print(f"Time is {time.time() - start}")
