//AES-CBC模式加解密
var CryptoJS = require("crypto-js");
var AesKey = "cloudwisdomadjsn";
var CBCIV = "5721678222017913";
//加密选项
var CBCOptions = {
	iv: CryptoJS.enc.Utf8.parse(CBCIV),
	mode:CryptoJS.mode.CBC,
	padding: CryptoJS.pad.Pkcs7
}
//AES加密
function encrypt(data){
    var key = CryptoJS.enc.Utf8.parse(AesKey);
    var secretData = CryptoJS.enc.Utf8.parse(data);
    var encrypted = CryptoJS.AES.encrypt(
		secretData,
		key,
		CBCOptions
	);
    return encrypted.toString();
}
//AES解密
function decrypt(data){
    var key = CryptoJS.enc.Utf8.parse(AesKey);
    var decrypt = CryptoJS.AES.decrypt(
		data,
		key,
		CBCOptions
	);
    return CryptoJS.enc.Utf8.stringify(decrypt).toString();
}