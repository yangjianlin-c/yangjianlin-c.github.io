


创建一个 Git 项目。

su git
cd ~
mkdir hugo.git
cd hugo.git
git init --bare

ssh -T git@mekesim.com:hugo.git

web目录 /var/www/html/mekesim.com/


cd hugo
wget https://github.com/gohugoio/hugo/releases/download/v0.30.1/hugo_0.30.1_Linux-64bit.tar.gz
tar -zxvf hugo_0.30.1_Linux-64bit.tar.gz
sudo mv hugo /usr/local/bin/hugo

git clone /home/git/hugo.git
chown -R git.git hugo
cd hugo
su git
hugo --theme=hugo_theme_robust


hugo new site hugo
chown -R git.git hugo
su git
cd hugo
git init
git remote add /home/git/hugo.git


创建 hook 任务让它把提交上来的文件复制到 Web 目录下。
/home/git/hugo.git/hooks/post-receive
将如下脚本复制进去：
#! /bin/bash -l
GIT_REPO=/home/git/hugo.git # Git 项目路径
PUBLIC_WWW=/var/www/html/mekesim.com/hugo   # Web 目录
cd $PUBLIC_WWW
git pull $GIT_REPO # 将提交上来的文件 pull 到web路径


git@git.mekesim.com:hugo.git

mklink /d "D:\hugo\content\" "C:\Users\q19439\Google Drive\Mekesim\hugo_content\"


chown -R git.git hugo


git fetch --all  
git reset --hard origin/master 
git pull