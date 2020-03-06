function fetch() {
    text = $.ajax({
        type: "GET", async: false,
        url: "http://127.0.0.1:8206/fet" + uri()
    });
    $("#content").html(text.responseText);

}

function randints(r, n, tof) {
    var result = [];
    if (tof) {
        return Math.floor(Math.random() * r);
    }
    for (var i = 0; i < n; i++) {
        s = Math.floor(Math.random() * r);
        result.push(s);
    }
    return result.join('');

}

function randstrs(n) {
    // 生成随机字母，n 为随机字母的数量
    var result = [];
    for (var i = 0; i < n; i++) {
        s = String.fromCharCode(65 + randints(25, 1, 1));
        result.push(s)
    }
    return result.join('');
}


function uri() {
    var action = randints(9, 5, 0);
    var tim = Math.round(new Date().getTime() / 1000).toString();
    var randstr = randstrs(5);
    var validata = $('#captcha').val();
    var crypto = encrypt(validata, 'nishizhu')
    var hexs = md5(action + tim + randstr + validata);
    args = '?action=' + action + '&tim=' + tim + '&randstr=' + randstr + '&sign=' + hexs + '&validata=' + validata + '&captcha=' + crypto;
    return args;

}

function encrypt(key, plaintText) {
    var plaintText = plaintText;
    var key = key;
    var options = {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    };
    const CRYPTOJSKEY = key;
    var key = CryptoJS.enc.Utf8.parse(CRYPTOJSKEY);
    var encryptedData = CryptoJS.AES.encrypt(plaintText, key, options);
    var encryptedBase64Str = encryptedData.toString().replace(/\//g, "_");
    encryptedBase64Str = encryptedBase64Str.replace(/\+/g, "-");
    return encryptedBase64Str;
}


function urii() {
    var action = randints(9, 5, 0);
    var tim = Math.round(new Date().getTime() / 1000).toString();
    var randstr = randstrs(5);

    var hexs = md5(action + tim + randstr);
    args = '?action=' + action + '&tim=' + tim + '&randstr=' + randstr + '&sign=' + hexs;
    return args;

}