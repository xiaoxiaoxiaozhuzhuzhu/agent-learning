from github_api import get_github_user

def route_task(task: str) -> str:
    task = task.lower()

    if task.startswith("github "):
        return "github"
    
    if "搜索" in task or "search" in task:
        return "search"

    if "计算" in task or "calculate" in task:
        return "calculate"
    
    return "chat"

def handle_task(task: str) -> str:
    route = route_task(task)

    if route == "github":
        username = task.replace("github ", "").strip()

        user = get_github_user(username)

        if "error" in user:
            return user["error"]

        return (
            f"用户名：{user.get('login')}\n"
            f"姓名：{user.get('name')}\n"
            f"简介：{user.get('bio')}\n"
            f"公开仓库：{user.get('public_repos')}\n"
            f"Followers：{user.get('followers')}"
        )
    
    elif route == "search":
        return f"准备调用搜索工具：{task}"
    
    elif route == "calculate":
        return f"准备调用计算工具：{task}"
    
    elif route == "chat":
        return f"准备调用聊天工具：{task}"
    
    return "无法处理的任务类型"













"""
if __name__ == "__main__":
    while True:
        user_input = input("你：")

        if user_input == "exit":
             break

        result = handle_task(user_input)

        print("agent:", result) 
"""