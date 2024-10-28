import argparse
import time
from mylib.lib import trapezoidal_rule


def append_to_md_file(file_name: str, result: float, duration: float) -> None:
    """
    Append the integration result and elapsed time to a markdown file.
    """
    with open(file_name, "a") as file:
        file.write("\n## Integration Result\n")
        file.write("- Function: x^2\n")
        file.write("- Interval: [0, 1]\n")
        file.write("- Number of segments: 100\n")
        file.write(f"- Result: {result:.5f}\n")
        file.write(f"- Time taken: {duration:.2f} microseconds\n\n")

    print(f"Content appended to {file_name} successfully!")


def main():
    # Define the function to integrate (e.g., f(x) = x^2)
    f = lambda x: x**2

    # Define the interval and number of segments
    a = 0.0
    b = 1.0
    n = 100

    # Start the timer
    start_time = time.perf_counter()

    # Calculate the integral
    result = trapezoidal_rule(a, b, n, f)

    # Stop the timer
    duration = (time.perf_counter() - start_time) * 1_000_000  # Convert to microseconds

    # Print the result
    print(f"The approximate integral of x^2 over [0, 1] is: {result}")
    print(f"Time taken: {duration:.2f} microseconds")

    # Append the result to a markdown file
    append_to_md_file("python_times.md", result, duration)


if __name__ == "__main__":
    main()
