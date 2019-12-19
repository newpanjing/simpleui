<p align="center">
  <a href="https://newpanjing.github.io/simpleui/">
    <img alt="Simpleui" src="https://github.com/newpanjing/simpleui/raw/master/images/logo.png" width="140">
  </a>
</p>
<p align="center">让Django Admin简单而友好</p>
<p align="center">
Simple and friendly.
Django admin theme the simpleui
</p>
<p align="center">
  <a href="https://github.com/newpanjing/simpleui/blob/master/LICENSE"><a href="https://opencollective.com/simpleui" alt="Financial Contributors on Open Collective"><img src="https://opencollective.com/simpleui/all/badge.svg?label=financial+contributors" /></a>
  <a href="https://github.com/newpanjing/simpleui/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://pypi.org/project/django-simpleui/#history"><img src="https://img.shields.io/pypi/v/django-simpleui.svg"></a>
<a href="https://python.org"><img src="https://img.shields.io/badge/python->=3.7.x-green.svg"></a>
<a href="https://pypi.org/project/django-simpleui/">
<img src="https://img.shields.io/pypi/dm/django-simpleui.svg">
</a>
</p>


---
<p align="center">
中文 | <a href="./doc/en/README_en.md">English</a>
</p>

---

<a href="https://www.88cto.com/admin/">
  <img alt="demo" src="https://github.com/newpanjing/simpleui/raw/master/images/%E4%B8%BB%E9%A1%B5.png" width="420" align="right" style="max-width: 50%">
</a>


simpleui 特点
-----
👍 内置28款流行的主题

⚡️ pip闪电安装100%兼容原生admin无需修改代码

✨ 多标签页面，各个模块更加清晰明了

🎯 配置简单，极速上手，在settings.py中加入simpleui后启动立即生效，效率提升 100%！让后端开发得心应手。

☕️ Element-UI + Vue 加持，让古老的django admin 焕然一新。

🦀 新增支持Django3.0，Python3.8、Python3.9，敢于做第一个吃螃蟹的人。

# 开发初衷
Django Admin默认界面设计语言存在着的一些不足，比如色彩单一，大量线条的使用，分割化明显。将这些不足归类一下就是界面单调、雷同性明显、缺少惊喜。我们认为新的平台类视觉风格可以打破这些束缚，尝试一些新的探索，启发传统的设计认知,因此结合当下设计趋势，构思了Element+Django Admin的Simpleui。让Django Admin和Element产生完美的交互。配以最流行的后台设计风格，让Django Admin更加强大。

## QQ群
+ QQ群号:786576510

<img src='https://github.com/newpanjing/simpleui/raw/master/images/QQ%E7%BE%A4.jpg' width='200'>


## 文档
文档详细的描述了安装使用方法，以及各种配置项的说明，请点击以下链接查阅。
 
 ### 重要的事情说3遍：

👇👇👇👇👇👇👇👇👇👇👇

👉 1.[simpleui文档教程使用说明](https://simpleui.88cto.com/docs/simpleui) 👈

👉 2.[simpleui文档教程使用说明](https://simpleui.88cto.com/docs/simpleui)👈

👉  3.[simpleui文档教程使用说明](https://simpleui.88cto.com/docs/simpleui)👈

👆👆👆👆👆👆👆👆👆👆👆



## 本地Demo下载
如果你没有任何python django基础，可以下载一个可以直接运行的demo进行体验。
[😝DEMO源码](https://github.com/newpanjing/simpleui_demo)

## 在线Demo
> 权限受限，只能查看模块的相关数据，不能操作。如果要体验全部功能，请在自己的系统安装simpleui查看效果。

+ 地址：[https://www.88cto.com/admin/](https://www.88cto.com/admin/)
+ 用户名：demo
+ 密码：demo123456

# simpleui 是什么？
🚀simpleui 是django admin的一个主题 是一个基于element-ui+vue开发，重写和优化90%以上的页面。 
与suit是同类产品。我们是一个更符合国人审美和使用习惯的一个主题。

# 开始使用
详细步骤请浏览 [使用文档](./QUICK.md)。 也可以参考[Demo](#在线Demo)

+ 安装
```python
pip install django-simpleui
```

用pip或者[源码方式](#克隆源码本地安装)安装simpleui后，在自己项目的settings.py文件中INSTALLED_APPS的第一行加入`simpleui`

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

如果不知道怎么配置或者如何使用，请下载[本地demo](#本地Demo下载)进行学习。或者加入QQ群：786576510 咨询。

# 升级simpleui
```python
pip install django-simpleui --upgrade
```

# 克隆源码本地安装
```shell
git clone https://github.com/newpanjing/simpleui
cd simpleui
python setup.py sdist install
```

## 常见问题:

1. 如果关闭debug模式后，请执行以下命令将simpleui静态文件静态文件克隆到根目录
    ```shell
    python3 manage.py collectstatic
    ```
2. 克隆静态文件出错
请在settings.py文件中加入：
    ```shell
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    ```
3. 其他问题请参考[django官方文档](https://docs.djangoproject.com/zh-hans/2.2/)。

4. i18n 国际化 采用js国际化，默认为英文和中文两种语言，随系统切换。具体请看[国际化配置](/i18n.md)

其他问题请查看[快速上手指南](./QUICK.md)

## 支持django和python版本
[查看支持的版本列表](/VERSION.md)


## 浏览器兼容性

![Chrome](https://raw.github.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png) | ![Firefox](https://raw.github.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png) | ![Edge](https://raw.github.com/alrra/browser-logos/master/src/edge/edge_48x48.png) | ![IE](https://raw.github.com/alrra/browser-logos/master/src/archive/internet-explorer_9-11/internet-explorer_9-11_48x48.png) | ![Safari](https://raw.github.com/alrra/browser-logos/master/src/safari/safari_48x48.png) | ![Opera](https://raw.github.com/alrra/browser-logos/master/src/opera/opera_48x48.png) | ![UC](https://raw.github.com/alrra/browser-logos/master/src/uc/uc_48x48.png)
:---: | :---: | :---: | :---: | :---: | :---: | :---:
 ✔ |  ✔ |  ✔ |  11+ ✔ |  ✔ |  ✔ | ✔

## README 徽章

如果你的项目正在使用Simpleui，可以将Simpleui徽章 [![ice](https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg)](https://github.com/newpanjing/simpleui) 添加到你的 README 中：

```
[![simpleui](https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg)](https://github.com/newpanjing/simpleui)
```


## 赞助💰
如果你觉得simpleui对你有帮助，你可以赞助我们一杯咖啡，鼓励我们继续开发维护下去。
![扫码赞助](https://github.com/newpanjing/simpleui/raw/master/images/pay.png)


# 登录页
![](https://github.com/newpanjing/simpleui/raw/master/images/%E6%95%B0%E6%8D%AE%E9%A1%B5.png)

# 主页
![](https://github.com/newpanjing/simpleui/raw/master/images/%E4%B8%BB%E9%A1%B5.png)

# 列表页
![](https://github.com/newpanjing/simpleui/raw/master/images/%E5%88%97%E8%A1%A8%E9%A1%B5.png)
![](https://github.com/newpanjing/simpleui/raw/master/images/%E6%95%B0%E6%8D%AE%E9%A1%B5.png)

# 切换主题
![](https://github.com/newpanjing/simpleui/raw/master/images/%E5%88%87%E6%8D%A2%E4%B8%BB%E9%A2%98.png)

# 密码修改
![](https://github.com/newpanjing/simpleui/raw/master/images/%E5%AF%86%E7%A0%81%E4%BF%AE%E6%94%B9.png)

# 编辑页
![](https://github.com/newpanjing/simpleui/raw/master/images/%E7%BC%96%E8%BE%91%E9%A1%B5.png)

# 设置字体大小
![](https://github.com/newpanjing/simpleui/raw/master/images/%E8%AE%BE%E7%BD%AE%E5%AD%97%E4%BD%93%E5%A4%A7%E5%B0%8F.png)

## 优质贡献者

simpleui的发展离不开以下优秀贡献者的支持。如果您想为simpleui贡献代码，请fork到自己仓库，然后发起合并请求，合并至dev分支。

|Github|贡献范围|
|------|------|
|[@zhangzhibo1014](https://github.com/zhangzhibo1014)|英文文档翻译|
|[@liaogx](https://github.com/liaogx)|bug修复|
|[@shouyong](https://github.com/shouyong)|bug修复|
|[@Roddy1219](https://github.com/Roddy1219)|bug修复|
|[@WalkerWang731](https://github.com/WalkerWang731)|优质代码贡献|

# 致谢
开发工具由[Jetbrains](https://www.jetbrains.com/)赞助的Pycharm