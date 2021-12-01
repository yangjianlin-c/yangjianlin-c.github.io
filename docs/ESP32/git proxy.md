---
title: Github Desktop 设置代理
---

## 第一种方式编辑 `.gitconfig` 文件

To directly add a proxy to Github Desktop without using git shell:

1. Set up/Sign in to your account in Github Desktop(This won't be a problem, proxy only doesn't allow you to Add, create or clone repo)
2. Close Github Desktop for the time being(to set up proxy).
3. Go to `C:\Users\@yourusername`.
4. There you will find a file named .gitconfig
5. Open it with any text editor(I have used sublime text 3) and add

`[http]     proxy = http://username:password@your.proxy.address:8080`

and save.

1. Now you can add, create and clone repos in Github Desktop.

## 第二种方式通过git 命令修改

安装github desktop，会同时安装git，路径如下

C:\Users\xxx\AppData\Local\GitHubDesktop\app-1.2.6\resources\app\git\cmd

在此目录下打开CMD界面

 ```
git config --global http.proxy proxy_address:proxy_port
git config --global https.proxy proxy_address:proxy_port
 ```