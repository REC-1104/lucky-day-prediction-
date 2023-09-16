<p align="center"><img src="https://media0.giphy.com/media/gIszyDPvwfPtyCfDyK/giphy.gif?cid=ecf05e47nml0djitz1xrzvsl4udjk496n8mdeplgfphan3o8&ep=v1_gifs_search&rid=giphy.gif&ct=g" height=200 width=200/></p>

# Zodiac Luck Meter

This project is a Lucky Day Prediction web application built using ReactJS. The app allows users to input their zodiac signs with other features and get predictions about their lucky days based on a multiple linear regression algorithm's results and findings. The prediction logic is implemented using a Jupyter notebook and its results and findings are used into the React app.

## Features

- User-friendly interface to input zodiac sign and other features and get lucky day predictions.
- Real-time feedback and validation for input fields.
- Jupyter notebook for prediction logic using multiple linear regression algorithms.
- Responsive design for seamless usage across different devices.

## Installation

1. Clone the repository.
2. Navigate to the project directory and run `npm install` to install the required dependencies.
3. Run `npm start` to start the development server.

## Role of Python 

The prediction logic is based on inferences obtained from python file. The file contains the necessary algorithms and data processing steps to predict lucky days based on birthdates. Below is a brief overview of the prediction process:

1. [Data Loading] - Loading the `luckyDay.csv` file.
2. [Data Preprocessing] - Process the data to ensure it meets the requirements of the prediction algorithm.
3. [Data Visualizing] - Plotting different graphs to derive some necessary observations and conclusion.
4. [Prediction Algorithm] - Utilize a multiple linear regression algorithm to determine lucky days based on the processed data.

The python file can be found in the `lib` directory.
