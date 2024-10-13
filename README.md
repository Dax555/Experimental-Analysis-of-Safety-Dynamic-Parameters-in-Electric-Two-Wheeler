# **E2W Safety Analysis: Monitoring and Analysis of Dynamic Parameters for Electric Two-Wheelers (E2Ws)**

## **Project Overview**

This repository contains the dataset and code associated with the research paper titled **"Safety Analysis for Electric Two-Wheelers Using Dynamic Parameters"**. The project focuses on monitoring and analyzing critical safety-related parameters such as acceleration, velocity, inclination, roll, and pitch of electric two-wheelers (E2Ws) under varying weather conditions. The insights obtained from the analysis emphasize the need for robust control systems and advanced rider assistance to ensure safer rides, especially in adverse weather scenarios.

### **Abstract**
India ranks first globally in two-wheeler accidents, and the rapid adoption of electric two-wheelers (E2Ws) has raised critical safety concerns. This study develops a system to monitor and analyze key dynamic parameters—acceleration, velocity, inclination, roll, and pitch—under various weather conditions. The analysis reveals significant insights into E2W dynamics, highlighting the need for robust control mechanisms and advanced rider assistance systems. Key findings show greater variability in the steering mechanism compared to the center of gravity, especially in adverse weather conditions, underscoring the importance of traction control systems to mitigate risks from sudden dynamic changes.

## **Project Structure**

- **data**: This folder contains all the raw and processed data collected during the study. The data is recorded from the MPU6050 sensor and organized in Excel sheets, covering:
  - **Acceleration Data**: Real-time acceleration values recorded during various driving conditions.
  - **Angular Velocity Data**: Measurements of angular velocity.
  - **Inclination, Roll, and Pitch Data**: Inclination and rotation data collected to monitor vehicle stability.
  - **Weather Condition Logs**: Correlating weather conditions with dynamic parameter variations.
  
- **code**: The folder contains Python code for data analysis and visualization. This includes:
  - **Data Preprocessing**: Code for cleaning and normalizing the sensor data.
  - **Statistical Analysis**: Scripts for calculating statistical measures like mean, variance, and p-tests.
  - **Machine Learning Models**: Scripts implementing outlier detection models (such as Isolation Forest) to identify unsafe driving conditions.
  - **Visualization Tools**: Scripts for generating graphs and plots that depict relationships between the parameters.


