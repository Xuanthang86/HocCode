#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import isqrt

def cong(a: float, b: float) -> float:
    """Trả về a + b"""
    return a + b

def tru(a: float, b: float) -> float:
    """Trả về a - b"""
    return a - b

def is_prime(n: int) -> bool:
    """
    Kiểm tra n có phải số nguyên tố không.
    - Chỉ đúng khi n là số nguyên.
    - Thuật toán kiểm tra tới sqrt(n), tối ưu 6k±1.
    """
    if not isinstance(n, int):
        raise TypeError("is_prime chỉ nhận số nguyên (int).")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # kiểm tra các số dạng 6k±1
    limit = isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def menu():
    print("=== CHƯƠNG TRÌNH TÍNH TOÁN & KIỂM TRA SỐ NGUYÊN TỐ ===")
    print("1) Cộng hai số")
    print("2) Trừ hai số")
    print("3) Kiểm tra số nguyên tố")
    print("0) Thoát")

def main():
    while True:
        menu()
        choice = input("Chọn chức năng (0-3): ").strip()
        if choice == "0":
            print("Tạm biệt!")
            break
        elif choice == "1":
            try:
                a = float(input("Nhập a: "))
                b = float(input("Nhập b: "))
                print(f"Kết quả: {a} + {b} = {cong(a, b)}\n")
            except ValueError:
                print("Lỗi: vui lòng nhập số hợp lệ.\n")
        elif choice == "2":
            try:
                a = float(input("Nhập a: "))
                b = float(input("Nhập b: "))
                print(f"Kết quả: {a} - {b} = {tru(a, b)}\n")
            except ValueError:
                print("Lỗi: vui lòng nhập số hợp lệ.\n")
        elif choice == "3":
            try:
                n_raw = input("Nhập số nguyên n: ").strip()
                # Cho phép nhập dạng số thực nhưng sẽ ép về int nếu không có phần thập phân
                if "." in n_raw:
                    raise ValueError("Vui lòng nhập đúng SỐ NGUYÊN.")
                n = int(n_raw)
                print(f"{n} là số nguyên tố." if is_prime(n) else f"{n} KHÔNG phải số nguyên tố.")
                print()
            except ValueError as e:
                print(f"Lỗi: {e}\n")

if __name__ == "__main__":
    main()