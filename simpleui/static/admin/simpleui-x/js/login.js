if (parent.callback) {
    //如果是在子框架内就把首页刷新
    parent.callback();
}
var loginApp = new Vue({
    el: '.login-main',
    data: {
        username: '',
        password: '',
        code: '',
        identifyCode: '',
        loading: false
    },
    mounted() {
        this.makeCode(6);
    },
    methods: {
        login: function () {
            this.loading = true;

            // 如果有canvas标签，则启用
            let canvas = document.getElementById("s-canvas");
            if (canvas && this.code.toLowerCase() !== this.identifyCode.toLowerCase()) {
                this.$message.error("请输入正确的验证码，不区分大小写");
                this.loading = false;
                return ;
            }
            if (this.username === "" || this.password === "") {
                this.$message.error("Please enter your username or password!");
                this.loading = false;
                return ;
            }
            this.$nextTick(function () {
                document.getElementById('login-form').submit();
            });
        },
        getRandomChars: function (count) {
            let str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            let result = "";
            for (let i = 0; i < count; i++) {
                let index = Math.floor(Math.random() * str.length);
                result += str.substring(index, index+1);
            }
            return result;
        },
        getRandomNum: function (min, max) {
            return Math.floor(Math.random() * (max - min) + min);
        },
        getRandomColor: function () {
            let r = this.getRandomNum(0, 255);
            let g = this.getRandomNum(0, 255);
            let b = this.getRandomNum(0, 255);
            return "rgb(" + r + "," + g + "," + b + ")";
        },
        makeCode: function (count) {
            this.identifyCode = this.getRandomChars(count);
            let canvas = document.getElementById("s-canvas");
            if (canvas) {
                let ctx = canvas.getContext("2d");
                ctx.textBaseline = "bottom";
                ctx.fillStyle = this.getRandomColor();
                ctx.fillRect(0, 0, 150, 40);
                for (let i = 0; i < this.identifyCode.length; i++) {
                    this.drawText(ctx, this.identifyCode[i], i);
                }
                this.drawLine(ctx);
                this.drawDot(ctx);
            }
        },
        drawText: function (ctx, txt, i) {
            ctx.fillStyle = this.getRandomColor();
            ctx.font = this.getRandomNum(35, 40) + "px SimHei";
            let x = (i + 0.5) * (150 / 7);
            let y = this.getRandomNum(40, 35);
            let deg = this.getRandomNum(-10, 10);
            ctx.translate(x, y);
            ctx.rotate((deg * Math.PI) / 180);
            ctx.fillText(txt, 0, 0);
            ctx.rotate((-deg * Math.PI) / 180);
            ctx.translate(-x, -y);
        },
        drawLine: function (ctx) {
            for (let i = 0; i < 3; i++) {
                ctx.strokeStyle = this.getRandomColor();
                ctx.beginPath();
                ctx.moveTo(this.getRandomNum(0, 150), this.getRandomNum(0, 40));
                ctx.lineTo(this.getRandomNum(0, 150), this.getRandomNum(0, 40));
                ctx.stroke();
            }
        },
        drawDot: function (ctx) {
            for (let i = 0; i < 30; i++) {
                ctx.fillStyle = this.getRandomColor();
                ctx.beginPath();
                ctx.arc(this.getRandomNum(0, 150), this.getRandomNum(0, 40), 1, 0, 2*Math.PI);
                ctx.fill()
            }
        }
    }
});