const express = require("express")
var bodyParser = require('body-parser')
const pg = require("./pg")
pgClient = pg.client
pgPool = pg.pool

//var redshiftClient = require('./redshift.js');
const PORT = 80;
const HOST = '0.0.0.0';
var qry = 'select * from '
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.get("/", (req, res)=>{
    res.end(JSON.stringify({message:'Hello from GSA Nodejs from express and ecs fargate architecture!!'}));
})

app.get("/hello", (req, res)=>{
    res.end(JSON.stringify({message:'Hello from GSA Nodejs from express and ecs fargate architecture!!'}));
})

app.get("/about", (req, res)=>{
    res.end("<h1>About!</h1>");
});

// app.get("/start", async (req, res)=>{
//     await pgClient.connect();
//     res.end("<h1>Server started...</h1><h2>Database is available to queries!</h2>");
// });

// app.get("/stop", async (req, res)=>{
//     await pgClient.end();
//     res.end("<h1></h1><h2>Server/DB Closed!</h2>");
// });


app.get("/time", async (req,res)=>{
    qry = 'select now()';
    console.log('Connected to time! -', qry);
    await pgClient.query(qry, async (err, reslt)=>{
        console.log("Error or response::", err, reslt);
        res.end(JSON.stringify(reslt.rows))
    })
})

app.get("/address", async (req, res)=>{
    //qry = 'select * from address';
    //console.log(req.path)
    //const {rows} = await pgPool.query(qry)
    //get the path and substring to remove the /
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})

app.get("/addresschange", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/adjustdeduction", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/adjustment", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/casecontrol", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/casecontrolgroup", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/casefile", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/claimfile", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/currentpay", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/currentpaygroup", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/electronicfundtransfer", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/priorpay", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/priorpaygroup", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/survivor", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/survivorclaim", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/employee", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})
app.get("/taxrecord", async(req, res)=>{
    const {rows} = await pgPool.query(qry + req.path.substring(1));
    res.end(JSON.stringify(rows))
})

app.listen (PORT, HOST, ()=>{
    console.log(`Connected to the server on http://${HOST}:${PORT}!!`);
})

 