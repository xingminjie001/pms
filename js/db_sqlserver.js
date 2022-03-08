var sql = hitchhiker.require('mssql');
//sqlserver连接配置
var dbConfig = {
    user: 'test_user',
    password: 't543fDS#5r47',
    server: '192.168.0.17',
    database: 'HYHotel_fenku_zhu',
    //port: 1433,
    pool: {
        max: 10,
        min: 0,
        idleTimeoutMillis: 30000
    }
};
//sql查询
function getsql(sqlstr) {
    var conn = new sql.ConnectionPool(dbConfig);
    var req = new sql.Request(conn);
    return new Promise((resolve, reject) => {
        //连接数据库
        conn.connect(function (err) {
            if (err) {
                console.log(err);
                return;
            }
            // 查询
            req.query(sqlstr, function (err, recordset) {
                conn.release();// 释放连接
                if (err) {
                    reject(err);
                }
                else {
                    resolve(recordset.recordset);
                }
            });
        })
    })
}

//getsql("select top 1 * from vstinfo")