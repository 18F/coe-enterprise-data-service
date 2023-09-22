
const redshift = require('node-redshift');

var client = {
    user: 'eds_user',
    database: 'dev',
    password: 'GreaterManchester3!',
    port: 5439,
    //host: '172.31.23.42'
    host: 'redshift-cluster-eds-usda.cd6ncnbo7kin.us-east-2.redshift.amazonaws.com'
};
var redshiftClient = new redshift(client);
module.exports = redshiftClient;