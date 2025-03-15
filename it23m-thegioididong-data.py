from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Thiết lập các tùy chọn cho Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Chạy Chrome ở chế độ không hiển thị (headless)
chrome_options.add_argument("--disable-gpu")  # Vô hiệu hóa GPU (tùy chọn)

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Mở trang web
driver.get("https://www.thegioididong.com/dtdd-apple-iphone?key=iphone&sc=new")

# Tìm tất cả các phần tử chứa thông tin sản phẩm
products = driver.find_elements(By.CSS_SELECTOR, "ul.listproduct li.item")

# Duyệt qua từng sản phẩm và lấy tên cùng giá
for product in products:
    try:
        # Lấy tên sản phẩm
        name = product.find_element(By.CSS_SELECTOR, "h3").text

        # Lấy giá sản phẩm
        price = product.find_element(By.CSS_SELECTOR, "strong.price").text

        # In ra tên và giá
        print(f"Tên sản phẩm: {name} - Giá: {price}")
    except Exception as e:
        # Nếu có lỗi (ví dụ: phần tử không có giá), bỏ qua sản phẩm này
        continue

# Đóng trình duyệt
driver.quit()