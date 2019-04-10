(function () {
    new Vue({
        el: '#main',
        data: {
            height: 1000,
            fold: false,
            zoom: false,
            timeline: true,
            tabs: [home],
            tabModel: 0,
            tabIndex: 0,
            menus: [],
            menuActive: '1',
            breadcrumbs: [],
            language: window.language,
            pwdDialog: {},
            popup: {
                left: 0,
                top: 0,
                show: false,
                tab: null,
                menus: [{
                    text: '刷新',
                    icon: 'el-icon-refresh',
                    handler: function (tab, item) {
                        try {
                            document.getElementById(tab.id).contentWindow.location.reload(true);
                        } catch (e) {
                            console.log(e)
                            var url = tab.url.split('?')[0];
                            tab.url = url + '?_=' + new Date().getTime()
                        }
                    }
                }, {
                    text: '关闭当前',
                    icon: 'el-icon-circle-close-outline',
                    handler: function (tab, item) {
                        app.handleTabsEdit(tab.id, 'remove');
                    }
                }, {
                    text: '关闭其他',
                    icon: 'far fa-copy',
                    handler: function (tab) {
                        app.tabs.forEach(item => {
                            if (item.id != tab.id) {
                                app.handleTabsEdit(item.id, 'remove');
                            }
                        })
                    }
                }, {
                    text: '全部关闭',
                    icon: 'el-icon-close',
                    handler: function (tab, item) {

                        app.$confirm('您确定要关闭全部标签吗?', '提示', {
                            confirmButtonText: '确定',
                            cancelButtonText: '取消',
                            type: 'warning'
                        }).then(function () {
                            app.tabs.forEach((tab, index) => {
                                if (index != 0) {
                                    app.handleTabsEdit(tab.id, 'remove');
                                }
                            });
                            app.menuActive = '1';
                        }).catch(function () {

                        });

                    }
                }, {
                    text: '新标签打开',
                    icon: 'el-icon-news',
                    handler: function (tab, item) {
                        window.open(tab.url);
                    }
                }]
            }
        },
        created: function () {
            var self = this;
            window.onload = window.onresize = function () {
                self.height = document.documentElement.clientHeight || document.body.clientHeight
                var width = document.documentElement.clientWidth || document.body.clientWidth;
                self.fold = width < 800;
            }
            window.app = this;
            this.menus = window.menus

        },
        methods: {
            openUrl:function(url){
                window.open(url);
            },
            contextmenu: function (item, e) {
                //home没有popup menu
                if (item.index == '1') {
                    return;
                }
                this.popup.tab = item;
                this.popup.left = e.clientX;
                this.popup.top = e.clientY;
                this.popup.show = true;
            },
            mainClick: function (e) {
                this.popup.show = false;
            },
            tabClick: function (tab) {
                var item = this.tabs[tab.index];
                var index = item.index;
                this.menuActive = index;
                this.breadcrumbs = item.breadcrumbs;
            },
            handleTabsEdit: function (targetName, action) {

                var self = this;
                if (action === 'remove') {
                    var next = '0';
                    this.tabs.forEach((tab, index) => {
                        if (tab.id == targetName) {
                            var temp = self.tabs[index + 1] || self.tabs[index - 1];
                            if (temp) {
                                next = temp.id;
                                self.menuActive = temp.index;
                                self.breadcrumbs = temp.breadcrumbs;
                            }
                        }
                    });
                    this.tabModel = next;

                    if (targetName != 0) {
                        this.tabs = this.tabs.filter(tab => tab.id !== targetName);
                    }
                }
            }
            ,
            openTab: function (data, index) {

                this.breadcrumbs = data.breadcrumbs;
                var exists = null;
                //判断是否存在，存在就直接打开
                for (var i = 0; i < this.tabs.length; i++) {
                    var tab = this.tabs[i];
                    if (tab.name == data.name) {
                        exists = tab;
                        continue;
                    }
                }

                if (exists) {
                    this.tabModel = exists.id;
                } else {
                    data.id = new Date().getTime() + "" + Math.random();
                    data.index = index;
                    this.tabs.push(data);
                    this.tabModel = data.id;
                }

            }
            ,
            foldClick: function () {
                console.log('11')
                if (this.fold) {
                    this.fold = false;
                } else {
                    this.fold = true;
                }
            }
            ,
            changePassword: function () {
                var width = document.documentElement.clientWidth || document.body.clientWidth;
                if (width > 800) {
                    this.pwdDialog = {
                        url: '/admin/password_change/',
                        name: language.change_password,
                        show: true
                    };
                } else {
                    this.openTab({url: '/admin/password_change/', icon: 'far fa-edit', name: language.change_password})
                    app.breadcrumbs = [language.change_password];
                }
            }
            ,
            logout: function () {
                this.$confirm(language.confirm, '提示', {
                    confirmButtonText: language.yes,
                    cancelButtonText: language.no,
                    type: 'warning'
                }).then(function () {
                    window.location.href = '/admin/logout';
                }).catch(function () {

                });
            }
            ,
            goIndex: function () {
                window.open('/');
            }
            ,
            goZoom: function () {
                var el = window.document.body;
                if (!this.zoom) {

                    var isFullscreen = document.fullScreen || document.mozFullScreen || document.webkitIsFullScreen;
                    if (!isFullscreen) {//进入全屏,多重短路表达式
                        (el.requestFullscreen && el.requestFullscreen()) ||
                        (el.mozRequestFullScreen && el.mozRequestFullScreen()) ||
                        (el.webkitRequestFullscreen && el.webkitRequestFullscreen()) || (el.msRequestFullscreen && el.msRequestFullscreen());
                    }
                    this.zoom = true;
                } else {

                    document.exitFullscreen ? document.exitFullscreen() :
                        document.mozCancelFullScreen ? document.mozCancelFullScreen() :
                            document.webkitExitFullscreen ? document.webkitExitFullscreen() : '';
                    this.zoom = false;
                }
            }
            ,
            displayTimeline: function () {
                this.timeline = !this.timeline;
            },
            report: function () {
                window.open('https://github.com/newpanjing/simpleui/issues')
            }
        }
    })
})();