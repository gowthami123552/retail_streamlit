
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# --------------------------------
# 1. Project Path
# --------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "retail_sales_pipeline.pkl"


# --------------------------------
# 2. Load Trained Model
# --------------------------------

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model file not found. Please run train.py first."
        )

    return joblib.load(MODEL_PATH)


model = load_model()


# --------------------------------
# 3. Streamlit Page Configuration
# --------------------------------

st.set_page_config(
    page_title="Retail Sales Prediction",
    page_icon="🛒",
    layout="wide"
)


# --------------------------------
# 4. Application Title
# --------------------------------

st.title("🛒 Retail Sales Prediction")

st.write(
    "Predict retail sales amounts using a trained Machine Learning model."
)

st.divider()


# --------------------------------
# 5. User Input Section
# --------------------------------

st.subheader("Enter Retail Transaction Details")

col1, col2 = st.columns(2)

with col1:

    quantity = st.number_input(
        "Quantity",
        min_value=1.0,
        value=1.0
    )

    unit_price = st.number_input(
        "Unit Price",
        min_value=0.01,
        value=100.0
    )

    discount_pct = st.number_input(
        "Discount Percentage",
        min_value=0.0,
        value=0.0
    )

    category = st.selectbox(
        "Product Category",
        ["Electronics", "Clothes", "Home-Kitchen"]
    )

    brand = st.text_input(
        "Brand",
        value="Unknown"
    )

    customer_segment = st.selectbox(
        "Customer Segment",
        ["Regular", "Premium", "New"]
    )

with col2:

    payment_method = st.selectbox(
        "Payment Method",
        ["Credit Card", "Debit Card", "UPI", "Cash"]
    )

    sales_channel = st.selectbox(
        "Sales Channel",
        ["Online", "Offline"]
    )

    region = st.selectbox(
        "Region",
        ["North", "South", "East", "West"]
    )

    month = st.selectbox(
        "Month",
        list(range(1, 13))
    )

    year = st.number_input(
        "Year",
        min_value=2000,
        max_value=2100,
        value=2026
    )

    day = st.number_input(
        "Day",
        min_value=1,
        max_value=31,
        value=1
    )

    day_of_week = st.selectbox(
        "Day of Week",
        list(range(7))
    )


# --------------------------------
# 6. Prediction
# --------------------------------

st.divider()

if st.button("Predict Sales Amount", type="primary"):

    try:

        input_data = pd.DataFrame([{
            "quantity": quantity,
            "unit_price": unit_price,
            "discount_pct": discount_pct,
            "category": category,
            "brand": brand,
            "customer_segment": customer_segment,
            "payment_method": payment_method,
            "sales_channel": sales_channel,
            "region": region,
            "month": month,
            "year": year,
            "day": day,
            "day_of_week": day_of_week
        }])

        prediction = model.predict(input_data)[0]

        st.success("Prediction Successful!")

        st.metric(
            label="Predicted Sales Amount",
            value=f"₹ {prediction:,.2f}"
        )

    except Exception as e:

        st.error(f"Prediction Error: {str(e)}")


# --------------------------------
# 7. Footer
# --------------------------------

st.divider()

st.caption(
    "Retail Sales Prediction | Machine Learning | Scikit-learn"
)
