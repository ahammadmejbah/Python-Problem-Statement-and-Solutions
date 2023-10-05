import math

def cumulative_std_dev(data):
    cumulative_mean = 0  # Initialize the cumulative mean
    cumulative_variance = 0  # Initialize the cumulative variance
    cumulative_std_deviation = []  # List to store cumulative standard deviations

    for i, x in enumerate(data, 1):
        # Update the cumulative mean
        cumulative_mean = (cumulative_mean * (i - 1) + x) / i

        # Update the cumulative variance
        cumulative_variance = (cumulative_variance * (i - 1) + (x - cumulative_mean) ** 2) / i

        # Calculate the cumulative standard deviation
        cumulative_std_dev = math.sqrt(cumulative_variance)

        cumulative_std_deviation.append(cumulative_std_dev)

    return cumulative_std_deviation

# Example usage:
data = [1, 2, 3, 4, 5]
cumulative_std = cumulative_std_dev(data)
print(cumulative_std)
