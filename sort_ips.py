def sort_ips(input_file, output_file):
    try:
        # 根据文件名判断是IPv4还是IPv6
        if input_file.endswith("4.txt"):
            ip_type = "ip"
            format_str = "{}#移动{}"
        elif input_file.endswith("6.txt"):
            ip_type = "ip6"
            format_str = "[{}]#移动{}"
        else:
            raise ValueError("Unsupported file name. Use '4.txt' for IPv4 or '6.txt' for IPv6.")

        # 读取IP地址
        with open(input_file, 'r') as file:
            ips = file.readlines()

        # 去除空格和换行符，并排序
        ips = [ip.strip() for ip in ips if ip.strip()]
        ips.sort()

        # 写入新的文件，格式为 "ip#移动1" 或 "[ip]#移动1"，并添加序号
        with open(output_file, 'w') as file:
            for index, ip in enumerate(ips, start=1):
                file.write(format_str.format(ip, index) + "\n")

        print(f"IPs sorted and formatted successfully. Output saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import sys

    # 从命令行参数获取输入文件名
    if len(sys.argv) != 2:
        print("Usage: python sort_ips.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]  # 输入文件名
    output_file = "ipv4.txt" if input_file.endswith("4.txt") else "ipv6.txt"  # 输出文件名
    sort_ips(input_file, output_file)
