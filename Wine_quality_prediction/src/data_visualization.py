import pandas as pd  # type: ignore # Nhập thư viện pandas để làm việc với dữ liệu
import matplotlib.pyplot as plt  # type: ignore # Nhập thư viện matplotlib để vẽ biểu đồ

# Đọc dữ liệu đã xử lý
file_path = 'D:/Wine_quality_prediction/data/processed/wines_processed.csv'  # Đường dẫn tới file dữ liệu đã xử lý
df = pd.read_csv(file_path)  # Đọc dữ liệu từ file CSV

# Tạo biểu đồ phân phối giá rượu
plt.figure(figsize=(10, 6))  # Thiết lập kích thước của biểu đồ
plt.hist(df['price'], bins=30, color='blue', alpha=0.7)  # Vẽ biểu đồ histogram cho giá
plt.title('Phân phối Giá Rượu')  # Tiêu đề của biểu đồ
plt.xlabel('Giá')  # Nhãn cho trục x
plt.ylabel('Số lượng')  # Nhãn cho trục y
plt.grid(axis='y')  # Thêm lưới cho trục y
plt.show()  # Hiển thị biểu đồ

# Tạo biểu đồ phân phối đánh giá (rating)
plt.figure(figsize=(10, 6))
plt.hist(df['rating'], bins=30, color='green', alpha=0.7)  # Vẽ biểu đồ histogram cho đánh giá
plt.title('Phân phối Đánh Giá Rượu')  # Tiêu đề của biểu đồ
plt.xlabel('Đánh Giá')  # Nhãn cho trục x
plt.ylabel('Số lượng')  # Nhãn cho trục y
plt.grid(axis='y')  # Thêm lưới cho trục y
plt.show()  # Hiển thị biểu đồ

# Tạo biểu đồ phân phối số lượng đánh giá (num_reviews)
plt.figure(figsize=(10, 6))
plt.hist(df['num_reviews'], bins=30, color='orange', alpha=0.7)  # Vẽ biểu đồ histogram cho số lượng đánh giá
plt.title('Phân phối Số Lượng Đánh Giá Rượu')  # Tiêu đề của biểu đồ
plt.xlabel('Số Lượng Đánh Giá')  # Nhãn cho trục x
plt.ylabel('Số lượng')  # Nhãn cho trục y
plt.grid(axis='y')  # Thêm lưới cho trục y
plt.show()  # Hiển thị biểu đồ

# Tạo biểu đồ hộp (box plot) giá theo loại rượu
plt.figure(figsize=(12, 6))
df.boxplot(column='price', by='type', grid=False)  # Vẽ biểu đồ hộp cho giá theo loại rượu
plt.title('Giá Rượu theo Loại')  # Tiêu đề của biểu đồ
plt.suptitle('')  # Xóa tiêu đề mặc định
plt.xlabel('Loại Rượu')  # Nhãn cho trục x
plt.ylabel('Giá')  # Nhãn cho trục y
plt.xticks(rotation=45)  # Xoay nhãn cho trục x để dễ đọc
plt.show()  # Hiển thị biểu đồ

# Tạo biểu đồ hộp cho đánh giá theo loại rượu
plt.figure(figsize=(12, 6))
df.boxplot(column='rating', by='type', grid=False)  # Vẽ biểu đồ hộp cho đánh giá theo loại rượu
plt.title('Đánh Giá Rượu theo Loại')  # Tiêu đề của biểu đồ
plt.suptitle('')  # Xóa tiêu đề mặc định
plt.xlabel('Loại Rượu')  # Nhãn cho trục x
plt.ylabel('Đánh Giá')  # Nhãn cho trục y
plt.xticks(rotation=45)  # Xoay nhãn cho trục x để dễ đọc
plt.show()  # Hiển thị biểu đồ

# Tạo biểu đồ phân tán giữa giá và đánh giá
plt.figure(figsize=(10, 6))
plt.scatter(df['price'], df['rating'], alpha=0.5, color='purple')  # Vẽ biểu đồ phân tán giữa giá và đánh giá
plt.title('Giá và Đánh Giá Rượu')  # Tiêu đề của biểu đồ
plt.xlabel('Giá')  # Nhãn cho trục x
plt.ylabel('Đánh Giá')  # Nhãn cho trục y
plt.grid()  # Thêm lưới cho biểu đồ
plt.show()  # Hiển thị biểu đồ
