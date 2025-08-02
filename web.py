import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("best_fire_detection_model.pkl")
scaler = joblib.load("scaler.pkl")

# Page config
st.set_page_config(page_title="🔥 Fire Type Classifier", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: 700;
            color: #FF4B4B;
            text-align: center;
        }
        .subtext {
            font-size: 18px;
            text-align: center;
            color: #555;
        }
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
        }
        .stButton>button:hover {
            background-color: #d13b3b;
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="title">🔥 Fire Type Classification</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Predict fire types using MODIS satellite input features</div>', unsafe_allow_html=True)
st.markdown("---")

# Input layout using columns
col1, col2 = st.columns(2)

with col1:
    brightness = st.number_input("🔆 Brightness", value=300.0, step=1.0)
    frp = st.number_input("🔥 Fire Radiative Power (FRP)", value=15.0, step=1.0)
    scan = st.number_input("🛰️ Scan", value=1.0, step=0.1)

with col2:
    bright_t31 = st.number_input("🌡️ Brightness T31", value=290.0, step=1.0)
    track = st.number_input("📍 Track", value=1.0, step=0.1)
    confidence = st.selectbox("✅ Confidence Level", ["low", "nominal", "high"])

# Map confidence to numeric
confidence_map = {"low": 0, "nominal": 1, "high": 2}
confidence_val = confidence_map[confidence]

# Prediction
st.markdown("### 🔍 Prediction Result")
if st.button("Predict Fire Type"):
    input_data = np.array([[brightness, bright_t31, frp, scan, track, confidence_val]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]

    fire_types = {
        0: "🌿 Vegetation Fire",
        2: "🏞️ Other Static Land Source",
        3: "🌊 Offshore Fire"
    }

    result = fire_types.get(prediction, "❓ Unknown")
    st.success(f"**Predicted Fire Type:** {result}")
