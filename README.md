# uptime-kuma on Replit
在replit自建uptime-kuma监控
https://github.com/louislam/uptime-kuma/wiki/

Rplit个人版：

<a href="https://repl.it/github/valetzx/uptimekumaonreplit">
  <img alt="Run on Repl.it" src="https://repl.it/badge/github/valetzx/uptimekumaonreplit" style="height: 40px; width: 190px;" />
</a>

Rplit教育版：

将以下代码粘贴至Replit Shell后回车

`git clone https://github.com/valetzx/uptimekumaonreplit && mv -b uptimekumaonreplit/* ./ && mv -b uptimekumaonreplit/.[^.]* ./ && rm -rf *~ && rm -rf uptimekumaonreplit`

当加载完 Loading Nix environment... 后点击绿色 ▶ Run

新增 `main.py` 部署企业微信通知

新增 `pushbullet.js` 企业微信配置

新增 `update.sh` 手动更新 

更新以后的版本 可以把 `git checkout 1.15.1 --force` 1.15.1 改成想更新的版本

Replit有点拉，似乎会回档，会导致数据库很多对不上。= 。随便用用吧20220430
