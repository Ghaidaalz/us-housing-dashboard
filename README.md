# House Price Dashboard

## 🏠 Project Overview

This project is an interactive data visualization dashboard built using Streamlit to explore and analyze real estate housing prices in Australia. It offers users a clear understanding of the housing market through intuitive visuals, filtering tools, and structured storytelling.

## 🎯 Objectives

- Introduce the dataset and context behind Australian house pricing.
- Provide a user-friendly interface for exploring housing data.
- Enable dynamic visual exploration: trends, distributions, and maps.
- Support decision-making for buyers, sellers, and analysts with city-wise insights.

## 📊 Features

- Storytelling-based introduction to the real estate market.
- Interactive map showing average house prices by city.
- Filtering options by bedrooms, bathrooms, and more.
- Charts for distribution and trend analysis.
- Clean, minimal UI using Streamlit and Plotly.

## 🧰 Tech Stack

- Python
- Streamlit
- Pandas, NumPy
- Plotly / Altair / Matplotlib
- Scikit-learn (for preprocessing)
- GitHub (version control)

## 🗂️ Project Structure

├── data/
│ └── houses.csv
├── pages/
│ ├── 1_Introduction.py
│ ├── 2_Dashboard.py
├── utils/
│ └── preprocessing.py
├── app.py
├── requirements.txt
└── README.md


## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/house-price-dashboard.git
cd house-price-dashboard

    Install dependencies:

pip install -r requirements.txt

    Run the Streamlit app:

streamlit run app.py

📌 Dataset

The dataset contains information on real estate listings in Australia, including attributes such as:

    Bedrooms, Bathrooms, Sqft, Lot Size

    Year Built, Renovated, View, City, Zipcode

    Price (target variable)

📎 License

This project is licensed under the MIT License.


Let me know if you'd like this saved to a file or if you want a matching requirements.txt generated!

