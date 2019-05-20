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
  + [如何下载这个模版](#如何下载这个模版)
  + [切换主题](#切换主题)
  + [图标说明](#图标说明)
# 进阶指南
  + [自定义主题](#自定义主题)
  + [修改首页图标](#修改默认图标)
  + [修改默认首页](#修改默认首页)
  + [修改LOGO](#修改LOGO)
  + [配置首页模块](#配置首页模块)
    + [服务器信息](#服务器信息)
    + [快速操作](#快速操作)
    + [最近动作](#最近动作)
  + [使用分析](#使用分析)
  + [菜单](#菜单)
    + [自定义菜单](#自定义菜单)
    + [默认图标](#默认图标)
    + [自定义图标](#自定义图标)

  + [修改模板](#修改模板)
  + [开发调试](#开发调试)
  + [源码安装到本地](#源码安装到本地)
  + [重写页面](#重写页面)
  + [头部添加自定义代码](#头部添加自定义代码)
  + [底部添加自定义代码](#底部添加自定义代码)

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

## 如何下载这个模版
目前暂时无法下载模板，不过我们计划推出simple-admin，纯html的模板，可以让更多语言使用。

## 切换主题
目前simpleui 内置28个流行样式风格的主题。后续随着版本的更新，会加入更多的主题。

## 图标说明
simpleui中显示的图标 可以参考[fontawesome](https://fontawesome.com/icons?d=gallery)的图标，只需要将完整的class名填入即可。


## 自定义主题
在自定义主题之前，请先把simpleui的静态资源克隆到根目录。然后找到theme
theme.js 就是用于配置主题列表

按该文件中的格式配置即可

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

在增加你的样式之前，请先了解less如何使用。

这是admin.lte.less的例子
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
他将会编译为admin.lte.css
需要安装less
```shell
npm install less -g

lessc admin.lte.less>admin.lte.css
```

## 修改默认图标
django内置的认证与授权以及关联的用户、组，都已经默认配置了一个图标。后续自定义的app将会是默认图标，需要自行在settings.py文件中进行配置
1. 

## 修改默认首页
simpleui内置了一个默认的首页，只是由简单的快捷导航与最近操作组成。

在自己项目的settings.py中加入：

+ 首页配置
> SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
+ 首页标题
> SIMPLEUI_HOME_TITLE = '百度一下你就知道'
+ 首页图标,支持element-ui和fontawesome的图标，参考https://fontawesome.com/icons图标
> SIMPLEUI_HOME_ICON = 'fa fa-user'

三项配置都是选填，不填都会有默认值。 [图标列表](https://fontawesome.com/icons)

## 修改LOGO
+ 自定义SIMPLEUI的Logo
> SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'

## 配置首页模块
首页默认展示3个模块，服务器信息、快速操作、最近动作，大家可以根据需要来显示或者隐藏某些模块。
### 服务器信息
隐藏：
> SIMPLEUI_HOME_INFO = False

显示：
> SIMPLEUI_HOME_INFO = True

### 快速操作

隐藏：
> SIMPLEUI_HOME_QUICK = False

显示：
> SIMPLEUI_HOME_QUICK = True

### 最近动作

隐藏：
> SIMPLEUI_HOME_ACTION = False

显示：
> SIMPLEUI_HOME_ACTION = True

## 使用分析
`默认开启，统计分析信息只是为了更好的帮助simpleui改进，并不会读取敏感信息。并且分析数据不会分享至任何第三方。`
> SIMPLEUI_ANALYSIS = False

|值|说明|
|--|--|
|True|收集分析，一天只上报一次分析数据。默认为True|
|False|不收集分析信息|

## 菜单

### 自定义菜单

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