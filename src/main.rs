// main.rs is the entry point of Rust program.
// Define and handle CLI arguments using clap crate

use integration::trapezoidal_rule;
use std::fs::OpenOptions;
use std::io::{Result, Write};
use std::time::Instant; // Importing the time module
use sys_info; // for tracking memory usage

fn append_to_md_file(file_name: &str, result: f64, duration: &u128, mem_used: &u64) -> Result<()> {
    // Open the file in append mode, creating it if it doesn't exist
    let file = OpenOptions::new()
        .write(true)
        .create(true)
        .append(true)
        .open(file_name)?;

    let mut file = std::io::BufWriter::new(file);
    // Write integration and resource usage details to the file
    writeln!(file, "\n## Integration Result")?;
    writeln!(file, "- Function: x^2")?;
    writeln!(file, "- Interval: [0, 1]")?;
    writeln!(file, "- Number of segments: 100")?;
    writeln!(file, "- Result: {:.5}", result)?;
    writeln!(file, "- Time taken: {} microseconds", duration)?;
    writeln!(file, "- Memory used: {} KB\n", mem_used)?;

    println!("Content appended to {} successfully!", file_name);

    Ok(())
}

fn main() {
    // Define the function to integrate (e.g., f(x) = x^2)
    let f = |x: f64| x * x;

    // Define the interval and number of segments
    let a = 0.0;
    let b = 1.0;
    let n = 100;

    // Start the timer and get initial memory usage
    let start_time = Instant::now();
    let mem_info_before = sys_info::mem_info().unwrap();

    // Calculate the integral
    let result = trapezoidal_rule(a, b, n, f);

    // Stop the timer and get final memory usage
    let duration = start_time.elapsed();
    let mem_info_after = sys_info::mem_info().unwrap();

    // Calculate the time taken in microseconds and memory used in kilobytes
    let elapsed_time = duration.as_micros();
    let mem_used = mem_info_after.total - mem_info_before.total;

    // Print the result
    println!(
        "The approximate integral of x^2 over [0, 1] is: {:.5}",
        result
    );
    println!("Time taken: {} microseconds", elapsed_time);
    println!("Memory used: {} KB", mem_used);

    // Append the result to a markdown file
    match append_to_md_file(
        "rust_integration_times.md",
        result,
        &elapsed_time,
        &mem_used,
    ) {
        Ok(_) => println!("Results successfully written to rust_integration_times.md"),
        Err(e) => eprintln!("Failed to write results: {:?}", e),
    }
}
