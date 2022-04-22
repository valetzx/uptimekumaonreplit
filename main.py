#这个文件需要新建一个Python仓库并将这个文件放入Python仓库运行！
#在Python仓库中点绿色run之前 在shell中执行 `pip install python-multipart`
import base64
import json
import requests
import uvicorn
from fastapi import FastAPI, Form

#如何注册企业微信请看：https://github.com/riba2534/wecomchan
wecom_cid = "引号中填企业微信id"
wecom_aid = "引号中填企业微信应用id"
wecom_secret = "引号中填企业微信应用秘钥secret"
app = FastAPI()


def send_to_wecom(text, wecom_touid='@all'):
    global wecom_cid, wecom_aid, wecom_secret
    get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wecom_cid}&corpsecret={wecom_secret}"
    response = requests.get(get_token_url).content
    access_token = json.loads(response).get('access_token')
    if access_token and len(access_token) > 0:
        send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
        data = {
            "touser": wecom_touid,
            "agentid": wecom_aid,
            "msgtype": "text",
            "text": {
                "content": text
            },
            "duplicate_check_interval": 600
        }
        response = requests.post(send_msg_url, data=json.dumps(data)).content
        return response
    else:
        return False


def send_to_wecom_image(base64_content, wecom_touid='@all'):
    global wecom_cid, wecom_aid, wecom_secret
    get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wecom_cid}&corpsecret={wecom_secret}"
    response = requests.get(get_token_url).content
    access_token = json.loads(response).get('access_token')
    if access_token and len(access_token) > 0:
        upload_url = f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={access_token}&type=image'
        upload_response = requests.post(upload_url, files={
            "picture": base64.b64decode(base64_content)
        }).json()
        if "media_id" in upload_response:
            media_id = upload_response['media_id']
        else:
            return False

        send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
        data = {
            "touser": wecom_touid,
            "agentid": wecom_aid,
            "msgtype": "image",
            "image": {
                "media_id": media_id
            },
            "duplicate_check_interval": 600
        }
        response = requests.post(send_msg_url, data=json.dumps(data)).content
        return response
    else:
        return False


def send_to_wecom_markdown(text, wecom_touid='@all'):
    global wecom_cid, wecom_aid, wecom_secret
    get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wecom_cid}&corpsecret={wecom_secret}"
    response = requests.get(get_token_url).content
    access_token = json.loads(response).get('access_token')
    if access_token and len(access_token) > 0:
        send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
        data = {
            "touser": wecom_touid,
            "agentid": wecom_aid,
            "msgtype": "markdown",
            "markdown": {
                "content": text
            },
            "duplicate_check_interval": 600
        }
        response = requests.post(send_msg_url, data=json.dumps(data)).content
        return response
    else:
        return False


@app.post("/")
def main(type: str = Form(...), title: str = Form(...), body: str = Form(...), wecom_touid='@all'):
    if type == 'note':
        data = send_to_wecom(title + '\n' + body, wecom_touid)
    elif type == 'image':
        data = send_to_wecom_image(body, wecom_touid)
    elif type == 'markdown':
        data = send_to_wecom_markdown(title + '\n' + body, wecom_touid)
    else:
        data = send_to_wecom(title + '\n' + body, wecom_touid)
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, log_level="info")
