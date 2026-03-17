import numpy as np
# P(X <= t) = 0.975
# let Z = (X - mu) / sigma, then P(Z <= (t - mu) / sigma) = 0.975
# So P(Z <= (t - mu) / sigma) = 0.975 => (t - mu) / sigma = Z_0975
# Using MLE equivalent so we have t_MLE = mu_MLE + Z_0975 * sigma_MLE
# Since we have mu_MLE = X_bar and sigma_MLE = sqrt(1/n * sum((X_i - X_bar)^2))
# Substitute these values in the equation to get t_MLE = X_bar + Z_0975 * sigma_MLE

Z_0975 = 1.959963984540054
mu = 2
sigma = 0.5

def generate_data(n, mu, sigma):
    np.random.seed(0)
    x = np.random.normal(mu, sigma, n)
    X_MLE= np.mean(x)
    sigma_MLE = np.sqrt(np.sum((x - X_MLE) **2) / n )
    return X_MLE, sigma_MLE

def calculate_t_MLE(X_MLE, sigma_MLE):
    t_MLE = X_MLE + Z_0975 * sigma_MLE
    return t_MLE

def main():
    n = 1000
    X_MLE, sigma_MLE = generate_data(n, mu, sigma)
    t_MLE = calculate_t_MLE(X_MLE, sigma_MLE)
    print(f"Estimated t (MLE): {t_MLE}")

if __name__ == "__main__":
    main()