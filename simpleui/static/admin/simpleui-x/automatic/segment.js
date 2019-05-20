if (!window.dicts) {
    window.dicts = {}
}

function Segment() {
    //初始化词库
    var mappers = {}

    for (key in dicts) {
        var array = dicts[key];
        array.map((value, index) => {
            mappers[value] = key;
        });
    }
    this.getMappers = function () {
        return mappers;
    }
    this.cut = function (sentence) {
        var start = 0, end = sentence.length - 1, result = [];
        while (start != end) {
            var str = [];
            for (var i = start; i <= end; i++) {
                var s = sentence.substring(i, i + 1);

                str.push(s);
                // 如果在字典中，则添加到分词结果集
                if (str.join('') in mappers) {
                    result.push(str.join(''));
                }
            }

            start++;
        }

        return result;
    }
}

var segment = new Segment();

function getIcon(name, icon) {
    var value = 'far fa-file';
    if (icon) {
        //有默认图标的
        if (icon != value) {
            return icon;
        }
    }

    var results = segment.cut(name);
    if (results.length != 0) {
        for (var i = 0; i < results.length; i++) {
            var map = segment.getMappers()
            var temp = map[results[i]];
            if (temp) {
                value = temp;
                break;
            }
        }
    }
    return value;
}