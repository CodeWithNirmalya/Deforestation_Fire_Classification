> ⚠️ **Note:** GitHub may not display the full code if the file is large.  
> To view the complete code,Please click the **“Raw”** button or **download** the file to view it properly.
### To view the complete notebook without any truncation, open it using **nbviewer**:

👉 [Click here to view the full notebook in nbviewer](https://nbviewer.org/github/CodeWithNirmalya/Deforestation_Fire_Classification)
# 🌲 Deforestation Fire Classification

## Fire Detection in India Using MODIS Satellite Data (2021-2023)
### Project Overview
This project analyzes MODIS satellite fire detection data for India from 2021 to 2023. The workflow includes data loading, cleaning, exploratory data analysis (EDA), feature engineering, handling class imbalance, model training, evaluation, and selection of the best performing classifier.

### Data Preparation
### Data Sources: 
MODIS fire detection CSV files for 2021, 2022, and 2023.
### Preprocessing: 
Dataframes were concatenated, missing values and duplicates were checked, and outliers were removed using the IQR method.
### Feature Engineering: 
Temporal features (year, month, day of week, etc.) were extracted from acquisition dates. Categorical variables were one-hot encoded, and numerical features were standardized.
### Exploratory Data Analysis (EDA)
### Distribution Analysis: 
Visualizations included count plots for fire types, day/night, satellite, and instrument, as well as histograms and boxplots for numerical features.
### Geographical Analysis: 
Fire locations were plotted on a map of India.
### Correlation Analysis: 
Heatmaps and pairplots revealed relationships between features.
Handling Class Imbalance
### SMOTE: 
Synthetic Minority Over-sampling Technique (SMOTE) was applied to balance the target classes before model training.
Model Training and Evaluation
Four classification algorithms were trained and evaluated:

#### Logistic Regression
#### Decision Tree
#### Random Forest
#### K-Nearest Neighbors
Performance was measured using accuracy, classification reports, and confusion matrices.

## Results
Random Forest achieved the highest accuracy (0.9780), outperforming other models.
The model was saved for future use, along with the scaler for preprocessing new data.
Conclusion
This project demonstrates a complete machine learning pipeline for satellite-based fire detection in India. After thorough data cleaning, feature engineering, and model comparison, the Random Forest classifier was selected as the best model due to its superior accuracy and robustness. This approach can be extended to other regions or years, and the trained model can be deployed for real-time fire detection and monitoring applications.
## 🔗 Author

- **Nirmalya Raja**  
  [GitHub](https://github.com/CodeWithNirmalya)

