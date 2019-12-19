<p align="center">
  <a href="https://newpanjing.github.io/simpleui/">
    <img alt="Simpleui" src="https://github.com/newpanjing/simpleui/raw/master/images/logo.png" width="140">
  </a>
</p>
<p align="center">Make Django Admin simple and firendly</p>
<p align="center">
Simple and friendly.
Django admin theme the simpleui
</p>
<p align="center">
   <a href="https://github.com/newpanjing/simpleui/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://pypi.org/project/django-simpleui/#history"><img src="https://img.shields.io/pypi/v/django-simpleui.svg"></a>
<a href="https://python.org"><img src="https://img.shields.io/badge/python->=3.7.x-green.svg"></a>
<a href="https://pypi.org/project/django-simpleui/">
<img src="https://img.shields.io/pypi/dm/django-simpleui.svg">
</a>
</p>

---
<p align="center">
<a href="../../README.md">中文</a> | English
</p>

---

<a href="https://www.88cto.com/admin/">
  <img alt="demo" src="https://github.com/newpanjing/simpleui/raw/master/images/%E4%B8%BB%E9%A1%B5.png" width="420" align="right" style="max-width: 50%">
</a>


simpleui Characteristics
-----
👍 Built in 28 popular themes

⚡️ pip lightning installation, 100% compatible with native, `admin` without modifying the code

✨ Multi-label pages, each module is more clear

🎯 Simple configuration, get started quickly, add `simpleui` in `settings.py` and start it immediately, the efficiency is increased by `100%!` Make back-end development handy.

☕️ `Element-UI` and `Vue` ，Let the `django admin` be better.

🦀 Add support for Django3.0 Python3.8, Python3.9, dares to do the first person to eat crab.

# Original intention of development
`Django Admin` default interface design language has some shortcomings, such as single color, the use of a large number of lines, and obvious segmentation. To classify these shortcomings is that the interface is monotonous, obvious similarity, and lack of surprises. We believe that the new platform-like visual style can break these constraints, try some new explorations, and inspire traditional design cognition, so combined with the current design trend, I have conceived `Element+Django Admin's` Simpleui. Let `Django Admin` and `Element` make the perfect interaction. With the most popular back-end design style, let `Django Admin` is even more powerful.

## QQ Group
+ QQ group : 786576510

<img src='https://github.com/newpanjing/simpleui/raw/master/images/QQ%E7%BE%A4.jpg' width='200'>


## Document
The document describes in detail how to use the installation, as well as a description of the various configuration items, please click on the link below.
 
 ### Important Things To Say Three Times：

👇👇👇👇👇👇👇👇👇👇👇

👉 1.[simpleui Document](https://simpleui.88cto.com/docs/simpleui/en/quick.html) 👈

👉 2.[simpleui Document](https://simpleui.88cto.com/docs/simpleui/en/quick.html)👈

👉  3.[simpleui Document](https://simpleui.88cto.com/docs/simpleui/en/quick.html)👈

👆👆👆👆👆👆👆👆👆👆👆



## Local Demo download
If you don't have any `python django` basics, you can download a `demo` that can be run directly.
[😝DEMO SourceCode](https://github.com/newpanjing/simpleui_demo)

## Online Demo
> Permission is limited, only the relevant data of the module can be viewed and cannot be operated. If you want to experience all the features, please install simpleui on your system to see the result.

+ Address：[https://www.88cto.com/admin/](https://www.88cto.com/admin/)
+ username：demo
+ password：demo123456

# What is simpleui？
🚀`simpleui` is django admin's theme. It is a page based on `element-ui` + `vue` development, rewriting and optimizing over `90%`. 
It is the same product as the suit. We are a theme that is more in line with the aesthetic and usage habits of Chinese people.

# Start
Detailed steps [Document](./QUICK_en.md). Also refer to [Demo](#Online%2dDemo)

+ Installation
```python
pip install django-simpleui
```

Use pip or [Clone Source](#Clone%2dsource%2dlocal%2dinstallation) after installing simpleui, and`simpleui` to the first line of `INSTALLED_APPS` in your project's `settings.py` file.

 For example🌰：
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

If you don't know how to configure or how to use it，please download [local demo](#Local%2dDemo%2ddownload) to learning. Or join the QQ group :  `786576510` consulting.

# Upgrade simpleui
```python
pip install django-simpleui --upgrade
```

# Clone source local installation
```shell
git clone https://github.com/newpanjing/simpleui
cd simpleui
python setup.py sdist install
```

## common problem:

1. If turn off debug mode, execute the following command to clone the simpleui static file to the root directory.
    ```shell
    python3 manage.py collectstatic
    ```
2. Clone static file error
Please add in the `settings.py` file：
    ```shell
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    ```
3. Please refer to other questions [django Documentation](https://docs.djangoproject.com/en/2.2/intro/tutorial01/).

4. i18n internationalization adopt js internationalization, the default is English and Chinese, switch with the system. Please see [International configuration](/i18n.md)

other questions [Quick start guide](./QUICK_en.md)

## Support for django and python versions
[List of Supported Versions](/VERSION.md)


## Browser Compatibility

![Chrome](https://raw.github.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png) | ![Firefox](https://raw.github.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png) | ![Edge](https://raw.github.com/alrra/browser-logos/master/src/edge/edge_48x48.png) | ![IE](https://raw.github.com/alrra/browser-logos/master/src/archive/internet-explorer_9-11/internet-explorer_9-11_48x48.png) | ![Safari](https://raw.github.com/alrra/browser-logos/master/src/safari/safari_48x48.png) | ![Opera](https://raw.github.com/alrra/browser-logos/master/src/opera/opera_48x48.png) | ![UC](https://raw.github.com/alrra/browser-logos/master/src/uc/uc_48x48.png)
:---: | :---: | :---: | :---: | :---: | :---: | :---:
 ✔ |  ✔ |  ✔ |  11+ ✔ |  ✔ |  ✔ | ✔

## **README** Badge

If your project is using Simpleui，you can put the Simpleui badge [![ice](https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg)](https://github.com/newpanjing/simpleui) add to your README：

```
[![simpleui](https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg)](https://github.com/newpanjing/simpleui)
```


## Sponsor💰
If you think that `simpleui` is helpful to you, you can sponsor us a cup of coffee and encourage us to continue to develop and maintain.
![sponsor us](https://github.com/newpanjing/simpleui/raw/master/images/pay.png)


# Login Page
![](https://github.com/newpanjing/simpleui/raw/master/images/%E6%95%B0%E6%8D%AE%E9%A1%B5.png)

# Home Page
![](https://github.com/newpanjing/simpleui/raw/master/images/%E4%B8%BB%E9%A1%B5.png)

# List Page
![](https://github.com/newpanjing/simpleui/raw/master/images/%E5%88%97%E8%A1%A8%E9%A1%B5.png)
![](https://github.com/newpanjing/simpleui/raw/master/images/%E6%95%B0%E6%8D%AE%E9%A1%B5.png)

# Switch Theme
![](https://github.com/newpanjing/simpleui/raw/master/images/%E5%88%87%E6%8D%A2%E4%B8%BB%E9%A2%98.png)

# Change Password
![](https://github.com/newpanjing/simpleui/raw/master/images/%E5%AF%86%E7%A0%81%E4%BF%AE%E6%94%B9.png)

# Edit Page
![](https://github.com/newpanjing/simpleui/raw/master/images/%E7%BC%96%E8%BE%91%E9%A1%B5.png)

# Set Font Size
![](https://github.com/newpanjing/simpleui/raw/master/images/%E8%AE%BE%E7%BD%AE%E5%AD%97%E4%BD%93%E5%A4%A7%E5%B0%8F.png)

## Great developer

The development of simpleui is supported by the following excellent contributors. If you want to contribute code to simpleui, fork to your repository and then make a merge request to the dev branch.

|Github|Scope|
|------|------|
|[@zhangzhibo1014](https://github.com/zhangzhibo1014)|Translate English document|
|[@liaogx](https://github.com/liaogx)|Bug fix|
|[@shouyong](https://github.com/shouyong)|Bug fix|
|[@Roddy1219](https://github.com/Roddy1219)|Bug fix|
|[@WalkerWang731](https://github.com/WalkerWang731)|Code contributions|
