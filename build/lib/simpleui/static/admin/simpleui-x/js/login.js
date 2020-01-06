if (parent.callback) {
    //如果是在子框架内就把首页刷新
    parent.callback();
}
var loginApp = new Vue({
    el: '.login-main',
    data: {
        username: '',
        password: '',
        loading: false
    },
    methods: {
        login: function () {
            this.loading = true
            this.$nextTick(function () {
                document.getElementById('login-form').submit();
            });
        }
    }
});