# 生产xshell的session
## 原因
#### 一直使用xshell作为登录现网机器的工具,但是随了每次接维一批机器就要建立一批session实在是很繁琐,而且换一台win机器又要重新建立session,这里主要的问题就是session中password加密的方法会根据每台机器用户和SID进行.所以产生写个脚本来批量产生session.
## 安装(需要是win系统,如果是unix或者linux,需要注释win32模块,而且需要手工提取加密的key:win系统的用户名+SID)
### 1. 构建虚拟环境(可选)
#### &ensp;&ensp;开发者用户推荐，使用pyenv和virtualenv构建纯净的python环境，推荐python版本2.7.10
```Bash
pyenv virtualenv 2.7.10 xshell
pyenv activate xshell
```
### 2.拉取当前版本
```Bash
git clone http://github.com/eggnice/xshellsessions.git
cd xshellsessions
```
### 3.安装依赖(因为pycrypt在win系统中安装需要编译比较麻烦,建议直接上网下载编译好的软件进行安装)
```Bash
pip install -r requirements.txt
```

