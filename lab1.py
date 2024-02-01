import time

num_Steps = 1000
steps = 1/num_Steps
sum = 0.0

start = time.perf_counter()
for i in range(num_Steps):
    x = (i + 0.5) * steps
    sum = sum + 4.0 / (1 + x*x)

pi = steps * sum
print("PI ",pi)
end = time.perf_counter()

execution_time = (end - start) * 1e6
print("PI calculation took ", execution_time, " microsec to run.")
