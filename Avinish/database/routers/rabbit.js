const express = require('express')
const router = new express.Router()
var amqp = require('amqplib/callback_api');

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

router.get('/website',(req,res)=>{
    const domain = req.query.domain
    const bool = req.query.bool

    const message = {
        domain,
        bool
    }

    const msg= JSON.stringify(message)
    console.log(msg)
    send("website",msg)
    res.send()
})

router.get('/youtube',(req,res)=>{
    const title = req.query.title
    const bool = req.query.bool

    const message = {
        title,
        bool
    }

    const msg= JSON.stringify(message)
    console.log(msg)
    send("youtube",msg)
    res.send()

})


router.get('/process',(req,res)=>{
    const list = req.body
    const bool = req.query.bool

    const message = {
        list: JSON.parse(list),
        bool
    }

    const msg= JSON.stringify(message)
    console.log(msg)
    send("process",msg)
    res.send()

})
