import time
import resource


def trapezoidal_rule(a: float, b: float, n: int, func: callable) -> float:
    """
    Calculate the integral of `func` over the interval [a, b] using the trapezoidal rule with n segments.
    """
    h = (b - a) / n
    result = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        result += func(a + i * h)
    return result * h


def calculate_time_memory_trapezoidal(
    a: float, b: float, n: int, func: callable
) -> tuple:
    """
    Calculate the integral using the trapezoidal rule and measure the time and memory usage.

    Parameters:
    - a (float): Start of the interval.
    - b (float): End of the interval.
    - n (int): Number of segments.
    - func (callable): Function to integrate.

    Returns:
    - result (float): The calculated integral.
    - memory_usage_change (int): Change in memory usage (in kilobytes).
    - elapsed_time (float): Time taken for the calculation (in seconds).
    """
    # Start time and memory usage
    start_time = time.time()
    start_mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    # Perform the integration
    result = trapezoidal_rule(a, b, n, func)

    # End time and memory usage
    end_time = time.time()
    end_mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    # Calculate elapsed time and memory usage change
    elapsed_time = end_time - start_time
    memory_usage_change = end_mem_usage - start_mem_usage

    # Display results
    print(f"Result of integration: {result:.7f}")
    print(f"Elapsed Time: {elapsed_time:.7f} seconds")
    print(f"Memory Usage Change: {memory_usage_change} kilobytes")

    return result, memory_usage_change, elapsed_time


# Example usage
if __name__ == "__main__":
    # Define the function to integrate, e.g., f(x) = x^2
    f = lambda x: x**2

    # Integrate f(x) = x^2 over the interval [0, 1] with 100 segments
    calculate_time_memory_trapezoidal(0.0, 1.0, 100, f)
