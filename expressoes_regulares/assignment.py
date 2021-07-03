"""

Já vimos os meta-caracteres | (ou), . (qualquer coisa) e [] (conjunto)
Vamos ver agora os  meta-caracteres quantificadores, que são representados pelos símbolos:
 - *   - representa 0 ou n (pode ser ilimitada) repetições
 - +   - representa 1 ou n (pode ser ilimitada) repetições
         pode ser usado num grupo como [a-zA-Z0-9]+
 - ?   - representa 0 ou 1 repetição
 - {}  - especificando as vezes e pode ser equivalente ao quantificadores acima
 - ()

Assignment from coursera course:  Introduction to Data Science in Python
"""

# ------------------------------- Parte A - Find all names in the string

import re


def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    return re.findall(r'Amy|Mary|Ruth|Peter', simple_string)


# print(names())

# ------------------------------------ Part B - Obtain the grades B in the file grades.txt


def grades():
    with open("grades.txt", "r") as file:
        notas = file.read()
    list_b = re.findall(r'[a-zA-Z]+.[a-zA-Z]+:.B', notas)
    list_names = []
    for i in range(16):
        pattern = re.findall(r'[a-zA-Z]+.[a-zA-Z]+', list_b[i])
        list_names.append(pattern[0])
    return list_names


# print(grades())


# Part C


texto = '''
    146.204.224.152 - feest6811 [21/Jun/2019:15:45:24 -0700] "POST /incentivize HTTP/1.1" 302 4622
    159.253.153.40 - - [21/Jun/2019:15:46:10 -0700] "POST /e-business HTTP/1.0" 504 19845
    159.253.153.40 - - [21/Jun/2019:15:46:10 -0700] "POST /e-business HTTP/1.0" 504 19845
    136.195.158.6 - feeney9464 [21/Jun/2019:15:46:11 -0700] "HEAD /open-source/markets HTTP/2.0" 204 21149
    126.196.238.197 - gusikowski9864 [21/Jun/2019:15:45:45 -0700] "DELETE /rich/reinvent HTTP/2.0" 405 7894
    63.134.169.160 - - [21/Jun/2019:15:46:45 -0700] "PUT /syndicate HTTP/1.1" 302 7654
    98.74.141.240 - terry3353 [21/Jun/2019:15:46:46 -0700] "GET /paradigms/reintermediate/web-enabled HTTP/1.1" 403 9171
    249.157.76.12 - doyle8092 [21/Jun/2019:15:46:47 -0700] "HEAD /end-to-end/open-source/markets HTTP/1.0" 501 9767
     '''


def logs():
    with open("logdata.txt", "r") as file:
        data = file.read()
    host = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', data)
    user_name = re.findall(r'[a-z]{1,10}[0-9]{4}|-.-.?', data)

    for i in range(len(user_name)):
        if user_name[i] == "- - ":
            user_name[i] = '-'

    time = re.findall(r'[0-9]{2}/[a-zA-Z].+.0700', data)
    request = re.findall(r'[PDHG]{1,6}.+\.[012]', data)

    lista_logs = [{'host': host[i],
                   'user_name':user_name[i],
                   'time':time[i],
                   'request':request[i]
                   }
                  for i in range(len(host))]

    return lista_logs


print(logs()[978])


one_item = {
    'host': '146.204.224.152',
    'user_name': 'feest6811',
    'time': '21/Jun/2019:15:45:24 -0700',
    'request': 'POST /incentivize HTTP/1.1'
}
# print(one_item in logs())
