django admin simpleui
-----
django admin 美化主题，采用layui 作为基本框架，改写大部分页面

## 说明
+ 安装
```python
pip install django-simpleui
```
+ 升级
```python
pip install django-simpleui --upgrade
```
+ 克隆源码本地安装
```shell
git clone https://github.com/newpanjing/simpleui
cd simpleui
python setup.py sdist install
```
+ 项目 settings.py 的INSTALLED_APPS 第一行加入
> `simpleui`
+ i18n 50%支持

+ 建议启动之前把静态文件克隆到根目录，然后用nginx处理静态文件
```python
python3 manage.py collectstatic
```

## 自动配图标功能
+ 自动配图标功能采用jieba分词插件对菜单项进行分词，然后在simpletags.py中进行匹配
+ 建议自己开个一个菜单管理模块，不然目前这种方式需要非常完善的词库才能较好的支持。

## 采用 simpleui的网站
1. [贝塔博客](https://www.88cto.com)
2. [奇客网](https://www.qikenet.com)
3. [WeNat](https://www.wezoz.com)
4. [72WO](https://www.72wo.com)
5. [12APM](https://www.12apm.com)

## 美化页面
 + 登录页
 + 主页
 + 列表页
 + 编辑页
 + 历史
 
## 更新日志

### version 1.4

+ 由于django无法自定义图标，所以采用猜测的方式来给菜单显示图标
+ 修复select下拉框bug
+ 修复错误提示不显示bug
+ 图标使用最新版layui 2.4.4
+ 导入jieba分词，用于猜测图标

## version 1.4.1
+ 取消日志输出

## version 1.4.2
+ 修复布尔类型下拉框无法显示bug

## version 1.4.3
+ 修正登录页面标题显示

## version 1.4.4
+ 修复pip 安装失败bug
    > 部分用户设置的pip，是Python2的版本，导致安装失败
+ 去掉首页代码库标识     

## v1.4版预览图

![img](https://github.com/newpanjing/simpleui/raw/master/images/图片1.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片2.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片3.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片4.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片5.png)

> 改版本的图标猜测功能可能不大完善，大家可以提issue 来完善。
