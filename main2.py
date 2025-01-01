# 全域變數：用來存儲任務
pending_tasks = []   # 待完成的任務清單
completed_tasks = [] # 已完成的任務清單
# 新增任務
def add_task():
    title = input("請輸入任務名稱：").strip()
    if not title:
        print("任務名稱不可為空！")
        return
    
    description = input("請輸入任務描述（可選）：").strip()
    due_date = input("請輸入完成期限（格式: YYYY-MM-DD，可選）：").strip()

    # 建立新任務
    new_task = {
        "title": title,
        "description": description or None, # 這邊用 None 的話，後面 task['description'][:40] 會產生錯誤！
        "due_date": due_date or None,
    }
    pending_tasks.append(new_task)
    print(f"\n成功新增任務：{new_task['title']}\n")

# 顯示任務清單
def show_tasks():
    print("\n=== 任務清單 ===")
    print("未完成的任務：")
    if not pending_tasks:
        print("\n  目前沒有任何任務！\n")
    else:
        for idx, task in enumerate(pending_tasks, start=1):
            print(f"  {idx}. {task['title']} ({task['description'][:40]})") # 描述部份最多顯示 40 個字元
    
    print("\n已完成的任務：")
    if not completed_tasks:
        print("\n  目前沒有任何任務！\n")
    else:
        for idx, task in enumerate(completed_tasks, start=1):
            print(f"  {idx}. {task['title']} ({task['description'][:40]})") # 描述部份最多顯示 40 個字元
    print()

def main():
    while True:
        print("\n=== To-Do List 管理系統 ===")
        print("1. 顯示任務清單")
        print("2. 新增任務")
        print("3. 離開系統")
        
        choice = input("請選擇功能（輸入數字）：").strip()
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            print("感謝使用，再見！")
            break
        else:
            print("無效的選擇，請重新輸入。\n")

# 啟動主程式
main()