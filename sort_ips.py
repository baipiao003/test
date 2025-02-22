def sort_ips(input_file, output_file, format_str):
    try:
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
        print(f"Error processing {input_file}: {e}")


if __name__ == "__main__":
    # 处理 IPv4 文件
    sort_ips("4.txt", "ipv4.txt", "{}#移动{}")

    # 处理 IPv6 文件
    sort_ips("6.txt", "ipv6.txt", "[{}]#移动{}")
