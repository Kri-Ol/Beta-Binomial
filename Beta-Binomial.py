import numpy as np

def sample_Beta_Binomial(a, b, n, size=None):
    """
    Use property of the compound distribution for B-B,
    see https://en.wikipedia.org/wiki/Beta-binomial_distribution
    """
    p = np.random.beta(a, b, size=size)
    r = np.random.binomial(n, p)

    return r

if __name__ == "__main__":
    # simple test case, repeat green graph in the Wiki page
    np.random.seed(777777)

    n = 10
    a = 2.
    b = 2.
    N = 100000

    q = sample_Beta_Binomial(a, b, n, size=N) # a lot of sampled numbers
    print(q)

    h = np.zeros(n + 1, dtype=np.float64) # histogram
    for v in q: # fill histogram
        h[v] += 1.0

    h /= np.float64(N) # normalization
    print(h)
