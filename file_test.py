try:
    with open("input123.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    count = len(lines)
    print("共有", count, "行")

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("共有" + str(count) + "行\n")

except FileNotFoundError:
    print("文件未找到，请检查路径")

finally:
    print("程序执行完毕")