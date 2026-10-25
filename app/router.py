def route_task(task: str) -> str:
    task = task.lower()

    if "搜索" in task or "search" in task:
        return "search"

    if "计算" in task or "calculate" in task:
        return "calculate"
    
    return "chat"

def handle_task(task: str) -> str:
    route = route_task(task)

    if route == "search":
        return f"准备调用搜索工具：{task}"
    elif route == "calculate":
        return f"准备调用计算工具：{task}"
    elif route == "chat":
        return f"准备调用聊天工具：{task}"
    else:
        return "无法处理的任务类型"

if __name__ == "__main__":
    while True:
        user_input = input("你：")

        if user_input == "exit":
             break

        result = handle_task(user_input)

        print("agent:", result) 