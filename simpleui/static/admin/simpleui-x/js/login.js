new Vue({
    el: '.login-main',
    data: {
        username: '',
        password: ''
    },
    methods: {
        login: function () {
            document.getElementById('login-form').submit();
        }
    }
})