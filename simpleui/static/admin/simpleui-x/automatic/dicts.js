/**
 全自动匹配图标，只支持中文
 python运算效率低，把运算放客户端来减轻服务器运行压力
 词库持续完善中，https://github.com/newpanjing/simpleui/issues/35
 */

// 给部分词设置权重，比如用户信息、用户留言、用户收藏，降低用户权重，使之选第二个词配图标
// 权重0-1
var weights = {
    '用户': 0.1,
    '部门': 0.1,
    '机构': 0.1
}
var dicts = {
    //系统
    'fab fa-microsoft': ['系统', '微软'],
    //组
    'fas fa-users-cog': ['分组', '组合', '组队', '队伍', '队列'],
    //权限
    'fas fa-shield-alt': ['权限', '权利'],
    //人
    'far fa-user': ['管理员', '用户', '员工', '成员', '工人', '职员', '职工', '农民', '清洁工', '客户', '账户', '会员', '供应商', '教师', '老师'],
    //医生
    'fas fa-user-md': ['医生', '护士', '大夫'],
    //配置
    'fas fa-cog': ['配置', '设置', '设立', '设定'],
    //日志
    'far fa-bookmark': ['日志', '记录'],
    //终端
    'fas fa-terminal': ['终端', '命令', '命令行', '控制台'],
    //机构
    'fas fa-university': ['机构', '部门'],
    //设备
    'fas fa-tablet-alt': ['设备'],
    //仪表
    'fas fa-tachometer-alt': ['仪表', '水表', '电表', '燃气表', '压力表', '温度表', '湿度表', '速度表'],
    //数据
    'fas fa-database': ['数据', '数据库'],
    //分析
    'far fa-chart-bar': ['分析', '图表', '统计', '统计图'],
    //蜘蛛
    'fas fa-spider': ['采集', '收集', '爬虫', '调试'],
    //异常
    'fas fa-exclamation-triangle': ['异常', '错误', '警告', '警报', '报警'],
    //产品
    'fas fa-shopping-cart': ['产品', '货物', '商品', '购物车'],
    //分类
    'fas fa-list': ['类别', '类目', '分类', '列表', '集合', '排行'],
    //职位
    'fas fa-chalkboard-teacher': ['职位', '职能', '职称'],
    //车
    'fas fa-car': ['汽车', '摩托车', '轿车', '货车', '公交车', '单车', '采购'],
    //计划
    'far fa-calendar-alt': ['计划', '定时', '日程', '日历'],
    //仓库
    'fas fa-warehouse': ['库存', '仓库', '房子'],
    //订单
    'fas fa-shopping-bag': ['订单'],
    //导入
    'fas fa-upload': ['导入', '上传'],
    //导出
    'fas fa-download': ['导出', '下载'],
    //网站
    'fas fa-globe-americas': ['网站', '网址', '站点', '官网'],
    //评论
    'far fa-comments': ['评论', '评价', '点评', '留言', '消息'],
    //文章
    'fas fa-book-open': ['文章', '博文', '日记'],
    //字典
    'fas fa-book': ['字典', '词典', '书籍', '书本'],
    //编辑
    'far fa-edit': ['编辑', '修改', '编写', '改变'],
    //钱相关
    'fas fa-yen-sign': ['金额', '账务', '财务', '美元', '英镑', '港币', '人民币', '提现', '充值', '奖金', '返利', '返佣'],
    //修复
    'fas fa-wrench': ['修复', '修理'],
    //货物
    'fas fa-truck': ['发货', '收货', '货物', '物品', '贸易'],
    //地图
    'fas fa-map-marker-alt': ['地图', '导航', '路线', '路程', '地址', '住址'],
    //音乐
    'fas fa-music': ['音乐', '歌曲', '歌词', '歌手', '歌唱家', '演唱会', 'MV'],
    //电影
    'fas fa-film': ['电影', '电视', '节目', '录像', '影片', '影视', '视频'],
    //菜单
    'fas fa-bars': ['菜单', '功能', '模块'],
    //链接
    'fas fa-link': ['链接', '连接', '友链', '友情链接'],
    //通知
    'fas fa-bullhorn': ['通知', '告知', '通告', '公告', '喇叭'],
    //主页
    'fas fa-home': ['主页', '首页', 'index', 'Index'],
    //银行
    'fas fa-credit-card': ['银行卡', '银行', '信用卡', '储蓄卡'],
    //ad
    'fas fa-ad': ['宣传', '广告', 'banner', 'Banner', 'ad', 'Ad'],
    //hot
    'fab fa-hotjar': ['热搜', '热度', '火焰'],
    //info
    'fas fa-info': ['信息', 'info'],
    //支付宝
    'fab fa-alipay': ['支付宝', '余额宝', '余利宝', '蚂蚁花呗'],
    //微信
    'fab fa-weixin': ['微信', 'WeChart'],
    //交易
    'fab fa-paypal': ['交易', '支付', '贝付', 'paypal'],
    //收藏
    'far fa-star': ['收藏', '星星', '五角星', '中国'],
    //短信
    'far fa-comment-dots': ['短信', '消息', '提示']
}