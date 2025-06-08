import streamlit as st
import pandas as pd
import joblib

# Load model & scaler
model = joblib.load('model/rf_model.joblib')
scaler = joblib.load('model/scaler.joblib')

# Fitur yang perlu diskalakan
features_to_scale = [
    'Previous_qualification_grade',
    'Admission_grade',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade'
]

features_not_scaled = ['Age_at_enrollment']

categorical_features = {
    'Marital_status': ['Single', 'Married', 'Divorced'],
    'Daytime_evening_attendance': ['Daytime', 'Evening'],
    'Displaced': ['Yes', 'No'],
    'Debtor': ['Yes', 'No'],
    'Tuition_fees_up_to_date': ['Yes', 'No'],
    'Gender': ['Male', 'Female'],
    'Scholarship_holder': ['Yes', 'No']
}

category_mapping = {
    'Yes': 1, 'No': 0,
    'Male': 1, 'Female': 0,
    'Daytime' : 1, 'Evening' : 0,
    'Single': 1, 'Married': 2, 'Divorced': 3
}

# UI
st.title("🎓 Prediksi Status Mahasiswa (App)")
st.markdown("Prototype untuk klasifikasi status mahasiswa: **Dropout**, **Graduate**, atau **Enrolled**.")
st.write("Masukkan data mahasiswa di bawah ini:")

# Input KATEGORIKAL
categorical_input = {}
with st.expander("🔘 Informasi Kategorikal"):
    cols = st.columns(3)
    for i, (feature, options) in enumerate(categorical_features.items()):
        selected = cols[i % 3].selectbox(feature, options)
        categorical_input[feature] = category_mapping[selected]

# Input NUMERIK
numeric_input = {}
with st.expander("📈 Informasi Numerik"):
    cols = st.columns(3)
    for i, feature in enumerate(features_to_scale + features_not_scaled):
        numeric_input[feature] = cols[i % 3].number_input(feature, step=0.1)

# Gabungkan input
user_input = {**categorical_input, **numeric_input}

# Prediksi
if st.button("Predict"):
    input_df = pd.DataFrame([user_input])

    # Transform semua kolom sesuai urutan dan format saat training
    input_scaled = scaler.transform(input_df)

    # Prediksi
    pred = model.predict(input_scaled)[0]
    pred_proba = model.predict_proba(input_scaled)[0]

    label_map = {0: "Dropout", 1: "Graduate", 2: "Enrolled"}

    st.success(f"Hasil Prediksi: **{label_map[pred]}**")
    st.write("Probabilitas:")
    st.bar_chart({
        "Dropout": [pred_proba[0]],
        "Graduate": [pred_proba[1]],
        "Enrolled": [pred_proba[2]]
    })