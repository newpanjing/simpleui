<p align="center">
  <a href="https://newpanjing.github.io/simpleui/">
    <img alt="Simpleui" src="https://github.com/newpanjing/simpleui/raw/2.0/images/simpleui-logo.png" width="140">
  </a>
</p>
<p align="center">让Django Admin简单而友好</p>
<p align="center">
Simple and friendly.
Django admin theme the simpleui
</p>
<p align="center">
  <a href="https://github.com/996icu/996.ICU/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-Anti%20996-blue.svg"></a>
  <a href="https://github.com/alibaba/ice"><img src="https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg"></a>
  <a href="https://pypi.org/project/django-simpleui/#history"><img src="https://img.shields.io/pypi/v/django-simpleui.svg"></a>
</p>

---

<a href="https://alibaba.github.io/ice/iceworks">
  <img alt="飞冰" src="https://github.com/newpanjing/simpleui/raw/master/images/图片1.png" width="420" align="right" style="max-width: 50%">
</a>


simpleui
-----

✨ 官方与社区共同维护；持续更新，满足日常开发之所需。

⚡️ 多标签页面，各个模块更加清晰明了。配以最流行的后台设计风格，让Django Admin更加强大。

🎯 配置简单，极速上手，在settings.py中加入simpleui后启动立即生效，效率提升 100%！让后端开发得心应手。

☕️ Element，一套为开发者、设计师和产品经理准备的基于 Vue 2.0 的桌面端组件库。

🎨 Django Admin默认界面设计语言存在着的一些不足，比如色彩单一，大量线条的使用，分割化明显。将这些不足归类一下就是界面单调、雷同性明显、缺少惊喜。我们认为新的平台类视觉风格可以打破这些束缚，尝试一些新的探索，启发传统的设计认知,因此结合当下设计趋势，构思了Element+Django Admin的Simpleui。让Django Admin和Element产生完美的交互。

# 开始使用
用pip或者源码方式安装simpleui后，在自己项目的settings.py文件中INSTALLED_APPS的第一行加入`simpleui`

详细步骤请浏览 [快速上手指南](#)。

# 在线Demo
> 权限受限，只能查看模块的相关数据，不能操作。如果要体验全部功能，请在自己的系统安装simpleui查看效果。

+ 地址：[https://www.88cto.com/admin/](https://www.88cto.com/admin/)
+ 用户名：demo
+ 密码：demo123456

## QQ群
+ QQ群号:786576510

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
## 修改首页
本主题提供了一个默认的首页，由于不同业务的需求，需要定制首页可以按照如下操作进行

在自己项目的settings.py中加入：

```python

# 首页配置
SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
# 首页标题
SIMPLEUI_HOME_TITLE = '百度一下你就知道'
# 首页图标
SIMPLEUI_HOME_ICON = 'layui-icon-rate'

```
三项配置都是选填，不填都会有默认值。
[图标列表](/ICON.md)

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
+ [详细更新日志](/HISTORY.md)

## version 1.4.7
- [x] 标题页点击刷新菜单无效
- [x] 列表页的过滤条件下拉框，如果类型为普通字段，内容不能被正确显示
- [x] 所有的搜索，在第一页显示正常，但是在第二页的时候就丢失了搜索关键字，也就是说这个第二页就是当前页面所有数据分页之后的第二页
- [X] 在list_filter中，不能按时间过滤(增加了时间区域选择，由于django的限制，暂时不能很好的发挥作用)

## version 1.4.8
- [X] 修复日期bug      

## 预览图
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片1.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片2.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片3.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片4.png)
![img](https://github.com/newpanjing/simpleui/raw/master/images/图片5.png)

## 自动配图标
> 改版本的图标猜测功能可能不大完善，大家可以提issue 来完善。

## 2.0版本建议收集
大家对2.0版有任何建议都可以在此提出，近期将着手开发2.0版本，将采用元件的UI + VUE进行开发。让这个主题更加的现代化和人性化。
[https://github.com/newpanjing/simpleui/issues/9](https://github.com/newpanjing/simpleui/issues/9)

## 扫码领红包:
![支付宝扫码领红包](https://github.com/newpanjing/simpleui/raw/master/images/alipay_qrcode.png)

## 赞助💰
如果你觉得simpleui对你有帮助，你可以赞助我们一杯开发，鼓励我们继续开发维护下去。
![扫码赞助](https://github.com/newpanjing/simpleui/raw/master/images/pay.png)
