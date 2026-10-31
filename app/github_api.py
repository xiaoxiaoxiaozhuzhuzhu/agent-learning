import requests

def get_github_user(username: str) -> dict:
    """
    获取GitHub用户信息

    :param username: GitHub用户名
    :return: 用户信息字典
    """
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(
            url,
            timeout=10  # 设置超时时间为10秒
            )

        response.raise_for_status() # 如果响应状态码不是200，会抛出HTTPError异常

        return response.json()  # 将返回的JSON数据转换为Python字典

    except requests.exceptions.Timeout:
        return {"error": "请求超时，请稍后再试。"}

    except requests.exceptions.ConnectionError:
        return {"error": "网络连接错误，请检查您的网络连接。"}

    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP错误: {http_err}"}

    except requests.exceptions.RequestException as err:
        return {"error": f"请求异常: {err}"}


















'''
def simplify_user(data: dict) -> dict:
    return {
        "username": data.get("login"),
        "name": data.get("name"),
        "bio": data.get("bio"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following")
    }        

def main():
    # username = input("请输入GitHub用户名：")
    # user_info = get_github_user(username)

    raw_user = get_github_user(
        "xiaoxiaoxiaozhuzhuzhu"
        )
    
    if not raw_user:
        print("获取用户信息失败")
        return

    user = simplify_user(raw_user)

    print(user)

if __name__ == "__main__":
    main()
'''


""" test
import requests

url = "https://api.github.com/users/xiaoxiaoxiaozhuzhuzhu"

response = requests.get(url)

data = response.json()  # 将返回的JSON数据转换为Python字典

# print(response.status_code)  # 200
# print(response.text)  # 返回的JSON数据

print(type(data))  # <class 'dict'>
print(data["login"])  # xiaoxiaoxiaozhuzhuzhu
print(data["public_repos"])  # 1
"""