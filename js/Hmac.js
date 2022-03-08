//HmacSHA1签名
//let CryptoJS = hitchhiker.require("crypto-js");
let Lc_Sid = '9fac9a36c2a845c0209ff4dc3dd25c75';
let SecretKey = 'ee12ba05cd22f998621b2bbae3f3bbba';
//let Lc_Ts = '1587711799182';
let Lc_Ts = new Date().getTime();
function Sign(req_body) {
	var obj={
			Lc_Sid:Lc_Sid,
			SecretKey:SecretKey,
			Lc_Ts:Lc_Ts,
			//Lc_Ts:'1587711799182',
			// QueryStringValue:'http://rezenhotels.com?a=test&b=testb',
			body:req_body,
		}
		function createString(obj={}){
			var arr=[];
			for (key in obj){
				arr.push(obj[key])
			}
			arr.sort();
			var str=arr.join('');
			return str
		}
    var signing = createString(obj)
	var hash = CryptoJS.HmacSHA1(signing,SecretKey)
	console.log('获取签名需要的串：')
	console.log(signing)
	var sign = hash.toString(CryptoJS.enc.Base64);
	console.log('获取签名：')
	console.log(sign)
	console.log('获取当前时间戳：')
    console.log(Lc_Ts)
	//return [sign,Lc_Ts]
	return { sign:sign,lc_ts:Lc_Ts}
}