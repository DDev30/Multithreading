import threading
import numpy as np
import time
import os
import matplotlib.pyplot as plt

# Constants
MATRIX_SIZE = 5000
NUM_MATRICES = 500
CONSTANT_MATRIX = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)

# Function to multiply a chunk of matrices
def multiply_chunk(start, end, matrices, results):
    for i in range(start, end):
        results[i] = np.dot(matrices[i], CONSTANT_MATRIX)

# Function to run the task with a specific number of threads
def run_with_threads(num_threads):
    matrices = [np.random.rand(MATRIX_SIZE, MATRIX_SIZE) for _ in range(NUM_MATRICES)]
    results = [None] * NUM_MATRICES
    threads = []
    chunk_size = NUM_MATRICES // num_threads

    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else NUM_MATRICES
        thread = threading.Thread(target=multiply_chunk, args=(start, end, matrices, results))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return time.time() - start_time

# Main script
num_cores = os.cpu_count()  # Get the number of CPU cores
max_threads = 2 * num_cores
execution_times = []

print(f"Running with up to {max_threads} threads...")
for threads in range(1, max_threads + 1):
    time_taken = run_with_threads(threads)
    execution_times.append(time_taken)
    print(f"Threads: {threads}, Time: {time_taken:.2f} seconds")

# Plot the results
plt.plot(range(1, max_threads + 1), execution_times, marker='o')
plt.title('Execution Time vs Number of Threads')
plt.xlabel('Number of Threads')
plt.ylabel('Time Taken (seconds)')
plt.grid()
plt.show()
