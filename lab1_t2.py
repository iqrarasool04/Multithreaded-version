import time
import threading

num_steps = 100000
num_threads = 4  
steps = 1.0 / float(num_steps)

def calculate_partial_sum(start, end, result):
    partial_sum = 0.0
    for i in range(start, end):
        x = (i + 0.5) * steps
        partial_sum += 4.0 / (1.0 + x * x)
    result.append(partial_sum)

start_time = time.time()
thread_list = []
partial_sums = []

for i in range(num_threads):
    start_index = i * (num_steps // num_threads)
    end_index = (i + 1) * (num_steps // num_threads) if i != num_threads - 1 else num_steps
    thread = threading.Thread(target=calculate_partial_sum, args=(start_index, end_index, partial_sums))
    thread_list.append(thread)
    thread.start()
for thread in thread_list:
    thread.join()

pi = steps * sum(partial_sums)

print("PI:", pi)

end_time = time.time()
time_taken = (end_time - start_time) * 1e6  # Convert seconds to microseconds
print("PI calculation took", time_taken, "microseconds to run with", num_threads, "threads.")
