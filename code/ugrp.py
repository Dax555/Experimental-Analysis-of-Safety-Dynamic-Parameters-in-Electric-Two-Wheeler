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

"""#DAY 4 DATA STEERING"""

df = pd.read_excel('final_steer.xlsx')
df.head()

filtered_final = df[df['Vel Y(m/s)'] >= -20.14]
final = filtered_final[filtered_final['Vel Y(m/s)']<=21.16]

# print(final)

final['Vel Y(m/s)'].sort_values()

final.to_excel('final_steer.xlsx')
final = final.iloc[:-1]
df = final
df

dfc = pd.read_excel('cog_drive.xlsx')
dfc.head()

"""#ANALYZING DATA OF ACC_X"""

start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(len(df['Acc X(m/s^2)']))]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(timestamps, df['Acc X(m/s^2)'], alpha=0.6, color='g')

# Set plot title and labels
plt.title('Acceleration vs Time')
plt.xlabel('Timestamp')
plt.ylabel('Acceleration_X (m/s^2)')

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

nor_accx_steer = np.array(df['Acc X(m/s^2)'])
nor_accx_steer

nor_accx = np.array(dfc['Acc X(m/s^2)'])
nor_accx

mu = np.mean(nor_accx_steer)
sigma = np.std(nor_accx_steer)
print(mu)
print(sigma)

# Calculate mean and standard deviation
mu = np.mean(nor_accx)
sigma = np.std(nor_accx)

# Generate data points for the Gaussian curve
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the Gaussian distribution
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.plot(x, y, label=f'Gaussian Curve ($\mu={mu:.2f}$, $\sigma={sigma:.2f}$)')
plt.title('Gaussian Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()

# Add vertical lines for mean and ±1σ, ±2σ
plt.axvline(mu, color='r', linestyle='--', linewidth=1, label=f'Mean ($\mu={mu:.2f}$)')
plt.axvline(mu + sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu+\sigma={mu+sigma:.2f}$')
plt.axvline(mu - sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu-\sigma={mu-sigma:.2f}$')
plt.axvline(mu + 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu+2\sigma={mu+2*sigma:.2f}$')
plt.axvline(mu - 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu-2\sigma={mu-2*sigma:.2f}$')

plt.legend()
plt.tight_layout()
plt.show()

# Plot the histogram
plt.hist(nor_accx, bins=10, density=True, alpha=0.6, color='g')

# Plot the normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, 0, 1)
plt.plot(x, p, 'k', linewidth=2)

title = "Normalized 'Acc X(m/s^2)' - Z-Scores"
plt.title(title)
plt.xlabel('Z-Score')
plt.ylabel('Density')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Calculate mean and standard deviation
mean_accx = np.mean(nor_accx)
std_accx = np.std(nor_accx)
mean_accx_steer = np.mean(nor_accx_steer)
std_accx_steer = np.std(nor_accx_steer)

# Plot the histograms
plt.hist(nor_accx, bins=10, density=True, alpha=0.6, color='r', label='Acc X')
plt.hist(nor_accx_steer, bins=10, density=True, alpha=0.6, color='azure', label='Acc X Steer')

# Plot the normal distribution curves
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p1 = stats.norm.pdf(x, mean_accx, std_accx)
p2 = stats.norm.pdf(x, mean_accx_steer, std_accx_steer)
plt.plot(x, p1, 'r', linewidth=2, label='Acc X Normal Curve')
plt.plot(x, p2, 'black', linewidth=2, label='Acc X Steer Normal Curve')

# Add mean and standard deviation lines
plt.axvline(mean_accx, color='r', linestyle='dashed', linewidth=1)
plt.axvline(mean_accx_steer, color='black', linestyle='dashed', linewidth=1)
plt.axvline(mean_accx + std_accx, color='r', linestyle='dotted', linewidth=1)
plt.axvline(mean_accx - std_accx, color='r', linestyle='dotted', linewidth=1)
plt.axvline(mean_accx_steer + std_accx_steer, color='black', linestyle='dotted', linewidth=1)
plt.axvline(mean_accx_steer - std_accx_steer, color='black', linestyle='dotted', linewidth=1)

# Add text annotations for mean and standard deviation
# plt.text(mean_accx, max(p1)/2, f'Mean: {mean_accx:.2f}\nStd: {std_accx:.2f}', color='g')
# plt.text(mean_accx_steer, max(p2)/2, f'Mean: {mean_accx_steer:.2f}\nStd: {std_accx_steer:.2f}', color='r')

# Add labels and title
title = "Normalized 'Acc X(m/s^2)' - Z-Scores"
plt.title(title)
plt.xlabel('Z-Score')
plt.ylabel('Density')
plt.legend()

# Zoom in on the graph
plt.xlim(-4, 4)

# Show the plot
plt.show()

print(mean_accx)
print(mean_accx_steer)

"""#ANALYZING DATA OF ACC_Y"""

start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(len(df['Acc Y(m/s^2)']))]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(timestamps, df['Acc Y(m/s^2)'], alpha=0.6, color='g')

# Set plot title and labels
plt.title('Acceleration vs Time')
plt.xlabel('Timestamp')
plt.ylabel('Acceleration_Y (m/s^2)')

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

nor_accy = np.array(df['Acc Y(m/s^2)'])
nor_accy

mu = np.mean(nor_accy)
sigma = np.std(nor_accy)
print(mu)
print(sigma)

# Calculate mean and standard deviation
mu = np.mean(nor_accy)
sigma = np.std(nor_accy)

# Generate data points for the Gaussian curve
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the Gaussian distribution
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.plot(x, y, label=f'Gaussian Curve ($\mu={mu:.2f}$, $\sigma={sigma:.2f}$)')
plt.title('Gaussian Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()

# Add vertical lines for mean and ±1σ, ±2σ
plt.axvline(mu, color='r', linestyle='--', linewidth=1, label=f'Mean ($\mu={mu:.2f}$)')
plt.axvline(mu + sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu+\sigma={mu+sigma:.2f}$')
plt.axvline(mu - sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu-\sigma={mu-sigma:.2f}$')
plt.axvline(mu + 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu+2\sigma={mu+2*sigma:.2f}$')
plt.axvline(mu - 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu-2\sigma={mu-2*sigma:.2f}$')

plt.legend()
plt.tight_layout()
plt.show()

"""#ANALYZING DATA OF VELOCITY X"""

start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(len(df['Vel X(m/s)']))]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.plot(timestamps, df['Vel X(m/s)'], alpha=0.6, color='g')

# Set plot title and labels
plt.title('Velocity vs Time')
plt.xlabel('Timestamp')
plt.ylabel('Velocity_X (m/s)')

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

nor_velx = np.array(df['Vel X(m/s)'])
nor_velx

mu = np.mean(nor_velx)
sigma = np.std(nor_velx)
print(mu)
print(sigma)

# Calculate mean and standard deviation
mu = np.mean(nor_velx)
sigma = np.std(nor_velx)

# Generate data points for the Gaussian curve
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the Gaussian distribution
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.plot(x, y, label=f'Gaussian Curve ($\mu={mu:.2f}$, $\sigma={sigma:.2f}$)')
plt.title('Gaussian Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()

# Add vertical lines for mean and ±1σ, ±2σ
plt.axvline(mu, color='r', linestyle='--', linewidth=1, label=f'Mean ($\mu={mu:.2f}$)')
plt.axvline(mu + sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu+\sigma={mu+sigma:.2f}$')
plt.axvline(mu - sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu-\sigma={mu-sigma:.2f}$')
plt.axvline(mu + 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu+2\sigma={mu+2*sigma:.2f}$')
plt.axvline(mu - 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu-2\sigma={mu-2*sigma:.2f}$')

plt.legend()
plt.tight_layout()
plt.show()

"""#ANALYZING DATA VELOCITY Y"""

start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(len(df['Vel Y(m/s)']))]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.plot(timestamps, df['Vel Y(m/s)'], alpha=0.6, color='b')

# Set plot title and labels
plt.title('Velocity vs Time')
plt.xlabel('Timestamp')
plt.ylabel('Velocity_Y (m/s)')

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

nor_vely = np.array(df['Vel Y(m/s)'])
nor_vely

mu = np.mean(nor_vely)
sigma = np.std(nor_vely)
print(mu)
print(sigma)

# Calculate mean and standard deviation
mu = np.mean(nor_vely)
sigma = np.std(nor_vely)

# Generate data points for the Gaussian curve
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the Gaussian distribution
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.plot(x, y, label=f'Gaussian Curve ($\mu={mu:.2f}$, $\sigma={sigma:.2f}$)')
plt.title('Gaussian Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()

# Add vertical lines for mean and ±1σ, ±2σ
plt.axvline(mu, color='r', linestyle='--', linewidth=1, label=f'Mean ($\mu={mu:.2f}$)')
plt.axvline(mu + sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu+\sigma={mu+sigma:.2f}$')
plt.axvline(mu - sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu-\sigma={mu-sigma:.2f}$')
plt.axvline(mu + 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu+2\sigma={mu+2*sigma:.2f}$')
plt.axvline(mu - 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu-2\sigma={mu-2*sigma:.2f}$')

plt.legend()
plt.tight_layout()
plt.show()

"""#ANALYZING DATA GYRO X"""

start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(len(df['Rot X(rad/s)']))]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.plot(timestamps, df['Rot X(rad/s)'], alpha=0.6, color='b')

# Set plot title and labels
plt.title('Angular Velocity vs Time')
plt.xlabel('Timestamp')
plt.ylabel('Angular Velocity X(rad/s)')

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

nor_rotx = np.array(df['Rot X(rad/s)'])
nor_rotx

mu = np.mean(nor_rotx)
sigma = np.std(nor_rotx)
print(mu)
print(sigma)

# Calculate mean and standard deviation
mu = np.mean(nor_rotx)
sigma = np.std(nor_rotx)

# Generate data points for the Gaussian curve
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the Gaussian distribution
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.plot(x, y, label=f'Gaussian Curve ($\mu={mu:.2f}$, $\sigma={sigma:.2f}$)')
plt.title('Gaussian Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()

# Add vertical lines for mean and ±1σ, ±2σ
plt.axvline(mu, color='r', linestyle='--', linewidth=1, label=f'Mean ($\mu={mu:.2f}$)')
plt.axvline(mu + sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu+\sigma={mu+sigma:.2f}$')
plt.axvline(mu - sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu-\sigma={mu-sigma:.2f}$')
plt.axvline(mu + 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu+2\sigma={mu+2*sigma:.2f}$')
plt.axvline(mu - 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu-2\sigma={mu-2*sigma:.2f}$')

plt.legend()
plt.tight_layout()
plt.show()

"""#ANALYZING DATA GYRO Y"""

start_time = pd.Timestamp('2023-07-01 00:00:00')
time_interval = pd.Timedelta(seconds=0.5)
timestamps = [start_time + i * time_interval for i in range(len(df['Rot X(rad/s)']))]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(timestamps, df['Rot X(rad/s)'], alpha=0.6, color='g')

# Set plot title and labels
plt.title('Rotation vs Time')
plt.xlabel('Timestamp')
plt.ylabel('Rotation X(rad/s)')

# Improve the readability of the x-axis by formatting the timestamps
plt.gcf().autofmt_xdate()

nor_roty = np.array(df['Rot X(rad/s)'])
nor_roty

mu = np.mean(nor_roty)
sigma = np.std(nor_roty)
print(mu)
print(sigma)

# Calculate mean and standard deviation
mu = np.mean(nor_roty)
sigma = np.std(nor_roty)

# Generate data points for the Gaussian curve
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the Gaussian distribution
plt.figure(figsize=(8, 6))  # Adjust figure size as needed
plt.plot(x, y, label=f'Gaussian Curve ($\mu={mu:.2f}$, $\sigma={sigma:.2f}$)')
plt.title('Gaussian Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()

# Add vertical lines for mean and ±1σ, ±2σ
plt.axvline(mu, color='r', linestyle='--', linewidth=1, label=f'Mean ($\mu={mu:.2f}$)')
plt.axvline(mu + sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu+\sigma={mu+sigma:.2f}$')
plt.axvline(mu - sigma, color='g', linestyle='--', linewidth=1, label=f'$\mu-\sigma={mu-sigma:.2f}$')
plt.axvline(mu + 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu+2\sigma={mu+2*sigma:.2f}$')
plt.axvline(mu - 2*sigma, color='b', linestyle='--', linewidth=1, label=f'$\mu-2\sigma={mu-2*sigma:.2f}$')

plt.legend()
plt.tight_layout()
plt.show()
