
from bottle import route, run, template, request


@route('/')
def index():
        if request.method == 'GET':
                print "This is GET method loop"
                dicc = request.GET['q']
                if dicc == 'Ping' :
                        return "OK"
                elif dicc == 'Name' :
                        return "Rahul Gupta"
                elif dicc == 'Email Address' :
                        return "guptaraul89@gmail.com"
                elif dicc == 'Phone' :
                        return '201-895-3063'
                elif dicc == 'Position' :
                        return 'Data Engineer'
                elif dicc == 'Years' :
                        return '4+'
                elif dicc == 'Referrer' :
                        return 'Jenny Gasparis reached out to me via linkedin.'
                elif dicc == 'Degree' :
                        return 'Masters in Information System, Bachelor of Engineering in Information Technology'
                elif dicc == 'Resume' :
                        return 'https://www.linkedin.com/in/guptaraul/'
                elif dicc == 'Source' :
                        return 'https://github.com/guptaraul89/web_service/blob/master/service.py'
                elif dicc == 'Status' :
                        return 'Yes'
                elif dicc == 'Puzzle' :
                        return ' ABCD\nA=\nB=\nC=\nD='

run(host='185.75.1.178', port=8080)
