# retail_streamlit
Machine Learning project to predict retail sales using regression algorithms.

# 🛒 Retail Sales Prediction Using Machine Learning

## 📌 Project Overview

Retail Sales Prediction is a Machine Learning regression project that predicts retail sales amounts based on historical transaction data.

The project uses different regression algorithms to identify patterns in retail transactions and estimate future sales amounts based on product, customer, pricing, discount, and transaction-related information.

The trained Machine Learning pipeline is deployed using Streamlit to provide an interactive web application for users.

## 🎯 Project Objectives

- Analyze historical retail transaction data.
- Perform data preprocessing and cleaning.
- Handle missing values, duplicates, and outliers.
- Convert categorical variables into numerical values.
- Apply feature scaling where required.
- Train and evaluate multiple regression algorithms.
- Select the best-performing model.
- Predict retail sales amounts using a web application.

## 📂 Project Structure

```text
Retail_Sales_Prediction/
│
├── dataset/
│   └── retail_sales_dataset.csv
│
├── models/
│
├── notebooks/
│   └── train.ipynb
│
├── templates/
│
├── retail_sales_pipeline.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

## 📊 Dataset Description

The dataset contains retail transaction information.

Important features include:

| Feature | Description |
|---|---|
| quantity | Number of products purchased |
| unit_price | Price per product |
| discount_pct | Discount percentage |
| category | Product category |
| brand | Product brand |
| customer_segment | Customer classification |
| payment_method | Payment method |
| sales_channel | Online or offline |
| region | Sales region |
| month | Transaction month |
| year | Transaction year |
| day | Transaction day |
| day_of_week | Day of the week |

**Target Variable:** `sales_amount`

## ⚙️ Data Preprocessing

The following preprocessing techniques are considered:

1. Handling Missing Values
2. Removing Duplicate Records
3. Handling Outliers
4. Encoding Categorical Variables
5. Feature Scaling (where required)
6. Feature Selection (where applicable)
7. Train-Test Split

Scikit-learn preprocessing techniques are used to prepare the data for Machine Learning.

## 🤖 Machine Learning Algorithms

The following regression algorithms are implemented:

1. Linear Regression
2. Lasso Regression
3. Ridge Regression
4. Decision Tree Regressor
5. K-Nearest Neighbors Regressor
6. Support Vector Regression (SVR)

## 📈 Model Evaluation

The regression models are evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The best-performing model is selected based on evaluation results.

## 🚀 Deployment

The trained Machine Learning pipeline is saved using Joblib.

The application is deployed locally using Streamlit.

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd Retail_Sales_Prediction
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

### Step 5: Open the Application

Open the following URL in your browser:

```text
http://localhost:8501
```

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

## 💡 Application Features

- User-friendly interface.
- Interactive input fields.
- Prediction using a trained ML pipeline.
- Displays predicted retail sales amount.
- Real-time prediction through Streamlit.

## 🔮 Future Enhancements

- Deploy the application online.
- Add interactive sales visualizations.
- Include historical sales analysis.
- Improve model performance with additional features.

## 👨‍💻 Author

**Machine Learning Project**

Retail Sales Prediction using Regression Algorithms.
