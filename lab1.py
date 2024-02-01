import time

num_Steps = 1000
steps = 1/num_Steps

start = time.time()
for i in num_Steps:
    x = (i + 0.5) * steps
    sum = sum + 4.0 / (1 + x*x)

pi = steps * sum
print("PI ",pi)
end = time.time()

execution_time = end - start
print("PI calculation took ", execution_time)
