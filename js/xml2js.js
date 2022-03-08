//xml转json
let xml2js = hitchhiker.require('xml2js');
function xml2json (testXML) {
    let jsons ;
    xml2js.parseString(testXML, {explicitArray : false}, function(err, json) {
        jsons=json
        console.log("转换成json：")
        console.log(jsons)
    });
    return jsons
}
//json转xmj
function json2xml(obj) {
    var builder = new xml2js.Builder();
    var xml = builder.buildObject(obj);
    console.log("转换成xml：")
    console.log(xml)
    return xml
}