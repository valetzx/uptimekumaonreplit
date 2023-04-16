#!/bin/bash

# 切换到uptime-kuma目录
cd uptime-kuma

# 获取最新稳定版本号非beta版
current_version=$(git describe --tags)
latest_version=$(git tag -l --sort=v:refname | grep -v "beta" | tail -n1)

if [ "${current_version}" == "${latest_version}" ]; then
  echo "The current version is already the latest: ${latest_version}"
  exit 0
fi

# 切换到最新版本
git fetch --all
git checkout "${latest_version}" --force

# 安装生产所需依赖并下载构建后的代码
npm install --production
npm run download-dist

# 启动程序
pm2 restart uptime-kuma

echo "Upgrade to version ${latest_version} successfully!"
