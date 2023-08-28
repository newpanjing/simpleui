# 快速上手指南
-----
有很多同学会误解simpleui，认为下载、安装simpleui后，启动就可以直接使用。但是simpleui是在django的基础上进行优化的，所以请先自行用命令行、IDE[创建一个django项目](#创建一个django项目)，然后[修改默认后台模板为simpleui](#修改默认后台模板为simpleui)

在开始入门之前，请花1分钟了解下[settings.py](#settingspy-找不到)文件，
它在接下来的过程中尤为重要。

## 目录

[[toc]]

---

## pip源切换

pip默认的源服务器在国外，安装速度较慢，推荐使用国内的源。

### 源列表
- 豆瓣：http://pypi.douban.com/simple/
- 中科大：https://pypi.mirrors.ustc.edu.cn/simple/
- 清华：https://pypi.tuna.tsinghua.edu.cn/simple

### 一次性使用
可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple

例如：

```shell
pip install django-simpleui -i https://pypi.tuna.tsinghua.edu.cn/simple
```
### 永久修改

#### Linux & MacOS
linux下，修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url 为国内镜像地址，内容如下：

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

#### Windows
windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
---


## 安装

### pip安装

```shell
pip3 install django-simpleui
```

### 源码安装
+ 克隆源码本地安装
```shell
git clone https://github.com/newpanjing/simpleui
cd simpleui
python setup.py sdist install
```
后续步骤请参考[修改默认后台模板为simpleui](#修改默认后台模板为simpleui)

### 创建一个django项目

django官方中文教程[https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/](https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/)

如果您已经有存在的项目，可以忽略这一步。

### 修改默认后台模板为simpleui

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

### 克隆静态文件

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

### 启动项目
在settings.py中成功加入simpleui后，运行命令：
```shell
    python manage.py runserver 8000
```
浏览器中输入：http://127.0.0.1:8000/admin
如果发现登录页和之前有所不同，那么就可以恭喜你，成功安装simpleui！接下来开始享受simpleui吧。

## 主题

### 默认主题

默认主题在settings.py中进行配置

```python
# 指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取
SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'
```


### 切换主题
目前simpleui 内置28个流行样式风格的主题。后续随着版本的更新，会加入更多的主题。

### 主题列表

> 取对应的file即可设置成默认主题

```javascript
var SimpleuiThemes = [
    {
        text: "Default",
        menu: 'rgb(48, 65, 86)',
        logo: 'rgb(48, 65, 86)',
        top: '#FFF'
    },
    {
        text: "Simpleui-x",
        menu: '#2c2e39',
        logo: '#2c2e39',
        top: '#FFF',
        file: "simpleui.css"
    },
    {
        text: "Element-UI",
        file: "element.css",
        top: '#447eff',
        menu: '#FFf',
        logo: '#FFF'
    },
    {
        text: "layui",
        file: "layui.css",
        menu: '#393D49',
        logo: '#23262E',
        top: '#23262E'
    }, {
        text: "Ant Design Pro",
        file: "ant.design.css",
        menu: '#000b16',
        logo: '#002140',
        top: '#FFF'
    }, {
        text: "Admin LTE",
        file: "admin.lte.css",
        top: '#3c8dbc',
        logo: '#3c8dbc',
        menu: '#2b3539'
    }, {
        text: "Highdmin",
        file: "highdmin.css",
        top: '#02c0ce',
        menu: '#e0e0e0',
        logo: '#02c0ce'
    }, {
        text: "Aircraft",
        file: "aircraft.css",
        top: '-webkit-gradient(linear, left bottom, left top, color-stop(0, #4d5b76), color-stop(1, #6f80a1)) !important',
        menu: '#e0e0e0',
        logo: '-webkit-gradient(linear, left bottom, left top, color-stop(0, #4d5b76), color-stop(1, #6f80a1)) !important'
    }, {
        text: "Purple",
        file: "purple.css",
        top: '#FFF',
        logo: '#FFF',
        menu: '#3e4295'
    }, {
        text: "Gray",
        file: "gray.css",
        top: '#213a53',
        logo: '#213a53',
        menu: '#e0e0e0'
    },
    {
        text: "Dark green",
        file: "dark.green.css",
        top: '#f3f3f4',
        menu: '#283846',
        logo: '#283846'
    },
    {
        text: "Orange",
        file: "orange.css",
        top: 'linear-gradient(to right bottom, #da8342, #e45131)',
        logo: 'linear-gradient(to right bottom, #da8342, #e45131)',
        menu: '#FFF'
    },
    {
        text: "Black",
        file: "black.css",
        top: "#333",
        logo: "#333",
        menu: '#FFF'
    },
    {
        text: "Green",
        file: "green.css",
        top: '#19a97b',
        logo: '#FFF',
        menu: '#FFF'
    },
    {
        text: "Light",
        file: "light.css",
        top: "#ebf1f5",
        logo: "#ebf1f5",
        menu: "#ebf1f5"
    }, {
        text: 'Enterprise blue',
        file: 'e-blue.css',
        top: '#3ba1df',
        logo: '#3ba1df',
        menu: '#FFF'
    }, {
        text: 'Enterprise blue pro',
        file: 'e-blue-pro.css',
        top: '#3ba1df',
        logo: '#3ba1df',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise green',
        file: 'e-green.css',
        top: '#27ad60',
        logo: '#27ad60',
        menu: '#FFF'
    }, {
        text: 'Enterprise green pro',
        file: 'e-green-pro.css',
        top: '#27ad60',
        logo: '#27ad60',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise red',
        file: 'e-red.css',
        top: '#c9333e',
        logo: '#c9333e',
        menu: '#FFF'
    }, {
        text: 'Enterprise red pro',
        file: 'e-red-pro.css',
        top: '#c9333e',
        logo: '#c9333e',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise purple',
        file: 'e-purple.css',
        top: '#8263b1',
        logo: '#8263b1',
        menu: '#FFF'
    }, {
        text: 'Enterprise purple pro',
        file: 'e-purple-pro.css',
        top: '#8263b1',
        logo: '#8263b1',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise black',
        file: 'e-black.css',
        top: '#1f2c39',
        logo: '#1f2c39',
        menu: '#FFF'
    }, {
        text: 'Enterprise black pro',
        file: 'e-black-pro.css',
        top: '#1f2c39',
        logo: '#1f2c39',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'x-green',
        file: 'x-green.css',
        top: '#2F9688',
        logo: '#2F9688',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'x-red',
        file: 'x-red.css',
        top: '#AA3130',
        logo: 'rgb(38, 50, 56)',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'x-blue',
        file: 'x-blue.css',
        top: '#FFF',
        logo: '#1E9FFF',
        menu: 'rgb(38, 50, 56)'
    }
]
```

### 自定义主题
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


## 图标

### 说明
simpleui中显示的图标 可以参考[fontawesome](https://fontawesome.com/icons?d=gallery)的图标，只需要将完整的class名填入即可。


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


## 菜单

### 自定义菜单

### system_keep 保留系统菜单
该字段用于告诉simpleui，是否需要保留系统默认的菜单，默认为False，不保留。
如果改为True，自定义和系统菜单将会并存

### menu_display 过滤显示菜单和排序功能
该字段用于告诉simpleui，是否需要开启过滤显示菜单和排序功能。<br>
默认可以不用填写，缺省配置为默认排序，不对菜单进行过滤和排序。<br>
开启认为传一个列表，如果列表为空，则什么也不显示。列表中的每个元素要对应到menus里面的name字段

### dynamic 开启动态菜单功能
该字段用于告诉simpleui，是否需要开启动态菜单功能。<br>
默认可以不用填写，缺省配置为False，不开启动态菜单功能。<br>
开启为True，开启后，每次用户登陆都会刷新左侧菜单配置。<br>
需要注意的是：开启后每次访问admin都会重读配置文件，所以会带来额外的消耗。

### menus说明  (2021.2已加入3级菜单)

|字段|说明|
|---|---|
|name|菜单名|
|icon|图标，参考element-ui和fontawesome图标|
|url|链接地址，绝对或者相对,如果存在models字段，将忽略url|
|models|子菜单，自2021.02.01+版本 支持最多3级菜单，使用方法可以看下方例子|
|newTab|boolean,default:False,浏览器新标签中打开，自2022.6.13开始支持|

### 例子

```python
import time
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['Simpleui', '测试', '权限认证', '动态菜单测试'],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [{
        'name': 'Simpleui',
        'icon': 'fas fa-code',
        'url': 'https://gitee.com/tompeppa/simpleui',
        # 浏览器新标签中打开
        'newTab': True,
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
        # 自2021.02.01+ 支持多级菜单，models 为子菜单名
        'name': '多级菜单测试',
        'icon': 'fa fa-file',
      	# 二级菜单
        'models': [{
            'name': 'Baidu',
            'icon': 'far fa-surprise',
            # 第三级菜单 ，
            'models': [
                {
                  'name': '爱奇艺',
                  'url': 'https://www.iqiyi.com/dianshiju/'
                  # 第四级就不支持了，element只支持了3级
                }, {
                    'name': '百度问答',
                    'icon': 'far fa-surprise',
                    'url': 'https://zhidao.baidu.com/'
                }
            ]
        }, {
            'name': '内网穿透',
            'url': 'https://www.wezoz.com',
            'icon': 'fab fa-github'
        }]
    }, {
        'name': '动态菜单测试' ,
        'icon': 'fa fa-desktop',
        'models': [{
            'name': time.time(),
            'url': 'http://baidu.com',
            'icon': 'far fa-surprise'
        }]
    }]
}
```

如果SIMPLEUI_CONFIG中存在menus字段，将会覆盖系统默认菜单。并且menus中输出的菜单不会受权限控制。

## 模板

### 修改模板
在simpleui的基础上修改模板需要对django有一定了解
1. 先把simpleui克隆到静态目录下，参考[克隆静态文件到根目录](#克隆静态文件到根目录)
2. 找到静态目录下的admin目录，里面就是simpleui的模板，直接修改相关html页面即可生效。


### 重写页面

例如重写首页，在templates目录中新建admin文件夹，然后添加index.html
如果选择继承方式，就只能采用block
代码如下：

```html
    {% extends 'admin/index.html' %}
    {% load static %}

    {% block head %}
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
####  头部添加自定义代码
```html
    {% extends 'admin/index.html' %}
    {% load static %}

    {% block head %}
        {{ block.super }}
        ..此处写你的代码
    {% endblock %}
```
####  底部添加自定义代码
```html
    {% extends 'admin/index.html' %}
    {% load static %}

    {% block script %}
        {{ block.super }}
        ..此处写你的代码
    {% endblock %}
```


## 自定义按钮&Action

### 介绍
> 需要在2.1.2以上版本生效

django admin 默认提供了自定义按钮的支持，但是样式、图标均不可自定义，simpleui在django admin 自定义action的基础上增加了样式、图标、按钮类型自定义。

### 例子
```python
    @admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'idCard', 'phone', 'birthday', 'department', 'enable', 'create_time')
   
    # 增加自定义按钮
    actions = ['make_copy', 'custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    def make_copy(self, request, queryset):
        pass
    make_copy.short_description = '复制员工'
```
该配置与原生admin兼容。

### 字段参数

|字段|说明|
|------|------|
|icon|按钮图标，参考https://element.eleme.cn/#/zh-CN/component/icon与https://fontawesome.com，把class 复制进来即可|
|type|按钮类型，参考：https://element.eleme.cn/#/zh-CN/component/button|
|style|自定义css样式|
|confirm|弹出确认框，在3.4或以上版本中生效|

### confirm 例子

```python
    def message_test(self, request, queryset):
        messages.add_message(request, messages.SUCCESS, '操作成功123123123123')
        
    # 给按钮增加确认
    message_test.confirm = '你是否执意要点击这个按钮？'
```



### 链接按钮

> 在2.9或以上版本中生效

|字段|说明|
|------|------|
|action_type|按钮动作类型，0=当前页内打开，1=新tab打开，2=浏览器tab打开|
|action_url|按钮访问链接|

demo：
```python
  # 增加自定义按钮
    actions = ['custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    # 链接按钮，设置之后直接访问该链接
    # 3中打开方式
    # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 设置了action_type，不设置url，页面内将报错
    # 设置成链接类型的按钮后，custom_button方法将不会执行。

    custom_button.action_type = 0
    custom_button.action_url = 'http://www.baidu.com'

```

### layer对话框按钮

> 在2021.1.0及以上版本中生效

对话框按钮是在admin中进行配置action，可以自定义输入的字段，然后通过ajax请求到action中进行业务的处理。

需要继承`AjaxAdmin` 在`from simpleui.admin import AjaxAdmin`包中

`simplepro`也会同步支持对话框按钮功能。

#### 效果
<img src="/images/layer.png" alt="layer">

#### 字段说明

下列字段是指`action`的`layer`属性

|字段|说明|
|--|--|
|title|对话框标题|
|tips|对话框提示|
|confirm_button|确认按钮文本|
|cancel_button|取消按钮文本|
|width|对话框宽度，百分比，例如：50%|
|labelWidth|表格的label宽度，例如：80px|
|params|对话框表格中的字段，array|

##### params字段

|字段|说明|
|--|--|
|type|类型，取值为：input原生属性，和elementui的：select、date、datetime、rate、color、slider、switch、input_number、checkbox、radio|
|key|参数名，post参数中获取的名称|
|value|默认值，数组或文本|
|label|字段在表格中显示的名称|
|size|组件的大小，取值为：medium / small / mini|
|require|是否必选，取值为：True/False|
|width|输入框宽度，例如：200px|
|options|选项，数组，type为select、checkbox、radio的时候可用|

#### options字段
|字段|说明|
|--|--|
|key|值|
|label|显示文本|


#### 例子

```python
class RecordAdmin(ImportExportActionModelAdmin, AjaxAdmin):
    resource_class = ProxyResource

    list_display = ('id', 'name', 'type', 'money', 'create_date')
    list_per_page = 10

    actions = ('layer_input',)

    def layer_input(self, request, queryset):
        # 这里的queryset 会有数据过滤，只包含选中的数据

        post = request.POST
        # 这里获取到数据后，可以做些业务处理
        # post中的_action 是方法名
        # post中 _selected 是选中的数据，逗号分割
        if not post.get('_selected'):
            return JsonResponse(data={
                'status': 'error',
                'msg': '请先选中数据！'
            })
        else:
            return JsonResponse(data={
                'status': 'success',
                'msg': '处理成功！'
            })

    layer_input.short_description = '弹出对话框输入'
    layer_input.type = 'success'
    layer_input.icon = 'el-icon-s-promotion'

    # 指定一个输入参数，应该是一个数组

    # 指定为弹出层，这个参数最关键
    layer_input.layer = {
        # 弹出层中的输入框配置

        # 这里指定对话框的标题
        'title': '弹出层输入框',
        # 提示信息
        'tips': '这个弹出对话框是需要在admin中进行定义，数据新增编辑等功能，需要自己来实现。',
        # 确认按钮显示文本
        'confirm_button': '确认提交',
        # 取消按钮显示文本
        'cancel_button': '取消',

        # 弹出层对话框的宽度，默认50%
        'width': '40%',

        # 表单中 label的宽度，对应element-ui的 label-width，默认80px
        'labelWidth': "80px",
        'params': [{
            # 这里的type 对应el-input的原生input属性，默认为input
            'type': 'input',
            # key 对应post参数中的key
            'key': 'name',
            # 显示的文本
            'label': '名称',
            # 为空校验，默认为False
            'require': True
        }, {
            'type': 'select',
            'key': 'type',
            'label': '类型',
            'width': '200px',
            # size对应elementui的size，取值为：medium / small / mini
            'size': 'small',
            # value字段可以指定默认值
            'value': '0',
            'options': [{
                'key': '0',
                'label': '收入'
            }, {
                'key': '1',
                'label': '支出'
            }]
        }, {
            'type': 'number',
            'key': 'money',
            'label': '金额',
            # 设置默认值
            'value': 1000
        }, {
            'type': 'date',
            'key': 'date',
            'label': '日期',
        }, {
            'type': 'datetime',
            'key': 'datetime',
            'label': '时间',
        }, {
            'type': 'rate',
            'key': 'star',
            'label': '评价等级'
        }, {
            'type': 'color',
            'key': 'color',
            'label': '颜色'
        }, {
            'type': 'slider',
            'key': 'slider',
            'label': '滑块'
        }, {
            'type': 'switch',
            'key': 'switch',
            'label': 'switch开关'
        }, {
            'type': 'input_number',
            'key': 'input_number',
            'label': 'input number'
        }, {
            'type': 'checkbox',
            'key': 'checkbox',
            # 必须指定默认值
            'value': [],
            'label': '复选框',
            'options': [{
                'key': '0',
                'label': '收入'
            }, {
                'key': '1',
                'label': '支出'
            }, {
                'key': '2',
                'label': '收益'
            }]
        }, {
            'type': 'radio',
            'key': 'radio',
            'label': '单选框',
            'options': [{
                'key': '0',
                'label': '收入'
            }, {
                'key': '1',
                'label': '支出'
            }, {
                'key': '2',
                'label': '收益'
            }]
        }]
    }


```

#### action 返回结果

```json
{
    'status': 'error',
    'msg': '请先选中数据！'
}
```

> status = success/error

> msg = 自定义

#### 对话框按钮说明

1. 如果需要作为增加和编辑 需要自己实现业务逻辑，编辑的时候将数据填充到value字段即可。

2. 限制选中后才能提交数据，可以在后台进行限制

3. 2020.1.0 及以上版本生效，需要继承`AjaxAdmin` 在`from simpleui.admin import AjaxAdmin`包中。 不继承提交数据会500或者404
   例如：

```python

 if not post.get('_selected'):
            return JsonResponse(data={
                'status': 'error',
                'msg': '请先选中数据！'
            })

```

### layer 文件上传

> 自2021.4.2+版本开始，支持layer中上传文件

例子：

```python

@admin.register(Layer)
class LayerAdmin(AjaxAdmin):
    actions = ('upload_file',)

    def upload_file(self, request, queryset):
        # 这里的upload 就是和params中配置的key一样
        upload= request.FILES['upload']
        print(upload)
        pass

    upload_file.short_description = '文件上传对话框'
    upload_file.type = 'success'
    upload_file.icon = 'el-icon-upload'
    upload_file.enable = True

    upload_file.layer = {
        'params': [{
            'type': 'file',
            'key': 'upload',
            'label': '文件'
        }]
    }

```



## 配置

simpleui在django 原生admin的基础上增加了若干自定义的配置，这些配置均是在`settings.py`文件中完成。

### 关闭登录页粒子动画
在项目的settings.py中加入
```python
SIMPLEUI_LOGIN_PARTICLES = False
```
粒子动画默认开启


### 修改默认图标
django内置的认证与授权以及关联的用户、组，都已经默认配置了一个图标。后续自定义的app将会是默认图标，需要自行在settings.py文件中进行配置
1.

### 首页-修改默认
simpleui内置了一个默认的首页，只是由简单的快捷导航与最近操作组成。

在自己项目的settings.py中加入：

+ 首页配置
> SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
+ 首页标题
> SIMPLEUI_HOME_TITLE = '百度一下你就知道'
+ 首页图标,支持element-ui和fontawesome的图标，参考https://fontawesome.com/icons图标
> SIMPLEUI_HOME_ICON = 'fa fa-user'

三项配置都是选填，不填都会有默认值。 [图标列表](https://fontawesome.com/icons)

### 首页-跳转地址
首页顶部首页图标默认跳转地址为/，即根目录。如果需要自定义，请在项目的settings.py中加入设置：

```python
# 设置simpleui 点击首页图标跳转的地址
SIMPLEUI_INDEX = 'https://www.88cto.com'
```

可以设置相对与绝对路径。该地址并无特殊之处，将会调用window.open直接打开该地址。
### 首页-模块
首页默认展示3个模块，服务器信息、快速操作、最近动作，大家可以根据需要来显示或者隐藏某些模块。

### 修改LOGO
+ 自定义SIMPLEUI的Logo
> SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'


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

### 使用分析
`默认开启，统计分析信息只是为了更好的帮助simpleui改进，并不会读取敏感信息。并且分析数据不会分享至任何第三方。`
> SIMPLEUI_ANALYSIS = False

|值|说明|
|--|--|
|True|收集分析，一天只上报一次分析数据。默认为True|
|False|不收集分析信息|

### 离线模式
> 在2.1.3或以上的版本中生效
在settings.py中加入
```python
SIMPLEUI_STATIC_OFFLINE = True
```
指定simpleui 是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目

不填该项或者为False的时候，默认从第三方的cdn获取
### 关闭Loading遮罩层
> 在2.1.5或以上的版本中生效

在settings.py中加入
```python
SIMPLEUI_LOADING = False
```
True或None 默认显示加载遮罩层，指定为False 不显示遮罩层。默认显示

## 插件支持

### django-import-export
simpleui对数据导入导出插件也做了支持，您可以直接安装使用。

### admindoc
admindoc需要simpleui 3.3+ 版本

### simplepro

simplepro也是我们推出的一个升级版的django admin插件，在现有的基础上，做了大量改进和优化。并且一前后分离的方式加载数据。

点击[了解更多](https://simpleui.88cto.com/simplepro)。

## 国际化

simpleui 国际化采用js前端国际化，因为没有涉及到后端，所以没有django标准的国际化文件。

将simpleui 克隆到静态目录，然后添加需要的语言

语言命名与django LANGUAGE_CODE 一致

例如：
中文简体：zh-hans
英文：en-us

将文件命名为: [code].js
+ zh-hans.js
+ en-us.js

## 常见问题
### settings.py 找不到

    这个文件是在自己创建的django项目中，不是在simpleui中。如果你熟悉django就会明白，如果不熟悉请先学习django。[django中文文档](https://docs.djangoproject.com/zh-hans/2.2/)

### python版本问题

    + 该项目推荐使用python3，python2.x可能会不兼容
    + 使用源码安装时如果出错，请指定python版本，python3 和 pip3
### 无法启动
可能由于某些未知的问题，导致项目无法启动，请不要放弃simpleui，你可以提[issue](https://github.com/newpanjing/simpleui/issues)，或者直接加入QQ群：873469913，我们将协助解决。

### 样式正常加载显示不正常
在win8 系统中 可能会遇到，css以及其他文件全部正常加载，但是显示不正常。这是因为响应头为application/x-css，而不是text/css，造成浏览器不正常解析。
#### 解决办法：
1.运行cmd： 输入regedit 并回车

2.在注册表HKEY_CLASSES_ROOT中找到.css 点击.css文件夹  修改Content Type 为 text/css

参考连接：[https://blog.csdn.net/sun754276603/article/details/46989965](https://blog.csdn.net/sun754276603/article/details/46989965)

### 如何下载这个模版
目前暂时无法下载模板，不过我们计划推出simple-admin，纯html的模板，可以让更多语言使用。

### 反馈建议
>其他更多问题，请提交[issues](https://github.com/newpanjing/simpleui/issues)给我们。


### 开发调试
如果想在simpleui的基础上进行一些修改，可以参考以下步骤
1. 安装simpleui到项目中
2. 找到simpleui的目录，然后删除
3. 克隆simpleui源码到本地
4. Linux、Unix、macOS环境下用软连接的方式，把项目依赖包中的simpleui目录指定到源码的simpleui目录
    ```shell
    ln -s 源文件 目标文件
    ```
5. windows环境下请右键创建快捷方式

接下来就可以修改、发布simpleui了。如有疑问请加入QQ群：873469913

### 官网&反馈

[https://simpleui.88cto.com](https://simpleui.88cto.com)
