# Project Auto Machine Learning

## Description

This Streamlit app provides a user-friendly interface for automated machine learning tasks. It allows users to upload their datasets, perform exploratory data analysis (EDA), train various machine learning models, and download the best-performing model.

## Key Features
### Navigation
![Bagian Navigation](https://github.com/user-attachments/assets/cdc3e4b8-6830-4c2f-bbd5-09e2ac7f4206)

- **Data Upload**: Supports uploading CSV and Excel files.
- **Data Profiling**: Generates a comprehensive profile report using `ydata_profiling` for data exploration and analysis.
- **Automated Model Selection**: Uses `pycaret` and `lazypredict` libraries to automatically train and compare different machine learning models.
- **Model Download**: Allows users to download the trained model in a `.pkl` file for future use.
- **User-Friendly Interface**: Streamlit provides a visually appealing and intuitive interface for interacting with the app.

## How to Use

1. **Upload Your Dataset**: Select the "Upload" option in the sidebar and upload your CSV or Excel file.

![Upload dataset](https://github.com/user-attachments/assets/409f65df-78c3-4853-a7b8-240ad3643114)

2. **Explore Your Data (Profiling)**: Navigate to the "Profiling" section to generate a detailed data profile report.

![profiling 1](https://github.com/user-attachments/assets/67e2ea1b-5c43-4dcf-b58b-6608daf23733)
![profiling 2](https://github.com/user-attachments/assets/0c359e7f-5a8f-43bd-84e1-3ddc43a9c850)
![profiling 3](https://github.com/user-attachments/assets/07fba88d-ca8e-4d13-bdcd-a21b796ae349)

3. **Train a Model (AutoML)**: Choose the "AutoML" option, select your target variable, and click "Train model". The app will automatically train and compare various models, displaying their performance metrics.

![ML 1](https://github.com/user-attachments/assets/0de41e91-a537-4634-a727-5a11f320ec28)
![ML 2](https://github.com/user-attachments/assets/65f8a943-9ec4-4272-a0df-2f905bc6de90)

4. **Download Your Model**: Go to the "Download" section to download the best performing model in a `.pkl` file.

![dw](https://github.com/user-attachments/assets/eca8d0d7-ca3c-4494-bb83-5f74b5a417e8)

## Objective

The objective of this project is to simplify the process of building and deploying machine learning models by providing a user-friendly tool for automated model selection and training.

## Insights

This app provides valuable insights into the user's data and helps them:

- **Understand data characteristics**: The profiling feature provides a detailed overview of the dataset, including data types, missing values, correlations, and distributions.
- **Identify the best model**: The automated model selection process helps users find the most suitable machine learning model for their specific task.
- **Deploy models easily**: The ability to download trained models allows users to easily deploy them in their applications.

## Note

This is a basic implementation of an AutoML app. You can further enhance it by adding features like:

- **Hyperparameter tuning**: Automatically tune hyperparameters for the selected model.
- **Model evaluation**: Provide more detailed evaluation metrics for each model.
- **Feature engineering**: Automatically perform feature engineering techniques to improve model performance.
- **Model deployment**: Integrate with cloud platforms for model deployment and serving.
