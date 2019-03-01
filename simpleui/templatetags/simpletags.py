# -*- coding: utf-8 -*-

import jieba
from django import template
from django.utils.html import format_html
from django.conf import settings
import os
import json

register = template.Library()

icons = [{
    "name": "半星",
    "cls": "layui-icon-rate-half"
}, {
    "name": "星星,空心",
    "cls": "layui-icon-rate"
}, {
    "name": "星星,实心",
    "cls": "layui-icon-rate-solid"
}, {
    "name": "手机,电话",
    "cls": "layui-icon-cellphone"
}, {
    "name": "验证码",
    "cls": "layui-icon-vercode"
}, {
    "name": "微信",
    "cls": "layui-icon-login-wechat"
}, {
    "name": "QQ",
    "cls": "layui-icon-login-qq"
}, {
    "name": "微博",
    "cls": "layui-icon-login-weibo"
}, {
    "name": "密码",
    "cls": "layui-icon-password"
}, {
    "name": "用户,用户名 会员 客户",
    "cls": "layui-icon-username"
}, {
    "name": "刷新-粗",
    "cls": "layui-icon-refresh-3"
}, {
    "name": "授权,权限",
    "cls": "layui-icon-auz"
}, {
    "name": "菜单,左向右伸缩菜单",
    "cls": "layui-icon-spread-left"
}, {
    "name": "右向左伸缩菜单",
    "cls": "layui-icon-shrink-right"
}, {
    "name": "雪花",
    "cls": "layui-icon-snowflake"
}, {
    "name": "提示,说明",
    "cls": "layui-icon-tips"
}, {
    "name": "便签,标签",
    "cls": "layui-icon-note"
}, {
    "name": "主页 首页 home HOME index INDEX 欢迎页 欢迎",
    "cls": "layui-icon-home"
}, {
    "name": "高级",
    "cls": "layui-icon-senior"
}, {
    "name": "刷新",
    "cls": "layui-icon-refresh"
}, {
    "name": "刷新",
    "cls": "layui-icon-refresh-1"
}, {
    "name": "旗帜,标志",
    "cls": "layui-icon-flag"
}, {
    "name": "主题,风格,样式",
    "cls": "layui-icon-theme"
}, {
    "name": "消息,通知",
    "cls": "layui-icon-notice"
}, {
    "name": "网站,站点",
    "cls": "layui-icon-website"
}, {
    "name": "控制台 仪表盘",
    "cls": "layui-icon-console"
}, {
    "name": "表情-惊讶",
    "cls": "layui-icon-face-surprised"
}, {
    "name": "设置-空心",
    "cls": "layui-icon-set"
}, {
    "name": "模板",
    "cls": "layui-icon-template-1"
}, {
    "name": "应用 APP app PC",
    "cls": "layui-icon-app"
}, {
    "name": "模板",
    "cls": "layui-icon-template"
}, {
    "name": "赞",
    "cls": "layui-icon-praise"
}, {
    "name": "踩",
    "cls": "layui-icon-tread"
}, {
    "name": "男",
    "cls": "layui-icon-male"
}, {
    "name": "女",
    "cls": "layui-icon-female"
}, {
    "name": "相机-空心",
    "cls": "layui-icon-camera"
}, {
    "name": "相机-实心",
    "cls": "layui-icon-camera-fill"
}, {
    "name": "菜单-水平",
    "cls": "layui-icon-more"
}, {
    "name": "菜单-垂直",
    "cls": "layui-icon-more-vertical"
}, {
    "name": "金额-人民币 钱 额度",
    "cls": "layui-icon-rmb"
}, {
    "name": "金额-美元",
    "cls": "layui-icon-dollar"
}, {
    "name": "钻石-等级",
    "cls": "layui-icon-diamond"
}, {
    "name": "火",
    "cls": "layui-icon-fire"
}, {
    "name": "返回",
    "cls": "layui-icon-return"
}, {
    "name": "位置-地图",
    "cls": "layui-icon-location"
}, {
    "name": "办公-阅读 文章 新闻",
    "cls": "layui-icon-read"
}, {
    "name": "调查 问卷",
    "cls": "layui-icon-survey"
}, {
    "name": "表情-微笑",
    "cls": "layui-icon-face-smile"
}, {
    "name": "表情-哭泣",
    "cls": "layui-icon-face-cry"
}, {
    "name": "购物车",
    "cls": "layui-icon-cart-simple"
}, {
    "name": "购物车",
    "cls": "layui-icon-cart"
}, {
    "name": "下一页",
    "cls": "layui-icon-next"
}, {
    "name": "上一页",
    "cls": "layui-icon-prev"
}, {
    "name": "上传-空心-拖拽",
    "cls": "layui-icon-upload-drag"
}, {
    "name": "上传-实心",
    "cls": "layui-icon-upload"
}, {
    "name": "下载-圆圈",
    "cls": "layui-icon-download-circle"
}, {
    "name": "组件",
    "cls": "layui-icon-component"
}, {
    "name": "文件-粗",
    "cls": "layui-icon-file-b"
}, {
    "name": "用户",
    "cls": "layui-icon-user"
}, {
    "name": "发现-实心",
    "cls": "layui-icon-find-fill"
}, {
    "name": "loading 进度",
    "cls": "layui-icon-loading layui-icon layui-anim layui-anim-rotate layui-anim-loop"
}, {
    "name": "loading",
    "cls": "layui-icon-loading-1"
}, {
    "name": "添加",
    "cls": "layui-icon-add-1"
}, {
    "name": "播放",
    "cls": "layui-icon-play"
}, {
    "name": "暂停",
    "cls": "layui-icon-pause"
}, {
    "name": "音频-耳机",
    "cls": "layui-icon-headset"
}, {
    "name": "视频 动画",
    "cls": "layui-icon-video"
}, {
    "name": "语音-声音",
    "cls": "layui-icon-voice"
}, {
    "name": "消息-通知-喇叭 公告 动态",
    "cls": "layui-icon-speaker"
}, {
    "name": "删除线",
    "cls": "layui-icon-fonts-del"
}, {
    "name": "代码 源码 源代码",
    "cls": "layui-icon-fonts-code"
}, {
    "name": "HTML",
    "cls": "layui-icon-fonts-html"
}, {
    "name": "字体加粗",
    "cls": "layui-icon-fonts-strong"
}, {
    "name": "删除链接",
    "cls": "layui-icon-unlink"
}, {
    "name": "图片",
    "cls": "layui-icon-picture"
}, {
    "name": "链接,友链 友情链接",
    "cls": "layui-icon-link"
}, {
    "name": "表情-笑-粗",
    "cls": "layui-icon-face-smile-b"
}, {
    "name": "左对齐",
    "cls": "layui-icon-align-left"
}, {
    "name": "右对齐",
    "cls": "layui-icon-align-right"
}, {
    "name": "居中对齐",
    "cls": "layui-icon-align-center"
}, {
    "name": "字体-下划线",
    "cls": "layui-icon-fonts-u"
}, {
    "name": "字体-斜体",
    "cls": "layui-icon-fonts-i"
}, {
    "name": "Tabs 选项卡",
    "cls": "layui-icon-tabs"
}, {
    "name": "单选框-选中",
    "cls": "layui-icon-radio"
}, {
    "name": "单选框-候选",
    "cls": "layui-icon-circle"
}, {
    "name": "编辑 修改",
    "cls": "layui-icon-edit"
}, {
    "name": "分享",
    "cls": "layui-icon-share"
}, {
    "name": "删除",
    "cls": "layui-icon-delete"
}, {
    "name": "表单,订单",
    "cls": "layui-icon-form"
}, {
    "name": "手机-细体",
    "cls": "layui-icon-cellphone-fine"
}, {
    "name": "聊天 对话 沟通",
    "cls": "layui-icon-dialogue"
}, {
    "name": "文字格式化",
    "cls": "layui-icon-fonts-clear"
}, {
    "name": "窗口",
    "cls": "layui-icon-layer"
}, {
    "name": "日期",
    "cls": "layui-icon-date"
}, {
    "name": "水 下雨",
    "cls": "layui-icon-water"
}, {
    "name": "代码-圆圈 片段",
    "cls": "layui-icon-code-circle"
}, {
    "name": "轮播组图",
    "cls": "layui-icon-carousel"
}, {
    "name": "翻页",
    "cls": "layui-icon-prev-circle"
}, {
    "name": "布局 页面",
    "cls": "layui-icon-layouts"
}, {
    "name": "工具 设置",
    "cls": "layui-icon-util"
}, {
    "name": "模板 导出 保存",
    "cls": "layui-icon-templeate-1"
}, {
    "name": "上传-圆圈",
    "cls": "layui-icon-upload-circle"
}, {
    "name": "树",
    "cls": "layui-icon-tree"
}, {
    "name": "表格",
    "cls": "layui-icon-table"
}, {
    "name": "图表 统计 分析 画像 报表 数据",
    "cls": "layui-icon-chart"
}, {
    "name": "图标 报表 屏幕",
    "cls": "layui-icon-chart-screen"
}, {
    "name": "引擎 系统",
    "cls": "layui-icon-engine"
}, {
    "name": "下三角",
    "cls": "layui-icon-triangle-d"
}, {
    "name": "右三角",
    "cls": "layui-icon-triangle-r"
}, {
    "name": "文件",
    "cls": "layui-icon-file"
}, {
    "name": "设置-小型",
    "cls": "layui-icon-set-sm"
}, {
    "name": "添加-圆圈",
    "cls": "layui-icon-add-circle"
}, {
    "name": "404",
    "cls": "layui-icon-404"
}, {
    "name": "关于",
    "cls": "layui-icon-about"
}, {
    "name": "箭头 向上",
    "cls": "layui-icon-up"
}, {
    "name": "箭头 向下",
    "cls": "layui-icon-down"
}, {
    "name": "箭头 向左",
    "cls": "layui-icon-left"
}, {
    "name": "箭头 向右",
    "cls": "layui-icon-right"
}, {
    "name": "圆点",
    "cls": "layui-icon-circle-dot"
}, {
    "name": "搜索",
    "cls": "layui-icon-search"
}, {
    "name": "系统",
    "cls": "layui-icon-set-fill"
}, {
    "name": "群组",
    "cls": "layui-icon-group"
}, {
    "name": "好友",
    "cls": "layui-icon-friends"
}, {
    "name": "回复 评论 实心",
    "cls": "layui-icon-reply-fill"
}, {
    "name": "菜单 隐身 实心",
    "cls": "layui-icon-menu-fill"
}, {
    "name": "记录 历史 最近",
    "cls": "layui-icon-log"
}, {
    "name": "图片-细体",
    "cls": "layui-icon-picture-fine"
}, {
    "name": "表情-笑-细体",
    "cls": "layui-icon-face-smile-fine"
}, {
    "name": "列表 目录 分类 订单 退货 退款 报损 报溢",
    "cls": "layui-icon-list"
}, {
    "name": "发布 纸飞机",
    "cls": "layui-icon-release"
}, {
    "name": "对 OK",
    "cls": "layui-icon-ok"
}, {
    "name": "帮助",
    "cls": "layui-icon-help"
}, {
    "name": "客服",
    "cls": "layui-icon-chat"
}, {
    "name": "top 置顶",
    "cls": "layui-icon-top"
}, {
    "name": "收藏-空心",
    "cls": "layui-icon-star"
}, {
    "name": "收藏-实心",
    "cls": "layui-icon-star-fill"
}, {
    "name": "关闭-实心",
    "cls": "layui-icon-close-fill"
}, {
    "name": "关闭-空心 退出 错误",
    "cls": "layui-icon-close"
}, {
    "name": "正确",
    "cls": "layui-icon-ok-circle"
}, {
    "name": "导入",
    "cls": "layui-icon-add-circle-fine"
}]


def find_icon(key):
    for d in icons:
        name = d.get('name')
        if name.find(key) != -1 or key.find(name) != -1:
            return d.get('cls')

    return None


@register.filter
def get_icon(name):
    # 默认为文件图标
    cls = "layui-icon-file"
    try:
        # 系统模块是proxy，分词会报错
        name = str(name)
        seg_list = jieba.lcut_for_search(name, HMM=True)
        for key in seg_list:

            val = find_icon(key)
            if val:
                cls = val
                break

        # print(seg_list)
        # print(cls)
    except:
        pass

    return format_html('<i class="layui-icon {}"></i>', cls)


@register.filter
def test(obj):
    print(obj)
    # pass
    return ''

@register.filter
def date_to_json(obj):
    return json.dumps(obj.date_params)

@register.simple_tag(takes_context=True)
def home_page(context):
    '''
    处理首页，通过设置判断打开的是默认页还是自定义的页面
    :return:
    '''
    home = __get_config('SIMPLEUI_HOME_PAGE')
    if home:
        context['home'] = home

    title = __get_config('SIMPLEUI_HOME_TITLE')
    if not title:
        title = '首页'

    icon = __get_config('SIMPLEUI_HOME_ICON')
    if not icon:
        icon = 'layui-icon-console'

    context['title'] = format_html('<i class="layui-icon {}"></i>{}', icon, title)

    return ''


def __get_config(name):
    value = os.environ.get(name, getattr(settings, name, None))
    return value
