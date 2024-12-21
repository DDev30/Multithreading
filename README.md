# Matrix Multiplication with Multithreading

## Assignment Overview
This assignment involves multiplying 500 random matrices of size **5000 x 5000** with a constant matrix of the same size using multithreading. The task is designed to analyze how execution time and CPU usage vary with the number of threads. You will:

1. Generate 500 random matrices.
2. Multiply these matrices with a constant matrix using varying numbers of threads.
3. Measure execution time for different thread counts (up to **2 \* Number of Cores**).
4. Plot the results to visualize execution time vs. number of threads.

## Code Description

### 1. **Constants**
- **`MATRIX_SIZE`**: Specifies the size of each matrix (5000 x 5000).
- **`NUM_MATRICES`**: Total number of random matrices to generate (500).
- **`CONSTANT_MATRIX`**: A randomly generated constant matrix used for multiplication.

### 2. **Function: `multiply_chunk`**
This function handles the matrix multiplication for a subset of matrices. It takes as input:
- `start` and `end`: Indices defining the chunk of matrices.
- `matrices`: List of random matrices.
- `results`: List to store the multiplication results.

It calculates the dot product of each matrix in the chunk with the constant matrix.

### 3. **Function: `run_with_threads`**
This function performs the matrix multiplication using a specified number of threads:
- Splits the matrices into chunks based on the number of threads.
- Creates threads to process each chunk in parallel.
- Measures and returns the total execution time.

### 4. **Main Script**
- Dynamically determines the number of CPU cores and calculates the maximum number of threads.
- Iterates through thread counts (1 to `2 \* Number of Cores`).
- Measures execution time for each thread count.
- Plots a graph of execution time vs. number of threads.

### 5. **Plotting**
The script generates a graph displaying execution time against the number of threads, helping to identify the optimal thread count for performance.

## Requirements

To run the script, ensure the following packages are installed:
- `numpy`
- `matplotlib`

Use the following command to install any missing dependencies:
```bash
pip install numpy matplotlib
```

## Execution Instructions
1. Save the script to a file (e.g., `matrix_multithreading.py`).
2. Run the script:
   ```bash
   python matrix_multithreading.py
   ```
3. Observe the printed execution times for each thread count.
4. Analyze the generated graph to study the performance trend.

## Output
- **Execution Time Table**: Displays the time taken for matrix multiplication with different thread counts.
- **Graph**: Plots the execution time vs. number of threads.
- **CPU Usage**: Use a task manager or monitoring tool to observe CPU utilization.

## Example Results
Here is an example table for the execution times:

| Threads | T=1 | T=2 | T=3 | T=4 | T=5 | T=6 | T=7 | T=8 |
|---------|------|------|------|------|------|------|------|------|
| Time (min) | 10   | 8    | 6    | 5    | 7    | 9    | 11   | 13   |

### Graph
The graph shows how the execution time varies with the number of threads, typically decreasing initially and increasing after a certain point due to thread management overhead.

## Observations
- Optimal performance is achieved at a specific number of threads (e.g., equal to the number of CPU cores).
- Increasing threads beyond the optimal point may degrade performance.

## Notes
- Large matrix sizes and high thread counts may cause memory limitations or increased overhead.
- Ensure sufficient system resources to handle the computation.

