const express = require("express")
require('./mongoose')
const blinkRouter = require('./routers/blink')
const timeRouter = require('./routers/time')
const userRouter = require('./routers/user')
const historyRouter = require('./routers/history')

const port = process.env.PORT || 3001
const app = express()


app.use(express.json())
app.use(blinkRouter)
app.use(timeRouter)
app.use(userRouter)
app.use(historyRouter)



app.get('/',(req,res)=>{
    res.send("Hello")
})
app.listen(port, ()=>{
    console.log("Server running on "+port)
})