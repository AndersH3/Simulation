import numpy as np


def simulate_iq_differences(
    n: int = 10_000_000,
    mean: float = 100.0,
    stddev: float = 15.0,
    rho: float = 0.6
) -> tuple[float, float]:
    """
    Simulate IQ score pairs with correlation and compute average percent differences.

    Returns:
        avg_intra (float): Average intraindividual percent difference between paired scores.
        avg_inter (float): Average interindividual percent difference between random pairs of individuals.

    Percent difference for a pair (a, b) is:
        100 * abs(a - b) / ((a + b) / 2)
    """
    # Generate correlated IQ scores
    z1 = np.random.standard_normal(n)
    z2 = np.random.standard_normal(n)

    x = mean + stddev * z1
    y = mean + stddev * (rho * z1 + np.sqrt(1 - rho**2) * z2)

    # Intraindividual percent differences
    perc_intra = 100 * np.abs(x - y) / ((x + y) / 2)
    avg_intra = perc_intra.mean()

    # Interindividual percent differences (random pairs on test 1)
    idx2 = np.random.randint(0, n, size=n)
    x2 = x[idx2]
    perc_inter = 100 * np.abs(x - x2) / ((x + x2) / 2)
    avg_inter = perc_inter.mean()

    return avg_intra, avg_inter


if __name__ == "__main__":
    avg_intra, avg_inter = simulate_iq_differences()
    print(f"Average intraindividual percent difference: {avg_intra:.4f}%")
    print(f"Average interindividual percent difference: {avg_inter:.4f}%")
