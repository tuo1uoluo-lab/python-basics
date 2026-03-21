keyword = "哈哈哈"

try:
    with open("input123.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    results = []
    for line in lines:
        if keyword in line:
            results.append(line)

    print(results)
    if len(results) == 0:
            print("没有找到包含关键词的行")
    else:
            with open("output.txt", "w", encoding="utf-8") as f:
                for line in results:
                    f.write(line)
            print("筛选完成，结果已写入 output.txt")
except FileNotFoundError:
    print("文件未找到，请检查路径")