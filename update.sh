#此脚本为手动更新，请关闭程序后使用！
cd uptime-kuma
git fetch --all
git checkout 1.15.0 --force
#在replit shell中输入 sh update.sh 回车 以更新
npm ci --production
npm run download-dist
#更新完成后点 绿色run 运行！
