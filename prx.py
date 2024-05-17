import colorama
from colorama import Fore
import time
import random

def main():
    # رشته اعداد دودویی
    binary_string = ""
    
    # تعداد اعداد دودویی
    num_digits = 100
    
    # حلقه برای ایجاد اثر باران
    for _ in range(num_digits):
        # اضافه کردن یک عدد دودویی تصادفی به رشته
        binary_string = random.choice(['0', '1']) + binary_string
        
        # چاپ رشته با رنگ سبز
        print(Fore.GREEN + binary_string)
        
        # تاخیر برای ایجاد اثر باران
        time.sleep(0.1)  # افزایش تاخیر

if __name__ == "__main__":
    # اجرای اصلی
    colorama.init(autoreset=True)  # فعال کردن رنگ‌های colorama
    main()