const NotificationProvider = require("./notification-provider");
const axios = require("axios");
var qs = require('qs');

const { DOWN, UP } = require("../../src/util");

class Pushbullet extends NotificationProvider {

    name = "pushbullet";

    async send(notification, msg, monitorJSON = null, heartbeatJSON = null) {
        let okMsg = "Sent Successfully.";
        try {
            let pushbulletUrl = "你的站点域名！示例：https://xxxx.repl.co";
            let config = {
                headers: {
                    "Content-Type": "application/json"
                }
            };
            if (heartbeatJSON == null) {
                let testdata = {
                    "type": "note",
                    "title": "Uptime Kuma Alert",
                    "body": "Testing Successful.",
                }
                // 提交 构造from表单
                var access_token_data = qs.stringify(testdata);
                var _config = {
                  method: 'post',
                  url: pushbulletUrl,
                  headers: { 
                    'Content-Type': 'application/x-www-form-urlencoded'
                  },
                  data : access_token_data
                };
                await axios(_config)
            } else if (heartbeatJSON["status"] == DOWN) {
                let downdata = {
                    "type": "note",
                    "title": "UptimeKuma Alert: " + monitorJSON["name"],
                    "body": "[🔴 Down] " + heartbeatJSON["msg"] + "\nTime (UTC): " + heartbeatJSON["time"],
                }
                // 提交 构造from表单
                var access_token_data = qs.stringify(downdata);
                var _config = {
                  method: 'post',
                  url: pushbulletUrl,
                  headers: { 
                    'Content-Type': 'application/x-www-form-urlencoded'
                  },
                  data : access_token_data
                };
                await axios(_config)
            } else if (heartbeatJSON["status"] == UP) {
                let updata = {
                    "type": "note",
                    "title": "UptimeKuma Alert: " + monitorJSON["name"],
                    "body": "[✅ Up] " + heartbeatJSON["msg"] + "\nTime (UTC): " + heartbeatJSON["time"],
                }
                // 提交 构造from表单
                var access_token_data = qs.stringify(updata);
                var _config = {
                  method: 'post',
                  url: pushbulletUrl,
                  headers: { 
                    'Content-Type': 'application/x-www-form-urlencoded'
                  },
                  data : access_token_data
                };
                await axios(_config)
            }
            return okMsg;
        } catch (error) {
            this.throwGeneralAxiosError(error)
        }
    }
}

module.exports = Pushbullet;
