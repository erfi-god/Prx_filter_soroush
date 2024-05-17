import os
import random

def main():
    # تعداد اعداد دودویی
    num_digits = 100000
    
    # حلقه برای ایجاد اثر باران
    for _ in range(num_digits):
        # ایجاد یک عدد دودویی تصادفی
        binary_digit = random.choice(['0', '1'])
        
        # چاپ عدد دودویی با رنگ سبز
        print(f"\033[32m{binary_digit}", end='', flush=True)  # کد ANSI برای رنگ سبز

    # پاک کردن خروجی ترمینال
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # اجرای اصلی
    main()
