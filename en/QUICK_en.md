simpleui Quick Start Guide
-----
Many people will misunderstand simpleui. They think after downloading and installing simpleui, they can be used directly after startup. But simpleui is majorization on the basis of the Django. Do, please [Create a Django project](#Create%2da%2dDjango%2dProject) using the Command Line or IDE, Then [Modify the default template for simpleui](#Modify%2ddefault%2dtemplate%2dfor%2dsimpleui).

Before starting，please take a minte to understand settings.py, because it's especially important in the next process.

# Start Guide
  + [Create a Django project](#Create%2da%2dDjango%2dProject)
  + [Modify default template for simpleui](#Modify%2ddefault%2dtemplate%2dfor%2dsimpleui)
  + [Clone static file to the root](#Clone%2dstatic%2dfile%2dto%2dthe%2droot)
  + [Startup Project](#Startup%2dProject)
  + [How to download simpleui's template](#How%2dto%2ddownload%2dsimpleui's%2dtemplate)
  + [Switch Theme](#Switch%2dTheme)
  + [About Icons](#About%2dIcons)
# Advance Guide
  + [Customize Theme](#Customize%2dTheme)
  + [Modify Default Icon](#Modify%2dDefault%2dIcon)
  + [Modify Default Home](#Modify%2dDefault%2dHome)
  + [Modify Home Jump Address](#Modify%2dHome%2dJump%2dAddress)
  + [Modify LOGO](#Modify%2dLOGO)
  + [Config Home Module](#Config%2dHome%2dModule)
    + [Server Information](#Server%2dInformation)
    + [Quick Operation](#Quick%2dOperation)
    + [Recent Action](#Recent%2dAction)
  + [Use Analysis](#Use%2dAnalysis)
  + [Menu](#Menu)
    + [Customize Munu](#Customize%2dMunu)
    + [Default Icon](#Default%2dIcon)
    + [Customize Icon](#自定义图标)

  + [Modify Templates](#修改模板)
  + [Develop And Debug](#开发调试)
  + [Source Code install to local](#源码安装到本地)
  + [ReWrit Page](#重写页面)
  + [Custom code to Header](#头部添加自定义代码)
  + [Custom code to Footer](#底部添加自定义代码)

# Common Problems
  + [settings.py](#settingspy-找不到)
  + [python version problem](#python版本问题)
  + [Unable to Start](#无法启动)
  + [Style Normal Loading But Display Abnormal](#样式正常加载显示不正常)

---

## Create a Django Project

Django Documentation[https://docs.djangoproject.com/en/2.2/intro/tutorial01/](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

## Modify default template for simpleui  

  We only need to add a line of simpleui in the settings.py of the project.

  For example 🌰：
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
  If Debug=False,static resources will be inaccessible，please go to[Clone static file to the root](#Clone static file to the root)

## Clone static file to the root
Django have a mode is DEBUG, it's in settings.py. Default DEBUG = True.
```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```
If DEBUG = Fasle, there are two ways to solve the situation that static resources can't be accessed.
1. Modify settings.py , add following content:
```python
 STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "static"),
 ]
```
2. Clone static resources to the static directory of the project，Then processed by nginx.
```shell
    python3 manage.py collectstatic
```
If the clone error message indicates that the static directory could't be found，please open the settings.py and assign a static directory
```python
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
```

## Startup Project
After successfully adding simpleui in settings.py，Run command：
```shell
    python manage.py runserver 8000
```
Open browser, input：http://127.0.0.1:8000/admin
if you find that the login page if different from before，Congratulations! You have successfully installed simpleui！Let's start enjoying simpleui!

## How to download simpleui's template
Currently unable to download templates，but we plan to launch simple-admin's html templates，can make more languages available.

## Switch Theme
Currently simpleui has 28 popular style themes. We will update more topics as the version is updated.

## About Icons
The icon displayed in simpleui can refer to the [fontawesome](https://fontawesome.com/icons?d=gallery) icon，just fill in the full class name.


## Customize Theme
Before customizing the theme, please clone the static resources of simpleui to the root directory. Then you need to find theme.js, it's used to configure the list of topics.

Please configure in this format.

```javascript
var SimpleuiThemes = [
    {
        "text": "Default"
    },
    {
        "text": "Simpleui-x",
        "file": "simpleui.css"
    },
    .....
]
```

Before adding your style, please understand how less to used.

Example for admin.lte.less
```css
@import "base";

@primary: #2096c8 !important;
@color: white;

@menu-color: #8aa4af !important;
@menu-background: #2b3539 !important;

@menu-color-hover: #FFF;
@menu-background-hover: #1f272b;

@menu-title-color: #FFF;
@menu-title-background-color: #212c32;

@menu-title-color-hover: #FFF;
@menu-title-background-color-hover: #1f272b;


@navbar-color: #fff;
@navbar-background: #3c8dbc;
```
it will compile to admin.lte.css.
you need to install less
```shell
npm install less -g

lessc admin.lte.less>admin.lte.css
```

## Modify Default Icon
Django's built-in authentication and authorization and associated users and groups have been configured with an icon by default. Custom app will be the default icons and need to be configured in the settings.py file.

## Modify Default Home
simpleui has a default home page, which consists of quick navigation and recent operations.

You can modify the default home page and add it to your project's settings.py：

+ Home configuration
> SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
+ Home title
> SIMPLEUI_HOME_TITLE = '百度一下你就知道'
+ Home Icon,support element-ui's and fontawesome's icon，reference https://fontawesome.com/icons
> SIMPLEUI_HOME_ICON = 'fa fa-user'

The above three configurations are optional. If you don't fill, there will be default values. [icon list](https://fontawesome.com/icons)

## Modify Home Jump Address
The top of the home page has a default jump address of /, this is root directory. If you need to customize, add some settings in your project's settings.py.

```python
# Configure simpleui Click the address of the home icon to jump.
SIMPLEUI_INDEX = 'https://www.88cto.com'
```

Relative and absolute paths can be set. There is nothing special about this address, it will call window.open to open the address directly.


## Modify LOGO
+ Customize SIMPLEUI's Logo
> SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'

## Config Home Module
The home page displays three modules by default, server information,quick operation and recent actions. You can show or hide some modules as needed.
### Server Information
Hide：
> SIMPLEUI_HOME_INFO = False

Display：
> SIMPLEUI_HOME_INFO = True

### Quick Operation

Hide：
> SIMPLEUI_HOME_QUICK = False

Display：
> SIMPLEUI_HOME_QUICK = True

### Recent Action

Hide：
> SIMPLEUI_HOME_ACTION = False

Display：
> SIMPLEUI_HOME_ACTION = True

## Use Analysis
`Default is True, statistical analysis information is only used to better help simpleui improvements, and doesn't read sensitive information. And the analysis data will not be shared with any third party.`
> SIMPLEUI_ANALYSIS = False

|Value|Description|
|--|--|
|True|Collect and analyze,report only one analysis data a day。Default is True|
|False|Don't collect and analyze|

## Menu

### Customize Munu

#### system_keep 保留系统菜单
该字段用于告诉simpleui，是否需要保留系统默认的菜单，默认为False，不保留。
如果改为True，自定义和系统菜单将会并存

#### menus说明

|字段|说明|
|---|---|
|name|菜单名|
|icon|图标，参考element-ui和fontawesome图标|
|url|链接地址，绝对或者相对,如果存在models字段，将忽略url|
|models|子菜单|

#### 例子
```python
SIMPLEUI_CONFIG = {
    'system_keep':False,
    'menus': [{
        'name': 'Simpleui',
        'icon': 'fas fa-code',
        'url': 'https://gitee.com/tompeppa/simpleui'
    }, {
        'app': 'auth',
        'name': '权限认证',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    }, {
        'name': '测试',
        'icon': 'fa fa-file',
        'models': [{
            'name': 'Baidu',
            'url': 'http://baidu.com',
            'icon': 'far fa-surprise'
        }, {
            'name': '内网穿透',
            'url': 'https://www.wezoz.com',
            'icon': 'fab fa-github'
        }]
    }]
}
```

如果SIMPLEUI_CONFIG中存在menus字段，将会覆盖系统默认菜单。并且menus中输出的菜单不会受权限控制。

### 默认图标
simpleui对所有菜单提供了一个默认的file图标，是为了统一风格。也许你并不喜欢，你可以选择关闭默认图标

>SIMPLEUI_DEFAULT_ICON = False

|值|说明|
|--|--|
|True|开启默认图标，默认为True|
|False|关闭默认图标|

### 自定义图标
simpleui仅为系统默认模块提供了图标，如果要为其他模块指定图标，可以自定义配置。图标参考请查阅：[图标说明](#图标说明)

优先级：
自定义->系统配图->默认图标

>注：simpleui 原则上不涉及代码，所以采用setting方式。后续可考虑扩展Model的 Meta class 进行配置图标

|字段|说明|
|---|---|
|name|模块名字，请注意不是model的命名，而是菜单栏上显示的文本，因为model是可以重复的，会导致无法区分|
|icon|图标|
例子：
```
SIMPLEUI_ICON = {
    '系统管理': 'fab fa-apple',
    '员工管理': 'fas fa-user-tie'
}

```

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

## 重写页面

例如重写首页，在templates目录中新建admin文件夹，然后添加index.html
如果选择继承方式，就只能采用block
代码如下：
```html
    {% extends 'admin/index.html' %}
    {% load static %}

    {%block head}
        {{ block.super }}
        ..此处写你的代码
    {% endblock %}

    {% block script %}
        {{ block.super }}
        ..此处写你的代码
    {% endblock %}
```

如果是想全部重写：

```html
<html>
    <head>
        <title>完全自定义</title>
    </head>
    <body>
        这里你是自定义的html代码
    </body>
</html>
```
##  头部添加自定义代码
```html
    {% extends 'admin/index.html' %}
    {% load static %}

    {%block head}
        {{ block.super }}
        ..此处写你的代码
    {% endblock %}
```
##  底部添加自定义代码
```html
    {% extends 'admin/index.html' %}
    {% load static %}

    {% block script %}
        {{ block.super }}
        ..此处写你的代码
    {% endblock %}
```
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

>其他更多问题，请提交[issues](https://github.com/newpanjing/simpleui/issues)给我们。