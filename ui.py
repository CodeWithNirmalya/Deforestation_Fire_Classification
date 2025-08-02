import streamlit as st
import numpy as np
import joblib
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container

# Load model and scaler
model = joblib.load("best_fire_detection_model.pkl")
scaler = joblib.load("scaler.pkl")

# Page config
st.set_page_config(
    page_title="🔥 FireWatch AI",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }
        
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #f8f9fa 100%);
        }
        
        .title-text {
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(90deg, #FF4B4B 0%, #FF8E53 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        
        .subtitle-text {
            font-size: 1.1rem;
            text-align: center;
            color: #666;
            margin-bottom: 2rem;
        }
        
        .feature-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        }
        
        .input-label {
            font-weight: 600;
            color: #444;
            margin-bottom: 0.5rem;
            display: block;
        }
        
        .stButton>button {
            background: linear-gradient(90deg, #FF4B4B 0%, #FF8E53 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 28px;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(255, 75, 75, 0.3);
        }
        
        .result-card {
            background: linear-gradient(135deg, #FFF3F3 0%, #FFFFFF 100%);
            border-left: 5px solid #FF4B4B;
            border-radius: 0 12px 12px 0;
            padding: 2rem;
            margin-top: 2rem;
        }
        
        .result-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #FF4B4B;
            margin-bottom: 1rem;
        }
        
        .result-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #333;
        }
        
        .icon-large {
            font-size: 2rem;
            margin-right: 0.5rem;
            vertical-align: middle;
        }
        
        .divider {
            height: 3px;
            background: linear-gradient(90deg, #FF4B4B 0%, #FF8E53 100%);
            border: none;
            margin: 2rem 0;
            border-radius: 3px;
        }
        
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #2C3E50 0%, #1A1A2E 100%);
            color: white;
        }
        
        .sidebar-title {
            color: white;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            text-align: center;
        }
        
        .sidebar-text {
            color: #ddd;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-title">FireWatch AI</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="sidebar-text">
        This advanced classifier uses MODIS satellite data to predict different types of fires with high accuracy.
        <br><br>
        Simply adjust the parameters and click "Predict" to get real-time classification results.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
        <div class="sidebar-text">
        <b>How it works:</b>
        <ol>
            <li>Adjust the satellite parameters</li>
            <li>Click the predict button</li>
            <li>Get instant fire classification</li>
        </ol>
        </div>
    """, unsafe_allow_html=True)

# Main content
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="title-text">FireWatch AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Advanced Fire Type Classification using MODIS Satellite Data</div>', unsafe_allow_html=True)
    
    # Feature cards in a 2x2 grid
    grid1 = st.columns(2)
    grid2 = st.columns(2)
    
    with grid1[0]:
        with stylable_container(
            key="brightness_card",
            css_styles="""
                {
                    background: white;
                    border-radius: 12px;
                    padding: 1.5rem;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                }
            """
        ):
            st.markdown('<span class="icon-large">🔆</span> <span class="input-label">Brightness</span>', unsafe_allow_html=True)
            brightness = st.slider("Brightness (Kelvin)", 290.0, 400.0, 300.0, 1.0, label_visibility="collapsed")
    
    with grid1[1]:
        with stylable_container(
            key="frp_card",
            css_styles="""
                {
                    background: white;
                    border-radius: 12px;
                    padding: 1.5rem;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                }
            """
        ):
            st.markdown('<span class="icon-large">🔥</span> <span class="input-label">Fire Radiative Power</span>', unsafe_allow_html=True)
            frp = st.slider("FRP (MW)", 1.0, 100.0, 15.0, 1.0, label_visibility="collapsed")
    
    with grid2[0]:
        with stylable_container(
            key="bright_t31_card",
            css_styles="""
                {
                    background: white;
                    border-radius: 12px;
                    padding: 1.5rem;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                }
            """
        ):
            st.markdown('<span class="icon-large">🌡️</span> <span class="input-label">Brightness T31</span>', unsafe_allow_html=True)
            bright_t31 = st.slider("Brightness T31 (Kelvin)", 280.0, 350.0, 290.0, 1.0, label_visibility="collapsed")
    
    with grid2[1]:
        with stylable_container(
            key="confidence_card",
            css_styles="""
                {
                    background: white;
                    border-radius: 12px;
                    padding: 1.5rem;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                }
            """
        ):
            st.markdown('<span class="icon-large">✅</span> <span class="input-label">Confidence Level</span>', unsafe_allow_html=True)
            confidence = st.selectbox("Confidence", ["low", "nominal", "high"], label_visibility="collapsed")

with col2:
    with stylable_container(
        key="additional_params",
        css_styles="""
            {
                background: white;
                border-radius: 12px;
                padding: 2rem;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                height: 100%;
            }
        """
    ):
        st.markdown('<div style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1.5rem; color: #444;">Additional Parameters</div>', unsafe_allow_html=True)
        
        st.markdown('<span class="icon-large">🛰️</span> <span class="input-label">Scan</span>', unsafe_allow_html=True)
        scan = st.slider("Scan", 0.1, 5.0, 1.0, 0.1, label_visibility="collapsed")
        
        st.markdown('<span class="icon-large">📍</span> <span class="input-label">Track</span>', unsafe_allow_html=True)
        track = st.slider("Track", 0.1, 5.0, 1.0, 0.1, label_visibility="collapsed")
        
        # Prediction button centered at bottom
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Predict Fire Type", type="primary"):
            # Map confidence to numeric
            confidence_map = {"low": 0, "nominal": 1, "high": 2}
            confidence_val = confidence_map[confidence]
            
            input_data = np.array([[brightness, bright_t31, frp, scan, track, confidence_val]])
            scaled_input = scaler.transform(input_data)
            prediction = model.predict(scaled_input)[0]
            
            fire_types = {
                0: ("🌿 Vegetation Fire", "#2ecc71"),
                2: ("🏞️ Other Static Land Source", "#3498db"),
                3: ("🌊 Offshore Fire", "#9b59b6")
            }
            
            result, color = fire_types.get(prediction, ("❓ Unknown Fire Type", "#e74c3c"))
            
            # Display result in a beautiful card
            with stylable_container(
                key="result_card",
                css_styles=f"""
                    {{
                        background: linear-gradient(135deg, #f9f9f9 0%, #ffffff 100%);
                        border-left: 5px solid {color};
                        border-radius: 0 12px 12px 0;
                        padding: 2rem;
                        margin-top: 2rem;
                    }}
                """
            ):
                st.markdown(f'<div class="result-title">Prediction Result</div>', unsafe_allow_html=True)
                st.markdown(f'<div style="font-size: 2rem; font-weight: 700; color: {color};">{result}</div>', unsafe_allow_html=True)
                
                # Add some visual feedback based on prediction
                if prediction == 0:
                    st.success("This appears to be a vegetation fire, possibly forest or grassland.")
                elif prediction == 2:
                    st.info("This fire is likely from a static land source like agricultural burning.")
                elif prediction == 3:
                    st.warning("This detection suggests an offshore fire, possibly gas flares or oil fires.")
                else:
                    st.error("The fire type couldn't be determined with confidence.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #777; font-size: 0.9rem; margin-top: 3rem;">
        FireWatch AI • MODIS Satellite Data Analysis • © 2023
    </div>
""", unsafe_allow_html=True)