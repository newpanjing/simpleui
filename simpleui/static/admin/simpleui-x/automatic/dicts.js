/**
 全自动匹配图标，只支持中文
 python运算效率低，把运算放客户端来减轻服务器运行压力
 词库持续完善中，https://github.com/newpanjing/simpleui/issues/35
 */

var dicts = {
    //系统
    'fab fa-microsoft': ['系统', '微软', '管理'],
    //组
    'fas fa-users-cog': ['分组', '组合', '组队', '队伍', '队列'],
    //权限
    'fas fa-shield-alt': ['权限', '权利'],
    //人
    'far fa-user': ['管理员', '用户', '员工', '成员', '工人', '职员', '职工', '农民', '清洁工', '客户', '账户', '会员', '供应商', '教师', '老师'],
    //医生
    'fas fa-user-md': ['医生', '护士', '大夫'],
    //配置
    '': ['配置', '设置', '设立', '设定'],
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
    'fas fa-list': ['类别', '类目', '分类', '列表', '集合'],
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
    'fas fa-book-open': ['文章', '博文', '日记']
}