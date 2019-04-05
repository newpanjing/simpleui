(function () {
    new Vue({
        el: '#main',
        data: {
            height: 200,
            fold: false,
            foldIcon: 'el-icon-arrow-left',
            zoom: false
        },
        created: function () {
            var self = this;
            window.onload = window.onresize = function () {
                self.height = document.documentElement.clientHeight || document.body.clientHeight
            }

        },
        methods: {
            openTab: function (data) {
                console.log(data)
            },
            foldClick: function () {
                console.log('11')
                if (this.fold) {
                    this.foldIcon = 'el-icon-arrow-left'
                    this.fold = false;
                } else {
                    this.foldIcon = 'el-icon-arrow-right'
                    this.fold = true;
                }
            }, changePassword: function () {
                this.openTab({url: '/admin/password_change/', icon: '', name: '修改密码'})
            },
            logout: function () {
                this.$confirm('您确定要退出登录吗?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(function () {
                    window.location.href = '/admin/logout';
                })
            },
            goIndex: function () {
                window.open('/');
            },
            goZoom: function () {

                if (!this.zoom) {

                    var el = window.document.body;
                    var isFullscreen = document.fullScreen || document.mozFullScreen || document.webkitIsFullScreen;
                    if (!isFullscreen) {//进入全屏,多重短路表达式
                        (el.requestFullscreen && el.requestFullscreen()) ||
                        (el.mozRequestFullScreen && el.mozRequestFullScreen()) ||
                        (el.webkitRequestFullscreen && el.webkitRequestFullscreen()) || (el.msRequestFullscreen && el.msRequestFullscreen());
                    }
                } else {
                    document.exitFullscreen ? document.exitFullscreen() :
                        document.mozCancelFullScreen ? document.mozCancelFullScreen() :
                            document.webkitExitFullscreen ? document.webkitExitFullscreen() : '';
                }
            }
        }
    })
})();