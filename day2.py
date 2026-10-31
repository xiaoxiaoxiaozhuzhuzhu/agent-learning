import json

"""
tools = [
    "search",
    "calculate",
    "weather",
]

for tool in tools:
    print(tool)
"""

"""
user = {
    "name": "Tom",
    "age": 22,
    "role": "student"
}

print(user["name"])
print(user["age"])
print(user["role"])
"""


json_text = """
{
    "name": "ResearchAgent",
    "tool": "search",
    "query": "LangGraph"
}"""

data = json.loads(json_text)

print(data)     # 'name': 'ResearchAgent', 'tool': 'search', 'query': 'LangGraph'}
print(type(data))   # <class 'dict'>
print(data["tool"])     # search
# 



task = {
    "tool": "search",
    "query": "Agent Memory"
}

json_test = json.dumps(task)

print(json_test)    # {"tool": "search", "query": "Agent Memory"}
print(type(json_test))      # <class 'str'>


# 中文为什么有时候变成 \uXXXX？
task2 = {
    "tool": "search",
    "query": "什么是智能体"
}

json_test2 = json.dumps(task2)

print(json_test2)    # {"tool": "search", "query": "\u4ec0\u4e48\u662f\u667a\u80fd\u4f53"}
print(type(json_test2))      # <class 'str'>
# 这不是乱码。
# 如果你希望直接显示中文：
print(
    json.dumps(
        task2,
        ensure_ascii=False,
        indent=2
    )
)
"""
{
  "tool": "search",
  "query": "什么是智能体"
}
"""
