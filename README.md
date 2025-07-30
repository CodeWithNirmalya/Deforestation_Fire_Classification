> ⚠️ **Note:** GitHub may not display the full code if the file is large.  
> To view the complete code,Please click the **“Raw”** button or **download** the file to view it properly.
### To view the complete notebook without any truncation, open it using **nbviewer**:

👉 [Click here to view the full notebook in nbviewer](https://nbviewer.org/github/CodeWithNirmalya/Deforestation_Fire_Classification)
# 🌲 Deforestation Fire Classification

# 🔥 Fire Detection in India Using MODIS Satellite Data (2021–2023)

## 📌 Project Overview

This project analyzes MODIS satellite fire detection data for India from **2021 to 2023**. The workflow includes data loading, cleaning, exploratory data analysis (EDA), feature engineering, handling class imbalance, model training, evaluation, and selection of the best performing classifier.

## 📂 Data Preparation

- **Data Sources**: MODIS fire detection CSV files for 2021, 2022, and 2023.
- **Preprocessing**:
  - Dataframes were concatenated.
  - Missing values and duplicates were checked.
  - Outliers were removed using the **IQR method**.
- **Feature Engineering**:
  - Temporal features (year, month, day of week, etc.) were extracted from acquisition dates.
  - Categorical variables were one-hot encoded.
  - Numerical features were standardized.

## 📊 Exploratory Data Analysis (EDA)

- **Distribution Analysis**:
  - Count plots for fire types, day/night flags, satellite, and instrument.
  - Histograms and boxplots for numerical features.
- **Geographical Analysis**:
  - Fire locations were plotted on a map of India.
- **Correlation Analysis**:
  - Heatmaps and pairplots were used to reveal relationships between features.

## ⚖️ Handling Class Imbalance

- **SMOTE** (Synthetic Minority Over-sampling Technique) was applied to balance the target classes before model training.

## 🤖 Model Training and Evaluation

Four classification algorithms were trained and evaluated:

1. Logistic Regression  
2. Decision Tree  
3. Random Forest  
4. K-Nearest Neighbors  

**Performance Evaluation**:
- Accuracy
- Classification Report
- Confusion Matrix

## 🏆 Results

- **Random Forest** achieved the highest accuracy of **0.9780**, outperforming other models.
- The best model and the scaler were saved for preprocessing and future use.

## 🛠️ Tools & Technologies Used

- **Programming Language**: Python  
- **Data Manipulation**: NumPy, Pandas  
- **Data Visualization**: Matplotlib, Seaborn  
- **Machine Learning**: Scikit-learn, XGBoost  
- **Data Balancing**: imbalanced-learn (SMOTE)  
- **Geospatial Mapping**: Matplotlib Basemap (optional if used)

## ✅ Conclusion

This project demonstrates a complete **machine learning pipeline** for satellite-based fire detection in India. After thorough data cleaning, feature engineering, and model comparison, the **Random Forest classifier** was selected as the best model due to its superior accuracy and robustness.

This approach can be extended to other regions or future years, and the trained model can be integrated into **real-time fire detection and monitoring systems**.

---

### 📁 Project Structure (Optional)

```bash
Fire-Detection-MODIS/
├── data/
│   ├── fire_data_2021.csv
│   ├── fire_data_2022.csv
│   └── fire_data_2023.csv
├── notebooks/
│   └── fire_detection_analysis.ipynb
├── models/
│   
│   └── scaler.pkl
├── README.md
└── requirements.txt
```
### 👨‍💻 Author

**Nirmalya Raja**  
[GitHub – CodeWithNirmalya](https://github.com/CodeWithNirmalya)  
Email: [work.nirmalyaraja@gmail.com]


