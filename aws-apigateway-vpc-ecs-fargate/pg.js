
const {Pool, Client} = require('pg');

const config = {
    user: 'XXXXXXXXXX',
    database: 'postgres',
    password: 'XXXXXXXXXX',
    port: 5432,
    //host: 'data-coe-gsa-aurorapg-sampledata.cluster-cozpouof2ron.us-east-2.rds.amazonaws.com'
    host: 'XXXXXXXXXX'
};

const client = new Client(config);
const pool = new Pool(config);

module.exports.client = client;
module.exports.pool = pool;