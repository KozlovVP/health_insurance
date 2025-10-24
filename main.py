import streamlit as st
import pandas as pd
from prediction_helper import predict

# Настройка страницы
st.set_page_config(page_title="Insurance Form", page_icon="📋", layout="wide")

# Инициализация session_state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'user_data' not in st.session_state:
    st.session_state.user_data = None

# Заголовок приложения
st.title("Health Insurance Prediction App")
st.markdown("---")

# Создаем колонки для компактного расположения
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👤 Personal Information")

    # Age (от 18 до 100)
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        step=1,
        help="Enter age from 18 to 100 years"
    )

    # Gender
    gender = st.selectbox(
        "Gender",
        ['Male', 'Female'],
        index=0
    )

    # Region
    region = st.selectbox(
        "Region",
        ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
        index=0
    )

    # Marital Status
    marital_status = st.selectbox(
        "Marital Status",
        ['Unmarried', 'Married'],
        index=0
    )

    # Number Of Dependants (от 0 до 5)
    number_of_dependants = st.number_input(
        "Number Of Dependants",
        min_value=0,
        max_value=5,
        value=0,
        step=1,
        help="Number of family dependants (0 to 5)"
    )

with col2:
    st.subheader("🏥 Medical Information")

    # BMI Category
    bmi_category = st.selectbox(
        "BMI Category",
        ['Normal', 'Obesity', 'Overweight', 'Underweight'],
        index=0
    )

    # Smoking Status
    smoking_status = st.selectbox(
        "Smoking Status",
        ['No Smoking', 'Regular', 'Occasional'],
        index=0
    )

    # Medical History
    medical_history = st.selectbox(
        "Medical History",
        [
            'No Disease',
            'Diabetes',
            'High blood pressure',
            'Thyroid',
            'Heart disease',
            'Diabetes & High blood pressure',
            'High blood pressure & Heart disease',
            'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ],
        index=0
    )

    # Genetical Risk
    genetical_risk = st.number_input(
        "Medical Risk",
        min_value=0,
        max_value=5,
        value=0,
        step=1,
    )

with col3:
    st.subheader("💰 Financial Information")

    # Employment Status
    employment_status = st.selectbox(
        "Employment Status",
        ['Salaried', 'Self-Employed', 'Freelancer'],
        index=0
    )

    # Income Lakhs (целое число от 0 до 100)
    income_lakhs = st.number_input(
        "Income (in Lakhs)",
        min_value=0,
        max_value=100,
        value=5,
        step=1,
        help="Annual income in lakhs (e.g., 5 = ₹5,00,000)"
    )

    # Insurance Plan
    insurance_plan = st.selectbox(
        "Insurance Plan",
        ['Bronze', 'Silver', 'Gold'],
        index=0
    )

st.markdown("---")

# Кнопка отправки по центру
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    submit_clicked = st.button("Submit Data", type="primary", use_container_width=True)

    if submit_clicked:
        # Сбор всех данных в формате для модели
        user_data = {
            "Age": age,
            "Gender": gender,
            "Region": region,
            "Marital_status": marital_status,
            "Number Of Dependants": number_of_dependants,
            "BMI_Category": bmi_category,
            "Smoking_Status": smoking_status,
            "Employment_Status": employment_status,
            "Income_Lakhs": income_lakhs,
            "Medical History": medical_history,
            "Insurance_Plan": insurance_plan,
            "Genetical Risk": genetical_risk
        }

        # Сохраняем в session_state
        st.session_state.user_data = user_data
        st.session_state.submitted = True
        st.rerun()

# Показываем результаты если данные были отправлены
if st.session_state.submitted and st.session_state.user_data is not None:
    user_data = st.session_state.user_data

    # Отображение собранных данных
    st.success("✅ Data successfully collected!")
    st.subheader("Collected Data:")

    # Отображение данных в колонках
    col_data1, col_data2 = st.columns(2)

    with col_data1:
        st.write(f"**Age:** {user_data['Age']}")
        st.write(f"**Gender:** {user_data['Gender']}")
        st.write(f"**Region:** {user_data['Region']}")
        st.write(f"**Marital Status:** {user_data['Marital_status']}")
        st.write(f"**Number Of Dependants:** {user_data['Number Of Dependants']}")
        st.write(f"**BMI Category:** {user_data['BMI_Category']}")
        st.write(f"**Smoking Status:** {user_data['Smoking_Status']}")

    with col_data2:
        st.write(f"**Employment Status:** {user_data['Employment_Status']}")
        st.write(f"**Income (Lakhs):** {user_data['Income_Lakhs']}")
        st.write(f"**Medical History:** {user_data['Medical History']}")
        st.write(f"**Insurance Plan:** {user_data['Insurance_Plan']}")
        st.write(f"**Genetical Risk:** {user_data['Genetical Risk']}")

    # Кнопка для предсказания
    col_pred1, col_pred2, col_pred3 = st.columns([1, 2, 1])
    with col_pred2:
        if st.button("Make Prediction", type="secondary", use_container_width=True):
            st.info("🔮 Making prediction...")

            # Вызов функции predict с СЛОВАРЕМ вместо DataFrame
            prediction = predict(user_data)  # ← Передаем словарь напрямую

            st.success(f"Prediction result: {prediction}")

    # Кнопка сброса
    col_reset1, col_reset2, col_reset3 = st.columns([1, 2, 1])
    with col_reset2:
        if st.button("Reset Form", use_container_width=True):
            st.session_state.submitted = False
            st.session_state.user_data = None
            st.rerun()