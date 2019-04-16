window.getLanuage = function (key) {
    console.log(key)
    if (!window.Lanuages) {
        return "";
    }
    var val = Lanuages[key];
    if (!val || val == "") {
        val = key;
    }
    return val
}