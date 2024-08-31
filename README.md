 # Used Car Price Prediction Model

This repository contains a machine learning model designed to predict the prices of used cars in the Pakistani market. The model utilizes various features such as brand name, model name, fuel type, model year, and kilometers driven to estimate the selling price.

## Table of Contents

- [Project Overview](#project-overview)
- [Files in the Repository](#files-in-the-repository)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Project Overview

The **Used Car Price Prediction Model** is built to help users estimate the market value of a used car in Pakistan based on specific details. The model is trained using a Random Forest algorithm and provides reasonably accurate predictions.

## Files in the Repository

- `templates/index.html`: The HTML file for the web interface where users can input car details.
- `static/css/style.css`: The CSS file for styling the web interface.
- `application.py`: The main Flask application file to run the web server.
- `model_data.csv`: The dataset used to train the model.
- `RandomForestModel.zip`: Contains the trained model file (`.pkl`). Users must extract the `.pkl` file from this zip and place it in the main directory (not in any subfolder).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Muzamil5hassan/Used-Car-Price-Prediction-Model.git
   cd used-car-price-prediction-model

 

## Usage

1. **Start the Web Application**:
   - Open your terminal and navigate to the directory where the project is located.
   - Ensure that your virtual environment is activated.
   - Run the Flask application by executing the following command:
     ```bash
     python application.py
     ```

2. **Access the Web Interface**:
   - Once the server is running, open your web browser and navigate to `http://127.0.0.1:5000/`.
   - You should see a form where you can input the car details.

3. **Input Car Details**:
   - Fill in the required fields:
     - **Brand Name**: The brand of the car (e.g., Toyota, Honda).
     - **Model Name**: The specific model of the car (e.g., Corolla, Civic).
     - **Fuel Type**: The type of fuel used (e.g., Petrol, Diesel).
     - **Model Year**: The year the car was manufactured.
     - **KM Driven**: The total kilometers the car has been driven.

4. **Get the Price Prediction**:
   - After entering all the details, click on the "Predict Price" button.
   - The application will display the estimated selling price of the car based on the input data.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software under the terms of the MIT License. See the [LICENSE](LICENSE) file for more details.

---

MIT License



