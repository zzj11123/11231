import requests
import random
import time
import sched
import json
import smtplib

phone="18833050890"#蘑菇丁账号
password="Zzj20001121"#蘑菇丁密码
sec = 10  # 延迟签到的上限时间，单位为秒


 
loginUrl = "https://api.moguding.net:9000/session/user/v1/login"
saveUrl = "https://api.moguding.net:9000/attendence/clock/v2/save"
 
inc = random.randint(0,sec)
schedule = sched.scheduler(time.time, time.sleep)
 
def getToken():
    data = {
        "password": password,
        "loginType":"android",
        "uuid":"",
        "phone": phone
    }
    resp = postUrl(loginUrl,data=data, headers={"Content-Type": "application/json; charset=UTF-8",'User-Agent': 'Mozilla/5.0 (Linux; U; Android 10; zh-cn; MIX 3 Build/QKQ1.190828.002) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1'})
    return resp['data']['token']
 
def postUrl(url,headers,data):
    requests.urllib3.disable_warnings()
    resp = requests.post(url, headers=headers, data=json.dumps(data),verify=False)
    return resp.json()
 
def main():
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 10; zh-cn; MIX 3 Build/QKQ1.190828.002) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1',
        'roleKey': 'student',
        'Authorization': getToken(),
        'Content-Length': '262',
        'sign': '9c67dc2f5dc5518130f76475585bfb77',
    }
    data = {
        "country": "中国",
        "address": "中国河北省石家庄市鹿泉区铜冶镇",
        "province": "河北省",
        "city": "石家庄市",
        "description": "",
        "planId": "b5fd5ea43e3d0a77e3e3c09c39c97364",
        "type": "END",#START 上班 END 下班
        "device": "Android",
        "latitude": "37.995922",
        "longitude": "114.457112",
    }
    resp = postUrl(saveUrl,headers,data)
    print(resp)
    
print("%s秒后进行签到" % inc)
schedule.enter(inc, 0, main, ())
schedule.run()
from email.mime.text import MIMEText
msg_from='1405569511@qq.com'                                 
passwd='ekhtyikdqrapigge'                                   
msg_to='1444001121@qq.com'                                  

t0=time.time()   
subject="签到时间"+time.strftime('%Y-%m-%d %H:%M:%S',(time.localtime(time.time())))                               #主题     
content="蘑菇丁签到成功"
msg=MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except s.SMTPException.e:
    print ("发送失败")


