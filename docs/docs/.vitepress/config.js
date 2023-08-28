export default {
    lang: 'zh-CN',
    ignoreDeadLinks: true,
    title: 'Django SimpleUI',
    base: '/',
    locales: {
        root: {
            lang: 'zh-CN',
            label: '简体中文',
        },
        en: {
            lang: 'en-US',
            label: 'English',
            link: '/en/',
        }
    },
    sitemap: {
        hostname: 'https://www.mldoo.com'
    },
    themeConfig: {
        siteTitle: 'SimpleUI Docs',
        logo: '/logo.png',
        footer: {
            message: 'Released under the MIT License.',
            copyright: 'Copyright © 2016-present Simple UI'
        },
        search: {
            provider: 'local'
        },
        externalLinkIcon: true,
        outlineTitle: '大纲',
        lastUpdated: true,
        socialLinks: [
            {icon: 'github', link: 'https://github.com/newpanjing/simpleui_demo'}
        ],
        editLink: {
            pattern: 'https://github.com/newpanjing/simpleui/edit/main/docs/docs/:path'
        },
        nav: [
            {text: 'Home', link: '/'},
            {text: '配置&Config', link: '/config'},
            {text: '社区', link: 'https://www.mldoo.com'},
            {
                text: '更新记录', link: 'https://github.com/newpanjing/simpleui/tags',
            },
            {text: '专业版', link: 'https://www.mldoo.com/simplepro'},
        ],
        sidebar: {
            '/config': [
                {text: '配置&指南', link: '/config'},
                {text: 'pip源切换', link: '#pip源切换'},
                {text: '安装', link: '#安装'},
                {text: '主题', link: '#主题'},
                {text: '图标', link: '#图标'},
                {text: '菜单', link: '#菜单'},
                {text: '模板', link: '#模板'},
                {text: '自定义按钮', link: '#自定义按钮-action'},
                {text: '配置', items:[
                        {text: '关闭登录页粒子动画', link: '#关闭登录页粒子动画'},
                        {text: '修改默认图标', link: '#修改默认图标'},
                        {text: '修改默认首页', link: '#首页-修改默认'},
                        {text: '修改首页地址', link: '#首页-跳转地址'},
                        {text: '修改首页模块', link: '#首页-模块'},
                        {text: '快速操作', link: '#快速操作'},
                        {text: '关闭Loading遮罩层', link: '#关闭loading遮罩层'},
                    ]},
                {text: '国际化', link: '#国际化'},
                {text: '插件', link: '#插件支持'},
                {text: '社区', link: 'https://www.mldoo.com'},
            ]
        },
    }
}