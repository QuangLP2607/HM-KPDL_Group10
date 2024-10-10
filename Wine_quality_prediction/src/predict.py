import pandas as pd # type: ignore
import joblib # type: ignore

# Đọc mô hình đã lưu
model = joblib.load('D:/Wine_quality_prediction/models/wine_quality_model.pkl')

# Đọc label encoders đã lưu
label_encoders = joblib.load('D:/Wine_quality_prediction/models/label_encoders.pkl')

# Dữ liệu mẫu
sample_data = {
    'winery': ['A Coroa'],
    'region': ['Abona'],
    'country': ['Espana'],
    'type': ['Tempranillo'],
    'year': [1990],
    'wine': ['1730 Amontillado'],
    'price': [25.0],
    'num_reviews': [500],
    'acidity': [3.5],
    'body': [4.0]
}

sample_df = pd.DataFrame(sample_data)

# Kiểm tra và chuyển đổi kiểu dữ liệu cột 'year'
sample_df['year'] = sample_df['year'].astype(str).str.strip()  # Chuyển đổi thành chuỗi và loại bỏ khoảng trắng

# Mã hóa các cột chuỗi
for column in label_encoders:
    if column in sample_df.columns:
        try:
            sample_df[column] = label_encoders[column].transform(sample_df[column])
        except KeyError as e:
            print(f"Lỗi mã hóa cho cột {column}: {e}")

# Đảm bảo thứ tự cột khớp với tên tính năng của mô hình
model_feature_names = model.feature_names_in_  # Lấy tên tính năng từ mô hình
sample_df = sample_df[list(model_feature_names)]  # Đảm bảo thứ tự khớp

# Dự đoán chất lượng rượu
predictions = model.predict(sample_df)
print(f"Dự đoán chất lượng rượu: {predictions[0]}")
