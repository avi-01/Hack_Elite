const express = require("express")
var amqp = require('amqplib/callback_api');
const port = 3001
const app = express()

function send(queue,msg)
{
    amqp.connect('amqp://localhost', function(error0, connection) {
                if (error0) {
                throw error0;
                }

                connection.createChannel(function(error1, channel) {
                    if (error1) {
                        throw error1;
                    }

                    channel.assertQueue(queue, {
                    durable: false
                    });


                    channel.sendToQueue(queue, Buffer.from(msg));
                
                });

            });
}

app.get('/website',(req,res)=>{
    const domain = req.query.domain
    const bool = req.query.bool

    const message = {
        domain,
        bool
    }

    const msg= JSON.stringify(message)
    console.log(msg)
    send("website",msg)

})


app.get('/',(req,res)=>{
    res.send("Hello")
})
app.listen(port, ()=>{
    console.log("Server running on "+port)
})