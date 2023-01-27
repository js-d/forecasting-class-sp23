import numpy as np

def q11_expected_win(q):
    assert(np.sum(q) == 1)
    if q[0] >= 0.9:
        return 0.8
    elif q[1] >= 0.3:
        return 0.2
    else:
        return 0

def submit_forecast_win(heads_prob):
    prob = q11_expected_win((heads_prob, 1-heads_prob))
    if np.random.rand() < prob:
        return "You win!"
    else:
        return "Better luck next time"

