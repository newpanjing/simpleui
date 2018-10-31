django admin simpleui
-----
django admin 美化，采用layui 作为基本框架，改写大部分页面

+ 安装
> pip install django-simpleui
+ 或者克隆源码本地安装
> python setup.py sdist install
+ 项目 settings.py 的INSTALLED_APPS 第一行加入
> `simpleui`

# 美化页面
----
 + 登录页
 + 主页
 + 列表页
 + 编辑页
 + 历史
 
# 效果图

## 主页
![主页](https://github.com/newpanjing/simpleui/raw/master/images/主页.png)
## 列表页
![列表](https://github.com/newpanjing/simpleui/raw/master/images/列表页.png)
## 登录页
![登录页](https://github.com/newpanjing/simpleui/raw/master/images/登录页.png)
 

# 更新日志
## version 1.4
1. 由于django无法自定义图标，所以采用猜测的方式来给菜单显示图标
2. 修复select下拉框bug
3. 修复错误提示不显示bug
4. 图标使用最新版layui 2.4.4
5. 导入jieba分词，用于猜测图标


# v1.4版预览图

![img](https://github.com/newpanjing/simpleui/raw/master/images/图片1.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片2.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片3.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片4.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片5.png)

> 改版本的图标猜测功能可能不大完善，大家可以提issue 来完善。