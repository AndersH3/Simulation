import numpy as np


def simulate_avg_iq_diff(rho, mu=100, sigma=15, n_samples=1_000_000, seed=None):
    """
    Simulate two correlated IQ test scores and return the average absolute difference.

    Parameters
    ----------
    rho : float
        Correlation between test 1 and test 2.
    mu : float
        Mean IQ score (default 100).
    sigma : float
        Standard deviation of IQ scores (default 15).
    n_samples : int
        Number of Monte Carlo samples (default 1e6).
    seed : int or None
        Random seed for reproducibility (default None).

    Returns
    -------
    float
        The average absolute difference |IQ1 - IQ2|.
    """
    rng = np.random.default_rng(seed)

    # Generate independent standard normals
    z1 = rng.standard_normal(n_samples)
    z2 = rng.standard_normal(n_samples)

    # Construct two normals with correlation rho
    iq1 = mu + sigma * z1
    iq2 = mu + sigma * (rho * z1 + np.sqrt(1 - rho**2) * z2)

    # Compute absolute differences and return their mean
    diffs = np.abs(iq1 - iq2)
    return diffs.mean()


if __name__ == "__main__":
    rho = 0.6
    avg_diff = simulate_avg_iq_diff(rho, seed=42)
    print(f"Average absolute IQ difference (ρ={rho}): {avg_diff:.3f} points")
