#此脚本为手动更新，请关闭程序后使用！

git fetch --all
git checkout 1.15.0 --force

npm ci --production
npm run download-dist
#更新完成后点 绿色run 运行。
