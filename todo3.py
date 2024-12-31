def delete_task():
    print("\n=== 刪除任務 ===")
    show_tasks()

    task_type = input("請選擇任務類型（1: 未完成, 2: 已完成）：").strip()
    if task_type not in ["1", "2"]:
        print("\n無效的選擇！請輸入 1 或 2。\n")
        return

    task_list = pending_tasks if task_type == "1" else completed_tasks
    if not task_list:
        print("\n選擇的任務清單中沒有任務。\n")
        return

    try:
        task_idx = int(input("請輸入要刪除的任務編號：")) - 1
        if 0 <= task_idx < len(task_list):
            task = task_list.pop(task_idx)
            print(f"\n成功刪除任務：{task['title']}\n")
        else:
            print("\n無效的編號！請重新選擇。\n")
    except ValueError:
        print("\n輸入無效！請輸入數字。\n")