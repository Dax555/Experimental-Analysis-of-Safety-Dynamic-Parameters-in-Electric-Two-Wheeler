
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import scipy.stats as stats
from scipy.stats import norm
import statistics
import math
import seaborn as sns

df = pd.read_excel('final_steer.xlsx')
df.head()

rain = pd.read_excel('Steer.xlsx')
rain.head()

# Find the length of the shortest dataset
min_length = min(len(df['Acc X(m/s^2)']), len(rain['Acc X(m/s^2)']))

# Generate timestamps based on the shortest dataset
start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(min_length)]

# Slice the datasets to match the shortest length
df_steering_trimmed = df['Acc X(m/s^2)'][:min_length]
dfc_cog_trimmed = rain['Acc X(m/s^2)'][:min_length]

# Create scatter plot for both accelerations
plt.figure(figsize=(14, 8))  # Increase the figure size
plt.plot(timestamps, df_steering_trimmed, alpha=0.6, color='red', label='Sunny Weather Acceleration')
plt.plot(timestamps, dfc_cog_trimmed, alpha=0.6, color='black', label='Rainy Weather Acceleration')

# Set plot title and labels
plt.title('Acceleration vs Time', fontsize=20)  # Increase title font size
plt.xlabel('Timestamp', fontsize=15)  # Increase x-axis label font size
plt.ylabel('Acceleration_X (m/s^2)', fontsize=15)  # Increase y-axis label font size
plt.legend(fontsize=12)  # Increase legend font size

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

plt.show()

nor_accx_steer = np.array(df['Acc X(m/s^2)'])
nor_accx = np.array(rain['Acc X(m/s^2)'])

# Calculate mean and standard deviation for both datasets
mu_steer = np.mean(nor_accx_steer)
sigma_steer = np.std(nor_accx_steer)
mu_cog = np.mean(nor_accx)
sigma_cog = np.std(nor_accx)

# Generate data points for the Gaussian curves
x_steer = np.linspace(mu_steer - 3*sigma_steer, mu_steer + 3*sigma_steer, 1000)
y_steer = norm.pdf(x_steer, mu_steer, sigma_steer)

x_cog = np.linspace(mu_cog - 3*sigma_cog, mu_cog + 3*sigma_cog, 1000)
y_cog = norm.pdf(x_cog, mu_cog, sigma_cog)

# Plot the Gaussian distributions
plt.figure(figsize=(14, 8))  # Adjust figure size as needed
plt.plot(x_steer, y_steer, label=f'Rainy Weather Accelaration Gaussian Curve ($\mu={mu_steer:.2f}$, $\sigma={sigma_steer:.2f}$)', color='g')
plt.plot(x_cog, y_cog, label=f'Sunny Weather Accelaration Gaussian Curve ($\mu={mu_cog:.2f}$, $\sigma={sigma_cog:.2f}$)', color='r')

# Plot the histograms
plt.hist(nor_accx_steer, bins=30, density=True, alpha=0.6, color='g', label='Rainy Weather Acceleration')
plt.hist(nor_accx, bins=30, density=True, alpha=0.6, color='red', label='Sunny Weather Acceleration')

# Add vertical lines for mean and ±1σ, ±2σ for both datasets
plt.axvline(mu_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Acceleration Mean ($\mu={mu_steer:.2f}$)')
plt.axvline(mu_steer + sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Acceleration $\mu+\sigma={mu_steer+sigma_steer:.2f}$')
plt.axvline(mu_steer - sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Acceleration $\mu-\sigma={mu_steer-sigma_steer:.2f}$')
plt.axvline(mu_steer + 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Acceleration $\mu+2\sigma={mu_steer+2*sigma_steer:.2f}$')
plt.axvline(mu_steer - 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Acceleration $\mu-2\sigma={mu_steer-2*sigma_steer:.2f}$')

plt.axvline(mu_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Acceleration Mean ($\mu={mu_cog:.2f}$)')
plt.axvline(mu_cog + sigma_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Acceleration $\mu+\sigma={mu_cog+sigma_cog:.2f}$')
plt.axvline(mu_cog - sigma_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Acceleration $\mu-\sigma={mu_cog-sigma_cog:.2f}$')
plt.axvline(mu_cog + 2*sigma_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Acceleration $\mu+2\sigma={mu_cog+2*sigma_cog:.2f}$')
plt.axvline(mu_cog - 2*sigma_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Acceleration $\mu-2\sigma={mu_cog-2*sigma_cog:.2f}$')

# Add labels and title
plt.title('Gaussian Distributions and Histograms of Accelerations In Rainy and Sunny Weather')
plt.xlabel('Acceleration')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np

# Load sunny day data
sunny_data = pd.read_excel('final_steer.xlsx')

# Load rainy day data
rainy_data = pd.read_excel('Steer.')

# Determine the 95th percentile thresholds
sunny_acceleration_threshold = np.percentile(sunny_data['Acc X(m/s^2)'], 95)
sunny_steering_threshold = np.percentile(sunny_data['Rot X(rad/s)'], 95)

rainy_acceleration_threshold = np.percentile(rainy_data['Acc X(m/s^2)'], 95)
rainy_steering_threshold = np.percentile(rainy_data['Rot X(rad/s)'], 95)

print(f"Sunny Day Acceleration Threshold (95th percentile): {sunny_acceleration_threshold}")
print(f"Sunny Day Steering Angle Threshold (95th percentile): {sunny_steering_threshold}")

print(f"Rainy Day Acceleration Threshold (95th percentile): {rainy_acceleration_threshold}")
print(f"Rainy Day Steering Angle Threshold (95th percentile): {rainy_steering_threshold}")

# Example of combining these thresholds into a single safety norm number
# You can choose a simple weighted sum or another formula
def calculate_safety_norm(acceleration, steering_angle, accel_threshold, steer_threshold):
    # Normalized values
    normalized_accel = acceleration / accel_threshold
    normalized_steering = steering_angle / steer_threshold

    # Combined safety norm (simple weighted sum in this example)
    safety_norm = 0.5 * normalized_accel + 0.5 * normalized_steering

    return safety_norm

# Apply the function to the datasets
sunny_data['safety_norm'] = sunny_data.apply(
    lambda row: calculate_safety_norm(row['Acc X(m/s^2)'], row['Rot X(rad/s)'],
                                      sunny_acceleration_threshold, sunny_steering_threshold), axis=1)

rainy_data['safety_norm'] = rainy_data.apply(
    lambda row: calculate_safety_norm(row['Acc X(m/s^2)'], row['Rot X(rad/s)'],
                                      rainy_acceleration_threshold, rainy_steering_threshold), axis=1)

# Display some example rows with the calculated safety norm
print("Sunny Data with Safety Norm:")
print(sunny_data[['Acc X(m/s^2)', 'Rot X(rad/s)', 'safety_norm']].head())

print("\nRainy Data with Safety Norm:")
print(rainy_data[['Acc X(m/s^2)', 'Rot X(rad/s)', 'safety_norm']].head())

nor_accx_steer = np.array(df['Rot X(rad/s)'])
nor_accx = np.array(rain['Rot X(rad/s)'])

# Calculate mean and standard deviation for both datasets
mu_steer = np.mean(nor_accx_steer)
sigma_steer = np.std(nor_accx_steer)
mu_cog = np.mean(nor_accx)
sigma_cog = np.std(nor_accx)

# Generate data points for the Gaussian curves
x_steer = np.linspace(mu_steer - 3*sigma_steer, mu_steer + 3*sigma_steer, 1000)
y_steer = norm.pdf(x_steer, mu_steer, sigma_steer)

x_cog = np.linspace(mu_cog - 3*sigma_cog, mu_cog + 3*sigma_cog, 1000)
y_cog = norm.pdf(x_cog, mu_cog, sigma_cog)

# Plot the Gaussian distributions
plt.figure(figsize=(14, 8))  # Adjust figure size as needed
plt.plot(x_steer, y_steer, label=f'Rainy Weather Angular Velocity Gaussian Curve ($\mu={mu_steer:.2f}$, $\sigma={sigma_steer:.2f}$)', color='g')
plt.plot(x_cog, y_cog, label=f'Sunny Weather Angular Velocity Gaussian Curve ($\mu={mu_cog:.2f}$, $\sigma={sigma_cog:.2f}$)', color='r')

# Plot the histograms
plt.hist(nor_accx_steer, bins=30, density=True, alpha=0.6, color='g', label='Rainy Weather Angular Velocity')
plt.hist(nor_accx, bins=30, density=True, alpha=0.6, color='red', label='Sunny Weather Angular Velocity')

# Add vertical lines for mean and ±1σ, ±2σ for both datasets
plt.axvline(mu_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Angular Velocity Mean ($\mu={mu_steer:.2f}$)')
plt.axvline(mu_steer + sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Angular Velocity $\mu+\sigma={mu_steer+sigma_steer:.2f}$')
plt.axvline(mu_steer - sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Angular Velocity $\mu-\sigma={mu_steer-sigma_steer:.2f}$')
plt.axvline(mu_steer + 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Angular Velocity $\mu+2\sigma={mu_steer+2*sigma_steer:.2f}$')
plt.axvline(mu_steer - 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Rainy Weather Angular Velocity $\mu-2\sigma={mu_steer-2*sigma_steer:.2f}$')

plt.axvline(mu_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Angular Velocity Mean ($\mu={mu_cog:.2f}$)')
plt.axvline(mu_cog + sigma_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Angular Velocity $\mu+\sigma={mu_cog+sigma_cog:.2f}$')
plt.axvline(mu_cog - sigma_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Angular Velocity $\mu-\sigma={mu_cog-sigma_cog:.2f}$')
plt.axvline(mu_cog + 2*sigma_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Angular Velocity $\mu+2\sigma={mu_cog+2*sigma_cog:.2f}$')
plt.axvline(mu_cog - 2*sigma_cog, color='red', linestyle='--', linewidth=1, label=f'Sunny Weather Angular Velocity $\mu-2\sigma={mu_cog-2*sigma_cog:.2f}$')

# Add labels and title
plt.title('Gaussian Distributions and Histograms of Angular Velocity In Rainy and Sunny Weather')
plt.xlabel('Acceleration')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()









# Find the length of the shortest dataset
min_length = min(len(df['Rot X(rad/s)']), len(rain['Rot X(rad/s)']))

# Generate timestamps based on the shortest dataset
start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(min_length)]

# Slice the datasets to match the shortest length
df_steering_trimmed = df['Rot X(rad/s)'][:min_length]
dfc_cog_trimmed = rain['Rot X(rad/s)'][:min_length]

# Create scatter plot for both accelerations
plt.figure(figsize=(14, 8))  # Increase the figure size
plt.plot(timestamps, df_steering_trimmed, alpha=0.6, color='red', label='Sunny Weather Acceleration')
plt.plot(timestamps, dfc_cog_trimmed, alpha=0.6, color='black', label='Rainy Weather Acceleration')

# Set plot title and labels
plt.title('Angular velocity vs Time', fontsize=20)  # Increase title font size
plt.xlabel('Timestamp', fontsize=15)  # Increase x-axis label font size
plt.ylabel('Angular Velocity on X-axis (rad/s)', fontsize=15)  # Increase y-axis label font size
plt.legend(fontsize=12)  # Increase legend font size

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

plt.show()

