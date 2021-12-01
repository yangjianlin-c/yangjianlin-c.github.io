MKDocs 是一个基于 Python 写成的文档生成工具，我们可以借助 GitHub Action 来实现自动部署到 GitHub Pages 。

## 本地配置

首先，你需要先在本地创建一个文件夹，文件夹内包含以下内容：

```
│  mkdocs.yml
│
├─.github
│  └─workflows
│          main.yml
│
└─docs
    │  xxx.md
    │  index.md
```

`mkdocs.yml` 是mkdocs项目的配置文件，配置主题等等。

`/docs` 文件夹内放文章内容的markdown文件。

`main.yml` 配置github自动发布脚本。最简单的配置文件如下：

```yaml
name: ci 
on:
  push:
    branches: 
      - master
      #- main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - run: pip install mkdocs-material 
      - run: mkdocs gh-deploy --force
```

!!! note

    branches 的设置，因为github将默认分支名改为了main,请注意查看你的github项目默认分支名称是 master 还是 main.

## Github配置

首先在Github上创建一个项目，项目名称为你在github的用户名<username>，这样的话就可以通过<username>.github.io/ 打开网页了。

当然如果项目名称使用的是其他名称，则访问地址是<username>.github.io/<repository>

关于github page功能的详细使用可以参考[这里](https://pages.github.com/)。

将本地项目push到远程后将会自动执行mkdocs部署脚本。打开网页就可以看到更新了。