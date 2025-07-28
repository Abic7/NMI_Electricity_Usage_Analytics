import pandas as pd
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

# --- 1. Load Data ---
# Load energy consumption data
try:
    energy_df = pd.read_csv('300Formatted.csv')
except FileNotFoundError:
    print("Error: '300Formatted.csv' not found. Please ensure the file is in the same directory as the script.")
    exit()

# Load temperature data
try:
    temp_df = pd.read_csv('melbourne_temperature.csv')
except FileNotFoundError:
    print("Error: 'melbourne_temperature.csv' not found. Please ensure the file is in the same directory as the script.")
    exit()

# --- 2. Preprocess Data ---
# Convert 'Date' columns to datetime objects for consistent merging
energy_df['Date'] = pd.to_datetime(energy_df['Date'])
temp_df['Date'] = pd.to_datetime(temp_df['Date'])

# Calculate the average daily temperature
temp_df['AvgTemp'] = temp_df[['MaxTemp', 'MinTemp']].mean(axis=1)

# Ensure the energy 'Value' column is numeric
energy_df['Value'] = pd.to_numeric(energy_df['Value'], errors='coerce')
# Drop any rows where the conversion resulted in NaN (Not a Number)
energy_df.dropna(subset=['Value'], inplace=True)

# Aggregate energy consumption by day (if there are multiple readings per day)
# If your data is already daily, this will just confirm it.
daily_energy_df = energy_df.groupby(energy_df['Date'].dt.date)['Value'].sum().reset_index()
daily_energy_df['Date'] = pd.to_datetime(daily_energy_df['Date'])


# --- 3. Merge Data ---
# Merge the two dataframes on the 'Date' column
merged_df = pd.merge(daily_energy_df, temp_df, on='Date', how='inner')


# --- 4. Correlation and Insights ---
# Calculate the correlation between daily energy consumption and average temperature
correlation = merged_df['Value'].corr(merged_df['AvgTemp'])

print("--- Key Insights ---")
print(f"✅ Correlation between daily energy consumption and average temperature: {correlation:.2f}")

# Find and display the day with the highest energy consumption
peak_usage_day = merged_df.loc[merged_df['Value'].idxmax()]
print(f"⚡ Peak energy usage of {peak_usage_day['Value']:.2f} kWh occurred on {peak_usage_day['Date'].date()} when the average temperature was {peak_usage_day['AvgTemp']:.2f}°C.")

# Find and display the hottest day and the consumption on that day
hottest_day = merged_df.loc[merged_df['AvgTemp'].idxmax()]
print(f"🔥 The hottest day had an average temperature of {hottest_day['AvgTemp']:.2f}°C on {hottest_day['Date'].date()}, with an energy consumption of {hottest_day['Value']:.2f} kWh.")


# --- 5. Create GIF Visualization ---
# Create a directory to store image frames for the GIF
frames_dir = 'frames'
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# Generate a plot for each day and save it as an image
for i in range(1, len(merged_df) + 1):
    plt.figure(figsize=(12, 7))
    plt.scatter(merged_df['AvgTemp'][:i], merged_df['Value'][:i], color='dodgerblue', alpha=0.7)
    
    # Add a title and labels with a bit more style
    plt.title(f'Daily Energy Consumption vs. Average Temperature\nDay: {merged_df["Date"][i-1].date()}', fontsize=16)
    plt.xlabel('Average Daily Temperature (°C)', fontsize=12)
    plt.ylabel('Daily Energy Consumption (kWh)', fontsize=12)
    
    # Set fixed plot limits for a stable animation
    plt.xlim(merged_df['AvgTemp'].min() - 2, merged_df['AvgTemp'].max() + 2)
    plt.ylim(merged_df['Value'].min() - 5, merged_df['Value'].max() + 10)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Save the frame
    plt.savefig(os.path.join(frames_dir, f'frame_{i:03d}.png'))
    plt.close()

# Compile the saved frames into a GIF
gif_path = 'energy_vs_temperature_analysis.gif'
with imageio.get_writer(gif_path, mode='I', fps=10) as writer:
    for i in range(1, len(merged_df) + 1):
        frame_filename = os.path.join(frames_dir, f'frame_{i:03d}.png')
        image = imageio.imread(frame_filename)
        writer.append_data(image)

print(f"\n📊 Successfully created '{gif_path}'!")
