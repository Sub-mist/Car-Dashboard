
# Car Stock Dashboard

This Streamlit application provides an interactive dashboard to explore and analyze car stock data.

## Features

- **Interactive Filtering:** Sidebar filters allow users to filter data by car brand, transmission type, and fuel type.
- **Key Performance Indicators (KPIs):** Displays average price, car count, and earliest make year of cars based on filters.
- **Visualizations:** 
  - Bar chart showing price distribution based on car color.
  - Bar chart showing price distribution based on car brand.
  - Pie chart for transmission type distribution.
  - Histogram for manufacturing year distribution.
- **Custom Styling:** Custom footer and color scheme for a unique user interface.

## Installation

To run this application, you'll need Python installed on your system. Follow the steps below to set up and run the app.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sub-mist/car-stock-dashboard.git
   cd car-stock-dashboard
   ```

2. **Install the required packages:**

   It's recommended to use a virtual environment to manage dependencies. You can create one and install the packages using the following commands:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scrips\activate`
   pip install -r requirements.txt  # or you only need to run `pip install pandas numpy streamlit plotly`
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

## Usage

Once the app is running, open your web browser and go to `http://localhost:8501` to view the dashboard. Use the sidebar to filter data according to your preferences.

## Data Requirements

The application requires a CSV dataset named df_last.csv located in the ./Dataset/ directory. The CSV file should contain the following columns:

brand: Car brand names.
transmission_type: Type of transmission (e.g., Manual, Automatic).
fuel_type: Type of fuel (e.g., Petrol, Diesel, Hybrid, Electric).
price_in_euro: Price of the car in Euros.
year: Manufacturing year of the car.
color: Color of the car.
Ensure that the fuel_type column values are correctly formatted to avoid issues with capitalization.

## File Structure

```plaintext
.
├── Dataset
│   ├── gcar_data.csv
|   ├── cleaned_data.csv
|   └── cleaned_car_data.csv
├── .Streamlit
|    └── df_new.csv
├── app.py
├── helper.ipynb
├── requirements.txt
└── README.md
```

Although the 'gcar_data.csv' and 'cleaned_data.csv' is not used in the actual app but for the purpose of clear understanding how was the raw data and converted the raw data into cleaned data.
helper.ipynb can help you understand the cleaning process.

## Customization

- **Themes and Colors:** You can customize the primary color, background color, and font in the Streamlit config.toml file to match your preferred theme.
- **Additional Visualizations:** You can add more visualizations or KPIs by extending the app.py file with additional plotly.express charts or streamlit components.

---------------------------------------------------------

This project is created using Streamlit, an open-source app framework in Python, and Plotly Express for data visualization.