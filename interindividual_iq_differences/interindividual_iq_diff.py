import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import time
import logging
import argparse

def simulate_iq_difference(num_simulations, mean, std):
    """
    Simulates IQ scores for two individuals and calculates their absolute difference.
    
    Parameters:
        num_simulations (int): Number of pairs to simulate.
        mean (float): The mean IQ value.
        std (float): The standard deviation of the IQ scores.
        
    Returns:
        avg_difference (float): The average absolute IQ difference.
        differences (numpy.ndarray): Array of individual IQ differences.
    """
    # Generate two arrays of IQ scores from a normal distribution
    iq1 = np.random.normal(loc=mean, scale=std, size=num_simulations)
    iq2 = np.random.normal(loc=mean, scale=std, size=num_simulations)
    
    # Compute the absolute difference between each pair
    differences = np.abs(iq1 - iq2)
    avg_difference = np.mean(differences)
    return avg_difference, differences

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(
        description="Simulate average IQ difference between two random people."
    )
    parser.add_argument("--simulations", type=int, default=1000000, 
                        help="Number of simulation runs (default: 1,000,000)")
    args = parser.parse_args()
    
    # Configure logging to display simulation time
    logging.basicConfig(level=logging.INFO)
    
    start_time = time.time()
    avg_diff, differences = simulate_iq_difference(args.simulations, mean=100, std=15)
    elapsed_time = time.time() - start_time
    
    logging.info(f"Simulated {args.simulations} pairs in {elapsed_time:.3f} seconds")
    print(f"Average IQ difference between two random people: {avg_diff:.2f} IQ points")
    
    # Create a pandas DataFrame for further inspection or analysis
    df = pd.DataFrame({"IQ Difference": differences})
    
    # Plot a histogram of the IQ differences using matplotlib
    plt.figure(figsize=(10, 6))
    plt.hist(differences, bins=100, color='blue', alpha=0.7)
    plt.xlabel("IQ Difference")
    plt.ylabel("Frequency")
    plt.title("Histogram of IQ Differences from Simulation")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

