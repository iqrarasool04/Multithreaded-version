import time

num_steps = 100000
steps = 1.0 / float(num_steps)

start_time = time.time()
sum_val = 0.0

for i in range(num_steps):
    x = (i + 0.5) * steps
    sum_val += 4.0 / (1.0 + x * x)

pi = steps * sum_val

print("PI:", pi)

end_time = time.time()
time_taken = (end_time - start_time) * 1e6
print("PI calculation took", time_taken, "microseconds to run.")
