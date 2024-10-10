import pandas as pd # type: ignore

# Đường dẫn đến file dữ liệu đã xử lý
file_path = 'D:/Wine_quality_prediction/data/processed/wines_processed.csv'

# Tải dữ liệu
df = pd.read_csv(file_path)

# Phân tích dữ liệu
print("Thông tin về dữ liệu:")
print(df.info())  # Thông tin tổng quát về DataFrame

print("\nMô tả thống kê:")
print(df.describe())  # Thống kê mô tả cho các cột số

print("\nSố lượng mỗi loại rượu:")
print(df['type'].value_counts())  # Đếm số lượng các loại rượu

# Kiểm tra giá trị bị thiếu
print("\nGiá trị bị thiếu:")
print(df.isnull().sum())
