simpleui 快速上手指南
-----
有很多同学会误解simpleui，认为下载、安装simpleui后，启动就可以直接使用。但是simpleui是在django的基础上进行优化的，所以请先自行用命令行、IDE[创建一个django项目](#创建一个django项目)，然后[修改默认后台模板为simpleui](#修改默认后台模板为simpleui)

在开始入门之前，请花1分钟了解下[settings.py](#settingspy-找不到)文件，
它在接下来的过程中尤为重要。

# 入门指引
  + [创建一个django项目](#创建一个django项目)
  + [修改默认后台模板为simpleui](#修改默认后台模板为simpleui)
  + [克隆静态文件到根目录](#克隆静态文件到根目录)
  + [启动项目查看效果](#启动项目查看效果)
# 进阶指南
  + [修改默认图标](#修改默认图标)
  + [修改默认首页](#修改默认首页)
  + [修改模板](#修改模板)
  + [开发调试](#开发调试)
  + [源码安装到本地](#源码安装到本地)

# 常见问题
  + [settings.py](#settingspy-找不到)
  + [python版本问题](#python版本问题)
  + [无法启动](#无法启动)
  + [样式正常加载显示不正常](#样式正常加载显示不正常)

---

## 创建一个django项目

django官方中文教程[https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/](https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/)

## 修改默认后台模板为simpleui  

  我们只需要在项目中的settings.py文件中加入一行simpleui即可。

  举个例子🌰：
  ```python
    # Application definition

    INSTALLED_APPS = [
        'simpleui',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ...
    ]
  ```
  如果关闭debug模式后,会出现静态资源无法访问，请查看[克隆静态文件到根目录](#克隆静态文件到根目录)

## 克隆静态文件到根目录
熟悉django的同学会了解，django有个神奇的模式叫做debug模式，默认是开启的，在settings.py中
```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```
关闭后可以有两种办法解决静态资源无法访问的情况
1. 在settings.py中加入：
```python
 STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "static"),
 ]
```
2. 克隆静态资源到项目的静态目录，然后交由nginx处理
```shell
    python3 manage.py collectstatic
```
如果克隆报错提示找不到静态目录，请先在settings.py指定静态目录
```python
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
```

## 启动项目查看效果
在settings.py中成功加入simpleui后，运行命令：
```shell
    python manage.py runserver 8000
```
浏览器中输入：http://127.0.0.1:8000/admin
如果发现登录页和之前有所不同，那么就可以恭喜你，成功安装simpleui！接下来开始享受simpleui吧。

## 修改默认图标
django内置的认证与授权以及关联的用户、组，都已经默认配置了一个图标。后续自定义的app将会是默认图标，需要自行在settings.py文件中进行配置
1. 

## 修改默认首页
simpleui内置了一个默认的首页，只是由简单的快捷导航与最近操作组成。

在自己项目的settings.py中加入：
```python
# 首页配置
SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
# 首页标题
SIMPLEUI_HOME_TITLE = '百度一下你就知道'
# 首页图标
SIMPLEUI_HOME_ICON = 'layui-icon-rate'
```
三项配置都是选填，不填都会有默认值。 [图标列表](./ICON.md)

## 修改模板
在simpleui的基础上修改模板需要对django有一定了解
1. 先把simpleui克隆到静态目录下，参考[克隆静态文件到根目录](#克隆静态文件到根目录)
2. 找到静态目录下的admin目录，里面就是simpleui的模板，直接修改相关html页面即可生效。

## 开发调试
如果想在simpleui的基础上进行一些修改，可以参考以下步骤
1. 安装simpleui到项目中
2. 找到simpleui的目录，然后删除
3. 克隆simpleui源码到本地
4. Linux、Unix、macOS环境下用软连接的方式，把项目依赖包中的simpleui目录指定到源码的simpleui目录
    ```shell
    ln -s 源文件 目标文件
    ```
5. windows环境下请右键创建快捷方式

接下来就可以修改、发布simpleui了。如有疑问请加入QQ群：786576510
## 源码安装到本地
+ 克隆源码本地安装
```shell
git clone https://github.com/newpanjing/simpleui
cd simpleui
python setup.py sdist install
```
后续步骤请参考[修改默认后台模板为simpleui](#修改默认后台模板为simpleui)

## 常见问题
  ### settings.py 找不到

    这个文件是在自己创建的django项目中，不是在simpleui中。如果你熟悉django就会明白，如果不熟悉请先学习django。[django中文文档](https://docs.djangoproject.com/zh-hans/2.2/)

  ### python版本问题

    + 该项目推荐使用python3，python2.x可能会不兼容
    + 使用源码安装时如果出错，请指定python版本，python3 和 pip3
  ### 无法启动
  可能由于某些未知的问题，导致项目无法启动，请不要放弃simpleui，你可以提[issue](https://github.com/newpanjing/simpleui/issues)，或者直接加入QQ群：786576510，我们将协助解决。
  
  ### 样式正常加载显示不正常
  在win8 系统中 可能会遇到，css以及其他文件全部正常加载，但是显示不正常。这是因为响应头为application/x-css，而不是text/css，造成浏览器不正常解析。
  #### 解决办法：
1.运行cmd： 输入regedit 并回车
    
2.在注册表HKEY_CLASSES_ROOT中找到.css 点击.css文件夹  修改Content Type 为 text/css

参考连接：[https://blog.csdn.net/sun754276603/article/details/46989965](https://blog.csdn.net/sun754276603/article/details/46989965)