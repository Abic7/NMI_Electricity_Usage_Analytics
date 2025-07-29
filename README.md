Australian Household Energy Consumption Analysis ⚡️💡

Welcome! This repository provides a set of Python scripts to enrich, analyze, and visualize household electricity usage data from Australian energy distributors. By correlating your energy consumption with local weather data, you can uncover actionable insights into your usage patterns, identify opportunities for savings, and understand your environmental impact.

The primary goal is to transform raw, complex NMI (National Metering Identifier) data into a clear, data-driven narrative.

📊 Features

    Data Enrichment: Automatically processes raw usage data from energy providers (like United Energy) and formats it according to NMI12 or NMI13 specifications.

    Usage Extraction: Precisely extracts your interval electricity consumption data from the enriched files.

    Weather Correlation: Merges your energy data with historical weather data from the Bureau of Meteorology (BOM).

    Insightful Analytics: Calculates key metrics, such as the correlation between temperature and energy use, peak consumption days, and more.

    Engaging Visualization: Generates a shareable animated GIF ( .gif ) that plots your daily energy consumption against the average temperature, bringing your data to life.

🚀 Getting Started

Follow these steps to get the project up and running on your local machine.
Prerequisites

    Python: Version 3.5 or higher.

    Usage Data: Your interval usage data file (usually a .csv). You can download this from your Australian electricity distributor's web portal.

        Example Source: United Energy - myEnergy Portal

    Weather Data: Historical daily weather data for your local area.

        Official Source: Australian Bureau of Meteorology (BOM) - Climate Data Online

⚙️ Installation

    Clone the repository:

    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name

    Install required Python libraries:

    pip install pandas matplotlib imageio

🛠️ How to Use
Step 1: Add Your Data Files 📁

Place your downloaded electricity usage and weather data files into the root directory of the project. For the scripts to work seamlessly, rename them to:

    Energy Data: 300Formatted.csv

    Weather Data: melbourne_temperature.csv

    Note: Ensure your CSV files have the correct column headers as specified in the scripts.

Step 2: Enrich Your Usage Data (Optional) 🧹

If you have a raw data file downloaded directly from your provider, first run nmi_Final.py to process it. This script reads the raw data, applies the correct NMI standard headers, and extracts the essential usage information into a clean file.

python nmi_Final.py

Step 3: Run the Analysis 📈

Once your data is cleaned and ready, run the main analysis script. This will perform the correlation, print key insights to your terminal, and generate the animated GIF.

python energy_analysis.py

After the script finishes, you will find a new file named energy_vs_temperature_analysis.gif in the project directory.
📜 Code Overview

This repository contains two main Python scripts:
nmi.py

    Purpose: To handle the initial data cleaning and preparation.

    Functionality:

        Reads raw usage data downloaded from an Australian electricity distributor.

        Enriches data headers to conform to NMI12 or NMI13 specifications.

        Extracts the relevant interval usage data and saves it to a formatted CSV file (300Formatted.csv).

energy_analysis.py

    Purpose: To perform the core analysis and create the visualization.

    Functionality:

        Loads the cleaned energy data and the local weather data.

        Calculates the correlation between electricity consumption and temperature.

        Identifies and prints high-level analytics (e.g., peak usage days).

        Generates an animated .gif plotting energy usage against temperature over time.

✨ Example Output
Analytics Insights

Running the energy_analysis.py script will produce an output similar to this in your terminal:

--- Key Insights ---
✅ Correlation between daily energy consumption and average temperature: 0.68
⚡ Peak energy usage of 25.40 kWh occurred on 2025-01-28 when the average temperature was 31.5°C.
🔥 The hottest day had an average temperature of 33.2°C on 2025-02-15, with an energy consumption of 24.90 kWh.

📊 Successfully created 'energy_vs_temperature_analysis.gif'!.

Animated Visualization

The script will generate a GIF that looks like this !
<img width="954" height="562" alt="image" src="https://github.com/user-attachments/assets/c98ee029-c2ab-4824-930c-8df8b8d2147b" />


🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

    Fork the Project

    Create your Feature Branch (git checkout -b feature/AmazingFeature)

    Commit your Changes (git commit -m 'Add some AmazingFeature')

    Push to the Branch (git push origin feature/AmazingFeature)

    Open a Pull Request

📄 License

This project is distributed under the MIT License. See LICENSE for more information.
