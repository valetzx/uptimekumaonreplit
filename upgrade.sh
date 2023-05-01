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

# 确认是否升级
echo "The latest version is: ${latest_version}"
echo "Do you want to upgrade to the latest version? (y/n)"
read -r confirm

case "$confirm" in
  [yY])
    git fetch --all
    git checkout "${latest_version}" --force

    npm install --production
    npm run download-dist

    pm2 restart uptime-kuma

    echo "Upgrade to version ${latest_version} successfully!"
    ;;
  [nN])
    echo "Upgrade cancelled."
    ;;
  *)
    echo "Invalid input. Upgrade cancelled."
    ;;
esac