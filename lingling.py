import requests
import json
import csv
import sys
import argparse

site_api = '你的API KEY' #key
results_pwd = 'results.csv'



def parse_args():
    description = "you should add those parameter"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-t','--target',help = "111")
    args = parser.parse_args()
    return args

def run_site(page):
    global site_api,site_keyword
    postdata = {"title":"nfdw", "title_type":"site", "page":1, "pagesize":10, "zone_key_id":"你的API KEY"}
    headers = {'Content-Type':'application/json'}
    response = requests.post(url="https://0.zone/api/data/",timeout=5,headers=headers,data=json.dumps(postdata))
    try:
        rejson = json.loads(response.text)['data']
    except Exception as _:
        print("没更多结果，结束")
        sys.exit()
    return (rejson)



def main():
    ii = 0
    write_csv_title()
    while 1:
        ii =ii+1
        rejson = run_site(ii)
        for i in rejson:
            ip = i['ip']
            port = i['port']
            url = i['url']
            title = i['title']
            os = i['os']
            ping = i['ping']
            cms = i['cms']
            banner_os = i['banner_os']
            component = i['component']
            area = i['area']
            city = i['city']
            continent = i['continent']
            country = i['country']
            device_type = i['device_type']
            latitude = i['latitude']
            longitude = i['longitude']
            operator = i['operator']
            province = i['province']
            service = i['service']
            extra_info = i['extra_info']
            app_name = i['app_name']
            group = i['group']
            company = i['company']
            tags = i['tags']
            status_code = i['status_code']
            toplv_domain = i['toplv_domain']
            timestamp = i['timestamp']
            write_csv_b(ip,port,url,title,os,ping,cms,banner_os,component,area,city,continent,country,device_type,latitude,longitude,operator,province,service,extra_info,app_name,group,company,tags,status_code,toplv_domain,timestamp)


def write_csv_b(ip,port,url,title,os,ping,cms,banner_os,component,area,city,continent,country,device_type,latitude,longitude,operator,province,service,extra_info,app_name,group,company,tags,status_code,toplv_domain,timestamp):
    global results_pwd
    f = open(results_pwd, 'a+', encoding='gb18030', newline='')
    try:
        csv_writer = csv.writer(f)
        csv_writer.writerow([ip,port,url,title,os,ping,cms,banner_os,component,area,city,continent,country,device_type,latitude,longitude,operator,province,service,extra_info,app_name,group,company,tags,status_code,toplv_domain,timestamp])
        print("成功写入",url)
    finally:
        f.close()

def write_csv_title():
    global results_pwd
    f = open(results_pwd, 'a+', encoding='gb18030', newline='')
    try:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['ip','port','url','title','os','ping','cms','banner_os','component','area','city','continent','country','device_type','latitude','longitude','operator','province','service','extra_info','app_name','group','company','tags','status_code','toplv_domain','timestamp'])
        print("成功写入标题")
    finally:
        f.close()
args = parse_args()
site_keyword = args.target
main()
