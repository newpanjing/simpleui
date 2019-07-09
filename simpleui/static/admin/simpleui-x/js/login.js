new Vue({
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
})