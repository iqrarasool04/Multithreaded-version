import time
import threading

def piCalculation(start, end, steps, result):
    sum = 0.0
    for i in range(start, end):
        x = (i + 0.5) * steps
        sum += 4.0 / (1 + x*x)
    result.append(sum)

def main():
    num_steps = 1000
    num_threads = 4  

    steps = 1 / num_steps
    sums = []

    start_time = time.perf_counter()

    threads = []
    for i in range(num_threads):
        start = i * (num_steps // num_threads)
        end = (i + 1) * (num_steps // num_threads)
        thread = threading.Thread(target=piCalculation, args=(start, end, steps, sums))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi = steps * sum(sums)
    print("PI ", pi)

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1e6
    print("PI calculation took ", execution_time, " microseconds to run.")

if __name__ == "__main__":
    main()
