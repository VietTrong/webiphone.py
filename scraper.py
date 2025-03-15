from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pymysql

# Kết nối đến MySQL trong XAMPP
connection = pymysql.connect(
    host="localhost",
    user="root",   # Mặc định là "root"
    password="",   # Mặc định là rỗng
    database="thegioididong",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

try:
    # Thiết lập Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy ẩn
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Truy cập trang web
    driver.get("https://www.thegioididong.com/dtdd-apple-iphone?key=iphone&sc=new")

    # Tìm tất cả sản phẩm
    products = driver.find_elements(By.CSS_SELECTOR, "ul.listproduct li.item")

    # Duyệt qua từng sản phẩm và lưu vào CSDL
    with connection.cursor() as cursor:
        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, "h3").text
                price = product.find_element(By.CSS_SELECTOR, "strong.price").text

                # Chèn dữ liệu vào MySQL
                sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
                cursor.execute(sql, (name, price))
                connection.commit()

                print(f"Đã lưu: {name} - {price}")
            except Exception as e:
                continue
finally:
    driver.quit()
    connection.close()
