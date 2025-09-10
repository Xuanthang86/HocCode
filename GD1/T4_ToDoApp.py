import json
import os

FILENAME = "tasks.json"

# Đọc dữ liệu từ file (nếu có)
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Ghi dữ liệu ra file
def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

# Hiển thị menu
def menu():
    print("\n=== TO-DO APP ===")
    print("1. Thêm công việc")
    print("2. Hiển thị danh sách công việc")
    print("3. Đánh dấu hoàn thành")
    print("4. Sửa công việc")
    print("5. Xóa công việc")
    print("0. Thoát")

# Hiển thị danh sách công việc
def show_tasks(tasks):
    if not tasks:
        print("📌 Danh sách trống!")
        return
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    for i, task in enumerate(tasks, start=1):
        status = "✅ Hoàn thành" if task["done"] else "❌ Chưa xong"
        print(f"{i}. {task['title']} - {status}")

# Thêm công việc
def add_task(tasks):
    title = input("Nhập tên công việc: ").strip()
    if not title:
        print("⚠️ Công việc không được để trống!")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Đã thêm công việc!")

# Đánh dấu hoàn thành
def complete_task(tasks):
    show_tasks(tasks)
    if not tasks: return
    try:
        idx = int(input("Chọn số công việc cần đánh dấu hoàn thành: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks(tasks)
            print("✅ Đã cập nhật!")
        else:
            print("⚠️ Số không hợp lệ!")
    except ValueError:
        print("⚠️ Nhập số hợp lệ!")

# Sửa công việc
def edit_task(tasks):
    show_tasks(tasks)
    if not tasks: return
    try:
        idx = int(input("Chọn số công việc cần sửa: ")) - 1
        if 0 <= idx < len(tasks):
            new_title = input("Nhập tên mới: ").strip()
            if new_title:
                tasks[idx]["title"] = new_title
                save_tasks(tasks)
                print("✅ Đã sửa công việc!")
            else:
                print("⚠️ Tên mới không được để trống!")
        else:
            print("⚠️ Số không hợp lệ!")
    except ValueError:
        print("⚠️ Nhập số hợp lệ!")

# Xóa công việc
def delete_task(tasks):
    show_tasks(tasks)
    if not tasks: return
    try:
        idx = int(input("Chọn số công việc cần xóa: ")) - 1
        if 0 <= idx < len(tasks):
            deleted = tasks.pop(idx)
            save_tasks(tasks)
            print(f"🗑️ Đã xóa: {deleted['title']}")
        else:
            print("⚠️ Số không hợp lệ!")
    except ValueError:
        print("⚠️ Nhập số hợp lệ!")

# Chương trình chính
def main():
    tasks = load_tasks()
    while True:
        menu()
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "0":
            print("👋 Tạm biệt!")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
    