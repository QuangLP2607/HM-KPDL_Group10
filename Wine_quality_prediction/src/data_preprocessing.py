# Kiểm tra và điền dữ liệu còn thiếu trong DataFrame.

import pandas as pd  # type: ignore # Nhập thư viện pandas để làm việc với dữ liệu

# Load the dataset
def load_data(file_path):
    # Đọc file CSV và trả về DataFrame
    return pd.read_csv(file_path)

# Preprocess the dataset
def preprocess_data(df):
    # Chọn các cột số trong DataFrame
    num_cols = df.select_dtypes(include=['number']).columns
    # Điền giá trị thiếu trong các cột số bằng giá trị trung bình của cột đó
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

    # Điền giá trị thiếu trong cột 'type' bằng giá trị xuất hiện nhiều nhất (mode)
    df['type'] = df['type'].fillna(df['type'].mode()[0])
    # Điền giá trị thiếu trong cột 'body' bằng giá trị xuất hiện nhiều nhất (mode)
    df['body'] = df['body'].fillna(df['body'].mode()[0])
    # Điền giá trị thiếu trong cột 'acidity' bằng giá trị xuất hiện nhiều nhất (mode)
    df['acidity'] = df['acidity'].fillna(df['acidity'].mode()[0])
    
    return df  # Trả về DataFrame đã được xử lý

# Định nghĩa đường dẫn file
raw_file_path = 'D:/Wine_quality_prediction/data/raw/wines_SPA.csv'  # Đường dẫn tới file dữ liệu gốc
processed_file_path = 'D:/Wine_quality_prediction/data/processed/wines_processed.csv'  # Đường dẫn tới file lưu dữ liệu đã xử lý

# Chạy script
df = load_data(raw_file_path)  # Tải dữ liệu từ file CSV
print("Missing values:\n", df.isnull().sum())  # In ra số lượng giá trị thiếu trong từng cột

df = preprocess_data(df)  # Xử lý dữ liệu
print(df.head())  # In ra 5 dòng đầu tiên của DataFrame đã được xử lý

# Lưu DataFrame đã xử lý vào một file mới
df.to_csv(processed_file_path, index=False)  # Lưu DataFrame vào file CSV mới, không lưu chỉ số hàng
print(f"Processed data saved to {processed_file_path}")  # Thông báo rằng dữ liệu đã được lưu

# Xử lý giá trị bị thiếu trong cột 'year'
# 1. Kiểm tra các giá trị bị thiếu
print("\nGiá trị bị thiếu trước khi xử lý:")
print(df['year'].isnull().sum())

# 2. Điền giá trị thiếu bằng giá trị phổ biến (mode)
df['year'] = df['year'].fillna(df['year'].mode()[0])

# 3. Kiểm tra lại các giá trị bị thiếu sau khi xử lý
print("\nGiá trị bị thiếu sau khi xử lý:")
print(df['year'].isnull().sum())  # In ra số lượng giá trị thiếu sau khi xử lý
