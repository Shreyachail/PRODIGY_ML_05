# Food Image Recognition & Calorie Estimation

A Machine Learning project developed as part of the **Prodigy InfoTech Machine Learning Internship — Task 05**.

This project uses a Convolutional Neural Network (CNN) to classify food images into five categories and estimate approximate calorie values using predefined reference data.

## Features

* Food image classification using a trained CNN model.
* Supports five food categories:

  * Pizza
  * Hamburger
  * Sushi
  * Ice Cream
  * French Fries
* Prediction confidence display.
* Approximate calorie estimation.
* Interactive web interface built with Streamlit.

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pillow
* Streamlit
* Google Colab
* Food-101 Dataset

## Model Details

* Model: Convolutional Neural Network (CNN)
* Input image size: 128 × 128 pixels
* Number of classes: 5
* Validation accuracy during training: approximately 45.70%

**Note:** Model predictions may be incorrect. Prediction confidence is not the same as model accuracy.

## Calorie Estimation

The application displays approximate reference values:

| Food         | Approximate Calories         |
| ------------ | ---------------------------- |
| Pizza        | 285 kcal per slice           |
| Hamburger    | 354 kcal per burger          |
| Sushi        | 200 kcal per typical serving |
| Ice Cream    | 207 kcal per 100 g           |
| French Fries | 312 kcal per 100 g           |

Actual calorie content depends on serving size, ingredients, and preparation method.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Shreyachail/PRODIGY_ML_05.git
cd PRODIGY_ML_05
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python -m streamlit run app.py
```

The application should open in your browser.

## Project Structure

```text
PRODIGY_ML_05/
├── app.py
├── food_recognition_model.keras
├── requirements.txt
└── README.md
```

## Limitations

* The model supports only five food categories.
* Classification performance is limited by the trained model.
* Calorie values are estimates, not nutritional measurements.
* The model may misclassify images.


