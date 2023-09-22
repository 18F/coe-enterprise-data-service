
const {Pool, Client} = require('pg');

const config = {
    user: 'gsa_data_pguser',
    database: 'postgres',
    password: 'dqVvAy89h9RsV3kEKn',
    port: 5432,
    //host: 'data-coe-gsa-aurorapg-sampledata.cluster-cozpouof2ron.us-east-2.rds.amazonaws.com'
    host: 'aurora-postgres-cluster-complete-postgresql.cluster-ro-cozpouof2ron.us-east-2.rds.amazonaws.com'
};

const client = new Client(config);
const pool = new Pool(config);

module.exports.client = client;
module.exports.pool = pool;