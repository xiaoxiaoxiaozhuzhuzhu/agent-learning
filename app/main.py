from utils import format_message
from router import handle_task

def main():
    while True:
        user_input = input("你：")

        if user_input == "exit":
            print("Agent：再见")
            break

        result = handle_task(user_input)

        print("Agent：")
        print(result)


if __name__ == "__main__":
    main()