const form = document.forms[0];
const { PythonShell } = require('python-shell');
let pyshell = new PythonShell('script.py');

// Обработчик вывода из скрипта
pyshell.on('message', function (message) {
    console.log(message);
});
form.addEventListener("submit", (e)=>{
    e.preventDefault();
    const input=form.elements.citeName.value;
    console.log(input, typeof input)
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "./probFlask.py", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            // Ответ от сервера доступен в переменной response
            console.log(response);
        }
    };

    xhr.setRequestHeader("Access-Control-Allow-Origin","*");
    xhr.setRequestHeader("Access-Control-Request-Header","*");
    var data = JSON.stringify({variable: input});
    xhr.send(data);
})
