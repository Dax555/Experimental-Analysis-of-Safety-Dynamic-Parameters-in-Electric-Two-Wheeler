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
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore

df = pd.read_excel('Steer_drive3_daksh.xlsx')
dfc = pd.read_excel('COG_drive3_daksh.xlsx')

df

# Find the length of the shortest dataset
min_length = min(len(df['Acc X(m/s^2)']), len(dfc['Acc X(m/s^2)']))

# Generate timestamps based on the shortest dataset
start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(min_length)]

# Slice the datasets to match the shortest length
df_steering_trimmed = df['Acc X(m/s^2)'][:min_length]
dfc_cog_trimmed = dfc['Acc X(m/s^2)'][:min_length]

# Create scatter plot for both accelerations
plt.figure(figsize=(14, 8))  # Increase the figure size
plt.plot(timestamps, df_steering_trimmed, alpha=0.6, color='darkgreen', label='Rainy Weather Acceleration COG')
plt.plot(timestamps, dfc_cog_trimmed, alpha=0.6, color='b', label='Rainy Weather Acceleration Steering')

# Set plot title and labels
plt.title('Acceleration vs Time', fontsize=20)  # Increase title font size
plt.xlabel('Timestamp', fontsize=15)  # Increase x-axis label font size
plt.ylabel('Acceleration_X (m/s^2)', fontsize=15)  # Increase y-axis label font size
plt.legend(fontsize=12)  # Increase legend font size

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

plt.show()

nor_accx_steer = np.array(df['Acc X(m/s^2)'])
nor_accx = np.array(dfc['Acc X(m/s^2)'])


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
plt.plot(x_steer, y_steer, label=f'Steering Gaussian Curve ($\mu={mu_steer:.2f}$, $\sigma={sigma_steer:.2f}$)', color='g')
plt.plot(x_cog, y_cog, label=f'COG Gaussian Curve ($\mu={mu_cog:.2f}$, $\sigma={sigma_cog:.2f}$)', color='b')

# Plot the histograms
plt.hist(nor_accx_steer, bins=30, density=True, alpha=0.6, color='g', label='Steering Acceleration')
plt.hist(nor_accx, bins=30, density=True, alpha=0.6, color='b', label='COG Acceleration')

# Add vertical lines for mean and ±1σ, ±2σ for both datasets
plt.axvline(mu_steer, color='g', linestyle='--', linewidth=1, label=f'Steering Mean ($\mu={mu_steer:.2f}$)')
plt.axvline(mu_steer + sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu+\sigma={mu_steer+sigma_steer:.2f}$')
plt.axvline(mu_steer - sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu-\sigma={mu_steer-sigma_steer:.2f}$')
plt.axvline(mu_steer + 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu+2\sigma={mu_steer+2*sigma_steer:.2f}$')
plt.axvline(mu_steer - 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu-2\sigma={mu_steer-2*sigma_steer:.2f}$')

plt.axvline(mu_cog, color='b', linestyle='--', linewidth=1, label=f'COG Mean ($\mu={mu_cog:.2f}$)')
plt.axvline(mu_cog + sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu+\sigma={mu_cog+sigma_cog:.2f}$')
plt.axvline(mu_cog - sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu-\sigma={mu_cog-sigma_cog:.2f}$')
plt.axvline(mu_cog + 2*sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu+2\sigma={mu_cog+2*sigma_cog:.2f}$')
plt.axvline(mu_cog - 2*sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu-2\sigma={mu_cog-2*sigma_cog:.2f}$')

# Add labels and title
plt.title('Gaussian Distributions and Histograms of Accelerations')
plt.xlabel('Acceleration on X-axis')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.xlim(-6,6)

plt.tight_layout()
plt.show()

# Find the length of the shortest dataset
min_length = min(len(df['Acc Y(m/s^2)']), len(dfc['Acc Y(m/s^2)']))

# Generate timestamps based on the shortest dataset
start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(min_length)]

# Slice the datasets to match the shortest length
df_steering_trimmed = df['Acc X(m/s^2)'][:min_length]
dfc_cog_trimmed = dfc['Acc X(m/s^2)'][:min_length]

# Create scatter plot for both accelerations
plt.figure(figsize=(14, 8))  # Increase the figure size
plt.plot(timestamps, df_steering_trimmed, alpha=0.6, color='blue', label='Rainy Weather Acceleration COG')
plt.plot(timestamps, dfc_cog_trimmed, alpha=0.6, color='green', label='Rainy Weather Acceleration Steering')

# Set plot title and labels
plt.title('Acceleration vs Time', fontsize=20)  # Increase title font size
plt.xlabel('Timestamp', fontsize=15)  # Increase x-axis label font size
plt.ylabel('Acceleration_Y (m/s^2)', fontsize=15)  # Increase y-axis label font size
plt.legend(fontsize=12)  # Increase legend font size

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

plt.show()

nor_accx_steer = np.array(df['Acc Y(m/s^2)'])
nor_accx = np.array(dfc['Acc Y(m/s^2)'])


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
plt.plot(x_steer, y_steer, label=f'Steering Gaussian Curve ($\mu={mu_steer:.2f}$, $\sigma={sigma_steer:.2f}$)', color='g')
plt.plot(x_cog, y_cog, label=f'COG Gaussian Curve ($\mu={mu_cog:.2f}$, $\sigma={sigma_cog:.2f}$)', color='b')

# Plot the histograms
plt.hist(nor_accx_steer, bins=30, density=True, alpha=0.6, color='g', label='Steering Acceleration')
plt.hist(nor_accx, bins=30, density=True, alpha=0.6, color='b', label='COG Acceleration')

# Add vertical lines for mean and ±1σ, ±2σ for both datasets
plt.axvline(mu_steer, color='g', linestyle='--', linewidth=1, label=f'Steering Mean ($\mu={mu_steer:.2f}$)')
plt.axvline(mu_steer + sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu+\sigma={mu_steer+sigma_steer:.2f}$')
plt.axvline(mu_steer - sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu-\sigma={mu_steer-sigma_steer:.2f}$')
plt.axvline(mu_steer + 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu+2\sigma={mu_steer+2*sigma_steer:.2f}$')
plt.axvline(mu_steer - 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu-2\sigma={mu_steer-2*sigma_steer:.2f}$')

plt.axvline(mu_cog, color='b', linestyle='--', linewidth=1, label=f'COG Mean ($\mu={mu_cog:.2f}$)')
plt.axvline(mu_cog + sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu+\sigma={mu_cog+sigma_cog:.2f}$')
plt.axvline(mu_cog - sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu-\sigma={mu_cog-sigma_cog:.2f}$')
plt.axvline(mu_cog + 2*sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu+2\sigma={mu_cog+2*sigma_cog:.2f}$')
plt.axvline(mu_cog - 2*sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu-2\sigma={mu_cog-2*sigma_cog:.2f}$')

# Add labels and title
plt.title('Gaussian Distributions and Histograms of Accelerations')
plt.xlabel('Acceleration on Y-axis')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.xlim(-4,4)

plt.tight_layout()
plt.show()

# Find the length of the shortest dataset
min_length = min(len(df['Rot X(rad/s)']), len(dfc['Rot X(rad/s)']))

# Generate timestamps based on the shortest dataset
start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(min_length)]

# Slice the datasets to match the shortest length
df_steering_trimmed = df['Rot X(rad/s)'][:min_length]
dfc_cog_trimmed = dfc['Rot X(rad/s)'][:min_length]

# Create scatter plot for both accelerations
plt.figure(figsize=(14, 8))  # Increase the figure size
plt.scatter(timestamps, df_steering_trimmed, alpha=0.6, color='blue', label='Rainy Weather Angular Velocity COG')
plt.scatter(timestamps, dfc_cog_trimmed, alpha=0.6, color='green', label='Rainy Weather Angular Velocity Steering')

# Set plot title and labels
plt.title('Angular Velocity vs Time', fontsize=20)  # Increase title font size
plt.xlabel('Timestamp', fontsize=15)  # Increase x-axis label font size
plt.ylabel('Angular Velocity (rad/s)', fontsize=15)  # Increase y-axis label font size
plt.legend(fontsize=12)  # Increase legend font size

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

plt.show()

nor_accx_steer = np.array(df['Rot X(rad/s)'])
nor_accx = np.array(dfc['Rot X(rad/s)'])


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
plt.plot(x_steer, y_steer, label=f'Steering Gaussian Curve ($\mu={mu_steer:.2f}$, $\sigma={sigma_steer:.2f}$)', color='g')
plt.plot(x_cog, y_cog, label=f'COG Gaussian Curve ($\mu={mu_cog:.2f}$, $\sigma={sigma_cog:.2f}$)', color='b')

# Plot the histograms
plt.hist(nor_accx_steer, bins=30, density=True, alpha=0.6, color='g', label='Steering Acceleration')
plt.hist(nor_accx, bins=30, density=True, alpha=0.6, color='b', label='COG Acceleration')

# Add vertical lines for mean and ±1σ, ±2σ for both datasets
plt.axvline(mu_steer, color='g', linestyle='--', linewidth=1, label=f'Steering Mean ($\mu={mu_steer:.2f}$)')
plt.axvline(mu_steer + sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu+\sigma={mu_steer+sigma_steer:.2f}$')
plt.axvline(mu_steer - sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu-\sigma={mu_steer-sigma_steer:.2f}$')
plt.axvline(mu_steer + 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu+2\sigma={mu_steer+2*sigma_steer:.2f}$')
plt.axvline(mu_steer - 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu-2\sigma={mu_steer-2*sigma_steer:.2f}$')

plt.axvline(mu_cog, color='b', linestyle='--', linewidth=1, label=f'COG Mean ($\mu={mu_cog:.2f}$)')
plt.axvline(mu_cog + sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu+\sigma={mu_cog+sigma_cog:.2f}$')
plt.axvline(mu_cog - sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu-\sigma={mu_cog-sigma_cog:.2f}$')
plt.axvline(mu_cog + 2*sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu+2\sigma={mu_cog+2*sigma_cog:.2f}$')
plt.axvline(mu_cog - 2*sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu-2\sigma={mu_cog-2*sigma_cog:.2f}$')

# Add labels and title
plt.title('Gaussian Distributions and Histograms of Accelerations')
plt.xlabel('Angular Velocity on X-axis')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.xlim(-1,1)

plt.tight_layout()
plt.show()

# Find the length of the shortest dataset
min_length = min(len(df['Rot Y(rad/s)']), len(dfc['Rot Y(rad/s)']))

# Generate timestamps based on the shortest dataset
start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(min_length)]

# Slice the datasets to match the shortest length
df_steering_trimmed = df['Rot Y(rad/s)'][:min_length]
dfc_cog_trimmed = dfc['Rot Y(rad/s)'][:min_length]

# Create scatter plot for both accelerations
plt.figure(figsize=(14, 8))  # Increase the figure size
plt.scatter(timestamps, df_steering_trimmed, alpha=0.6, color='blue', label='Rainy Weather Angular Velocity COG')
plt.scatter(timestamps, dfc_cog_trimmed, alpha=0.6, color='green', label='Rainy Weather Angular Velocity Steering')

# Set plot title and labels
plt.title('Angular Velocity vs Time', fontsize=20)  # Increase title font size
plt.xlabel('Timestamp', fontsize=15)  # Increase x-axis label font size
plt.ylabel('Angular Velocity Y-axis (rad/s)', fontsize=15)  # Increase y-axis label font size
plt.legend(fontsize=12)  # Increase legend font size

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

plt.show()

nor_accx_steer = np.array(df['Rot Y(rad/s)'])
nor_accx = np.array(dfc['Rot Y(rad/s)'])


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
plt.plot(x_steer, y_steer, label=f'Steering Gaussian Curve ($\mu={mu_steer:.2f}$, $\sigma={sigma_steer:.2f}$)', color='g')
plt.plot(x_cog, y_cog, label=f'COG Gaussian Curve ($\mu={mu_cog:.2f}$, $\sigma={sigma_cog:.2f}$)', color='b')

# Plot the histograms
plt.hist(nor_accx_steer, bins=30, density=True, alpha=0.6, color='g', label='Steering Acceleration')
plt.hist(nor_accx, bins=30, density=True, alpha=0.6, color='b', label='COG Acceleration')

# Add vertical lines for mean and ±1σ, ±2σ for both datasets
plt.axvline(mu_steer, color='g', linestyle='--', linewidth=1, label=f'Steering Mean ($\mu={mu_steer:.2f}$)')
plt.axvline(mu_steer + sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu+\sigma={mu_steer+sigma_steer:.2f}$')
plt.axvline(mu_steer - sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu-\sigma={mu_steer-sigma_steer:.2f}$')
plt.axvline(mu_steer + 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu+2\sigma={mu_steer+2*sigma_steer:.2f}$')
plt.axvline(mu_steer - 2*sigma_steer, color='g', linestyle='--', linewidth=1, label=f'Steering $\mu-2\sigma={mu_steer-2*sigma_steer:.2f}$')

plt.axvline(mu_cog, color='b', linestyle='--', linewidth=1, label=f'COG Mean ($\mu={mu_cog:.2f}$)')
plt.axvline(mu_cog + sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu+\sigma={mu_cog+sigma_cog:.2f}$')
plt.axvline(mu_cog - sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu-\sigma={mu_cog-sigma_cog:.2f}$')
plt.axvline(mu_cog + 2*sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu+2\sigma={mu_cog+2*sigma_cog:.2f}$')
plt.axvline(mu_cog - 2*sigma_cog, color='b', linestyle='--', linewidth=1, label=f'COG $\mu-2\sigma={mu_cog-2*sigma_cog:.2f}$')

# Add labels and title
plt.title('Gaussian Distributions and Histograms of Accelerations')
plt.xlabel('Angular Velocity on Y-axis')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.xlim(-1,1)

plt.tight_layout()
plt.show()

df['acceleration_z'] = zscore(df['Acc X(m/s^2)'])
df['angular_velocity_z'] = zscore(df['Rot X(rad/s)'])
df['roll_z'] = zscore(df['Inclin X(deg)'])
df['pitch_z'] = zscore(df['Inclin Y(deg)'])

# Outliers are typically defined as |z| > 3
outliers = df[(abs(df['acceleration_z']) > 3) |
              (abs(df['angular_velocity_z']) > 3) |
              (abs(df['roll_z']) > 3) |
              (abs(df['pitch_z']) > 3)]

outliers

# Select relevant features
features = df[['Acc X(m/s^2)', 'Rot X(rad/s)', 'Inclin X(deg)', 'Inclin Y(deg)']]

# Train Isolation Forest
iso_forest = IsolationForest(contamination=0.1, random_state=42)
iso_forest.fit(features)

# Predict anomalies
df['anomaly'] = iso_forest.predict(features)

anomalies = df[df['anomaly'] == -1]
anomalies

# Safety margin can be set based on domain knowledge, e.g., 3 standard deviations
acceleration_safe_upper = np.mean(df['Acc X(m/s^2)']) + 3 * statistics.stdev(df['Acc X(m/s^2)'])
acceleration_safe_lower = np.mean(df['Acc X(m/s^2)']) - 3 * statistics.stdev(df['Acc X(m/s^2)'])

angular_velocity_safe_upper = np.mean(df['Rot X(rad/s)']) + 3 * statistics.stdev(df['Rot X(rad/s)'])
angular_velocity_safe_lower = np.mean(df['Rot X(rad/s)'])- 3 * statistics.stdev(df['Rot X(rad/s)'])

roll_safe_upper = np.mean(df['Inclin X(deg)'])+ 3 * statistics.stdev(df['Inclin X(deg)'])
roll_safe_lower = np.mean(df['Inclin X(deg)'])- 3 * statistics.stdev(df['Inclin X(deg)'])

pitch_safe_upper = np.mean(df['Inclin Y(deg)']) + 3 * statistics.stdev(df['Inclin Y(deg)'])
pitch_safe_lower = np.mean(df['Inclin Y(deg)']) - 3 * statistics.stdev(df['Inclin Y(deg)'])

safety_norms = {
    'acceleration': (acceleration_safe_lower, acceleration_safe_upper),
    'angular_velocity': (angular_velocity_safe_lower, angular_velocity_safe_upper),
    'roll': (roll_safe_lower, roll_safe_upper),
    'pitch': (pitch_safe_lower, pitch_safe_upper)
}

safety_norms
