import pandas as pd  # type: ignore # Nhập thư viện pandas để làm việc với dữ liệu
from sklearn.model_selection import train_test_split  # type: ignore # Nhập hàm để chia dữ liệu
from sklearn.ensemble import RandomForestRegressor  # type: ignore # Nhập mô hình Random Forest
from sklearn.metrics import mean_squared_error, r2_score  # type: ignore # Nhập các hàm đánh giá
from sklearn.preprocessing import LabelEncoder  # type: ignore # Nhập LabelEncoder
import joblib  # type: ignore # Nhập thư viện để lưu mô hình

# Đọc dữ liệu đã xử lý
file_path = 'D:/Wine_quality_prediction/data/processed/wines_processed.csv'  # Đường dẫn tới file dữ liệu đã xử lý
df = pd.read_csv(file_path)  # Đọc dữ liệu từ file CSV

# Mã hóa các cột chuỗi
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le  # Lưu label encoder nếu cần sử dụng lại sau này
    print(f"Giá trị mã hóa cho cột {column}: {le.classes_}")  # In ra giá trị đã mã hóa

# Chọn các đặc trưng (features) và nhãn (target)
X = df.drop(columns=['rating'])  # Các cột đặc trưng
y = df['rating']  # Cột nhãn

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Khởi tạo mô hình Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Lưu mô hình
joblib.dump(model, 'D:/Wine_quality_prediction/models/wine_quality_model.pkl')
print("Mô hình đã được lưu.")
# Lưu label encoders
joblib.dump(label_encoders, 'D:/Wine_quality_prediction/models/label_encoders.pkl')
print("Label encoders đã được lưu.")
