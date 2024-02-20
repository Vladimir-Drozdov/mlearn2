import sys
url=sys.argv[1]

import requests
import json
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
#from requests_html import HTMLSession

csp_presence = False
def forms_on_page(url):
    #По url я получаю все формы на стнанице
    response = requests.get(url)
    content = response.content
    soup = bs(content, "html.parser")
    all_forms = soup.find_all("form")
    return all_forms
def csrf_token(url):#ищет csrf-токен на странице
    csrfToken_in_input = False
    csrfToken_in_meta = False
    response = requests.get(url)
    content = response.content
    soup = bs(content, "html.parser")
    all_inputs = soup.find_all('input')
    for input in all_inputs:
        if(input.has_attr('name')):
            value = input['name']
            if 'csrf' in value:
                if input['value']:
                    csrfToken_in_input = True
    all_meta = soup.find_all('meta')
    for meta in all_meta:
        if(meta.has_attr('name')):
            value = meta['name']
            if 'csrf' in value:
                csrfToken_in_meta = True
    if csrfToken_in_input or csrfToken_in_meta:
        return 1#есть csrf-токен
    return 0#нет csrf-токена
def inner_HTML(url):
    # Инициализируем сессию
    session = requests.Session()
    # получаем HTML-контент
    html = session.get(url).content
    soup = bs(html, "html.parser")
    # получаем Java-Script файлы
    script_files = []
    innerhtml_in_js = 0
    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            script_url = urljoin(url, script.attrs.get("src"))
            script_files.append(script_url)
    for i in range(0, len(script_files)):
        url = script_files[i]
        response = requests.get(url)
        text = response.text
        text = text.lower()
        if "innerhtml" in text:
            innerhtml_in_js = 1
    response = requests.get(url)
    text = response.text
    text = text.lower()
    innerHTML_string = "innerhtml"
    if innerHTML_string in text or innerhtml_in_js:
        return 1  # есть innerHTML, который стоит заменить на innerText
    else:
        return 0  # нет innerText
def Dom_Purify(url):
    # Инициализируем сессию
    response_html = requests.get(url)
    session = requests.Session()
    # Получаем HTML-контент
    html = session.get(url).content
    soup = bs(html, "html.parser")
    # Получаем Java-Script файлы
    script_files = []
    dompurify_in_js=0
    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            script_url = urljoin(url, script.attrs.get("src"))
            script_files.append(script_url)
    for i in range(0,len(script_files)):
        url = script_files[i]
        response = requests.get(url)
        text = response.text
        text = text.lower()
        if "dompurify" in text:
            dompurify_in_js = 1
    text = response_html.text
    text = text.lower()
    if "dompurify" in text or dompurify_in_js:
         return 1#есть DOMPurify
    else:
        return 0#нет DOMPurify
def inputs_in_form(form):
    details = {}
    # получаю action у формы
    action_of_form = form.attrs.get("action").lower()
    # получаю метод формы
    method_of_form = form.attrs.get("method", "get").lower()
    # Получаю информацию о форме
    inputs = []
    list_of_inputs_in_form=form.find_all("input")
    for input in list_of_inputs_in_form:
        input_type = input.attrs.get("type", "text")
        input_name = input.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action_of_form
    details["method"] = method_of_form
    details["inputs"] = inputs
    return details #словарь содержит информацию о input-ах формы
def submitting_of_form(form_details, url, value):#отправляем форму
    # составляем полный url
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    csp_presence = False
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            #print(value, type(value))
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            if input_value != None:
                data[input_name] = input_value
    if form_details["method"] == "post":
        response = requests.post(target_url, data=data)

        return response
    else:
        return requests.get(target_url, params=data)

def check_csp(csp):
    unsafe_inline = "unsafe" in csp or "inline" in csp
    unsafe_eval = "unsafe" in csp or "eval" in csp
    http = "http" in csp
    if unsafe_inline or unsafe_eval or http:
        return 0
    return 1

def vulnerability_scan(url):
    formsInfo=[]
    forms = forms_on_page(url)
    js_script = "<script>alert('hi')</script>"
    is_vulnerable = False
    # iterate over all forms
    for form in forms:
        form_details = inputs_in_form(form)
        response = submitting_of_form(form_details, url, js_script)
        content = response.content.decode()
        headers = response.headers
        check = 1
        if 'Content-Security-Policy' in headers:
            csp = headers['Content-Security-Policy']
            check = check_csp(csp)
            csp_presence = True
        else:
            csp_presence = False
            check = 0

        if js_script in content:
            is_vulnerable = True
        if csp_presence and check:
            is_vulnerable = False

        if(is_vulnerable == True):
            formsInfo.append({"form_details": form_details, "is_vulnerable": is_vulnerable, "csp_presence": csp_presence, "csp_is_right": check, })#check-проверяет правильно ли установлен csp, DomPurify=1, если он есть =0, если его нет; innerHTML=1, если он есть,=0,если его нет; scrfToken=1, если есть, =0, если нет
    if formsInfo:
        DomPurify = Dom_Purify(url)
        innerHTML = inner_HTML(url)
        csrfToken = csrf_token(url)
        formsInfo.append({"DomPurify": DomPurify, "innerHTML": innerHTML, "csrfToken": csrfToken})
    return json.dumps(formsInfo)

print(vulnerability_scan(url))#False, если есть санитайзинг, True-если есть CSP, экранирование(на клиентской стороне, т.е. нужна защита на двух уровнях чтобы все было впорядке), проверяет только ту страницу, на которыую ведет action у form
#https://parantek.com/en/index.php - пример плохого сайта
#https://www.kinopoisk.ru/ - пример хорошего сайта



#рассмотреть конкурентов по vulnerability scanner, составить статистику по ним (можно разделить на наши и зарубежные), в чем преим-ва или отличия моего приложения от этих. Нужны более новые статьи. Распечатать отзыв и принести - оценка B