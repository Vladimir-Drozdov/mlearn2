const path = require("path");
const express = require("express");
var bodyParser = require('body-parser')
const cors = require('cors');
const app=express();
app.use(express.json());
   
app.use(express.static("public"));
// app.use(cors());
// app.use(bodyParser.json())
// const urlencodedParser = bodyParser.urlencoded({
//     extended: true,//false - было раньше
// });
//const url="https://parantek.com/en/index.php"
const {spawn}=require('child_process');

app.get('/',(req,res)=>{
    res.sendFile(path.resolve(__dirname, 'index.html'));
    
})
app.post("/", function (request, response) {//получилось
    if(!request.body) return response.sendStatus(400);
    //response.header("Access-Control-Allow-Origin", "*");
    //response.header("Access-Control-Allow-Headers", "X-Requested-With");
    console.log(request.body)
    const userName = request.body.name;
    url=userName
    content="1"
    const childPython=spawn('python',['script.py', url]);
    myPromise=new Promise(function(resolve,reject){
        console.log("Начали")
        console.log(url)
        childPython.stdout.on('data', (data)=>{
            const data2=data.toString();
            content= JSON.parse(data2);
            resolve(content);
        })
        childPython.stderr.on('data', (data) => { 
            console.error(`stderr: ${data}`);
        });
        childPython.on('error', (err) => {
            reject(err)
        });
    })
    myPromise.then((data)=>{
        response.send(data)
    })

    childPython.on('close', (code)=>{
        console.log(`child process exited with code ${code}`);
    })
});
app.listen(3000, ()=>console.log("Сервер запущен по адресу http://localhost:3000"))
// const { PythonShell } = require('python-shell');

// // Задайте параметры скрипта Python
// let options = {
//    // pythonPath: '/usr/bin/python3', // Путь к интерпретатору Python
//    // scriptPath: '/path/to/script/', // Путь к папке, содержащей скрипт Python
//     args: ['john', 'ed'] // Аргументы передаваемые в скрипт
// };

// // Создайте новую инстанцию PythonShell с указанными параметрами
// // let pyshell = new PythonShell('script.py');

// // // Обработчик вывода из скрипта 
// // pyshell.on('message', function (message) {
// //     console.log(message);
// // });
// PythonShell.run("./script.py", options).then(messages=>{
//     console.log('results', results)
// })

//https://www.kinopoisk.ru
//https://parantek.com/en/index.php

