import numpy as np
from percent_difference.iq_percent_simulation import simulate_iq_differences

def test_simulate_iq_differences_bounds():
    np.random.seed(0)
    avg_intra, avg_inter = simulate_iq_differences(n=1000)
    assert avg_intra > 0
    assert avg_inter > 0
    assert avg_intra < 100
    assert avg_inter < 100
