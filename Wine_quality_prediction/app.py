import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc mô hình đã lưu và label encoders
model = joblib.load('D:/Wine_quality_prediction/models/wine_quality_model.pkl')
label_encoders = joblib.load('D:/Wine_quality_prediction/models/label_encoders.pkl')
data = pd.read_csv('D:/Wine_quality_prediction/data/processed/wines_processed.csv')

# Tiêu đề ứng dụng
st.title('Dự đoán chất lượng rượu')

# Nhập thông tin rượu từ người dùng
winery = st.text_input('Winery', 'A Coroa')
region = st.text_input('Region', 'Abona')
country = st.text_input('Country', 'Espana')
wine_type = st.text_input('Type', 'Tempranillo')
year = st.number_input('Year', min_value=1900, max_value=2023, value=1990)
wine_name = st.text_input('Wine Name', '1730 Amontillado')
price = st.number_input('Price', min_value=0.0, value=25.0)
num_reviews = st.number_input('Number of Reviews', min_value=0, value=500)
acidity = st.number_input('Acidity', value=3.5)
body = st.number_input('Body', value=4.0)

# Nút để dự đoán
if st.button('Dự đoán'):
    # Dữ liệu mẫu
    sample_data = {
        'winery': [winery],
        'region': [region],
        'country': [country],
        'type': [wine_type],
        'year': [year],
        'wine': [wine_name],
        'price': [price],
        'num_reviews': [num_reviews],
        'acidity': [acidity],
        'body': [body]
    }
    
    sample_df = pd.DataFrame(sample_data)

    # Tiền xử lý dữ liệu tương tự như trong predict.py
    sample_df['year'] = sample_df['year'].astype(str).str.strip()

    for column in label_encoders:
        if column in sample_df.columns:
            sample_df[column] = label_encoders[column].transform(sample_df[column])

    model_feature_names = model.feature_names_in_
    sample_df = sample_df[list(model_feature_names)]

    # Dự đoán chất lượng rượu
    predictions = model.predict(sample_df)
    st.write(f'Dự đoán chất lượng rượu: {predictions[0]}')

    # Thống kê dữ liệu và phân tích trực quan
    st.subheader('Phân tích chất lượng rượu theo năm')
    trend_data = data.groupby('year')['rating'].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=trend_data, x='year', y='rating')
    plt.title('Trung bình đánh giá chất lượng rượu theo năm')
    plt.xlabel('Năm')
    plt.ylabel('Đánh giá trung bình')
    st.pyplot(plt)

    # Thông tin các loại rượu tương tự
    similar_wines = data[(data['type'] == wine_type) & (data['year'] == year)]
    st.subheader('Các loại rượu tương tự')
    st.write(similar_wines[['winery', 'wine', 'rating', 'price']])
