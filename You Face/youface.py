from bottle import get, post, run, request, response
from bottle import redirect, debug, static_file
import xmlrpclib
import template

DB_ADDRESS = 'http://youface.cs.dixie.edu/'
DB_SERVER = None

title = "CodyFace"
subtitle = "like Facebook only not as good!"
links = [
    { 'href': 'http://cit.cs.dixie.edu/cs/cs1410/',     'text': 'CS 1410' },
    { 'href': 'http://codrilla.cs.dixie.edu/',          'text': 'Codrilla' },
    { 'href': 'http://new.dixie.edu/reg/syllabus/',     'text': 'College calendar' },
]

@get('/youface.css')
def stylesheet():
    return static_file('youface.css', root='./')

@get('/loginscreen')
def loginscreen():
##    return 'Hello'
    f = open('login-page.template','r')
    lines = f.read()
    t= template.Template(lines)
    data= {'title':title,
           'subtitle':subtitle,
           'links':links}
    return t.render(data)
 
@post('/login')
def login():
##    return 'Does it work?'
    name = request.forms.get('name')
    password = request.forms.get('password')
    type1 = request.forms.get('type')
##    s=name+password+type1
    if type1=='Create':
        (status, message) = DB_SERVER.newUser(name, password)
    if type1=='Delete':
        (status, message) = DB_SERVER.deleteUser(name, password)
    response.set_cookie('name', name, path='/')
    response.set_cookie('password', password, path='/')
    redirect('/')
##    return s

@get('/')
def feedPage():
    name= request.COOKIES.get('name', '')
    password= request.COOKIES.get('password', '')
    (status, message)= DB_SERVER.listFriends(name, password)
    if status=='failure':
        redirect('/loginscreen')
    (status2, message2)= DB_SERVER.listStatusFriends(name, password, 25)
    if status2=='failure':
        redirect('/loginscreen')
    friends=[]
    for i in message:
        lst={'name':i}
        friends.append(lst)
    status=[]
    for i in message2:
        lst={'status':i}
        status.append(lst)
    f = open('feed-page.template','r')
    lines = f.read()
    t= template.Template(lines)
    data= {'title':title,
           'subtitle':subtitle,
           'name': name,
           'updates':status,
           'friends':friends,
           'links':links}
    return t.render(data)

@get('/friend/:fname')
def friend(fname):
    name= request.COOKIES.get('name', '')
    password= request.COOKIES.get('password', '')
    (status, message)= DB_SERVER.listFriends(name, password)
    if status=='failure':
        redirect('/loginscreen')
    (status2, message2)= DB_SERVER.listStatusUser(name, password, fname, 25)
    if status2=='failure':
        redirect('/loginscreen')
    friends=[]
    for i in message:
        lst={'href':'http://localhost:8080/friend/'+i, 'name':i}
        friends.append(lst)
    status=[]
    for i in message2:
        lst={'status':i}
        status.append(lst)
    f = open('friend-page.template','r')
    lines = f.read()
    t= template.Template(lines)
    data= {'title':title,
            'subtitle':subtitle,
            'friend': fname,
            'updates':status,
            'friends':friends,
            'links':links}
    return t.render(data)  

@post('/status')
def status():
    name= request.COOKIES.get('name', '')
    password= request.COOKIES.get('password', '')
    status = request.forms.get('status')
    (status2, message)= DB_SERVER.setStatus(name, password, status) 
    redirect('/')
    
@post('/addfriend')
def addfriend():
    name= request.COOKIES.get('name', '')
    password= request.COOKIES.get('password', '')
    addfriend = request.forms.get('name')
    (status, message)= DB_SERVER.addFriend(name, password, addfriend) 
    redirect('/')
   
@post('/unfriend')
def unfriend():
    name= request.COOKIES.get('name', '')
    password= request.COOKIES.get('password', '')
    unfriend = request.forms.get('name')
    (status, message)= DB_SERVER.unFriend(name, password, unfriend) 
    redirect('/')
    
@post('/logout')
def logout():
    response.set_cookie('name', '', path='/')
    response.set_cookie('password', '', path='/')
    redirect('/')  

def main():
    global DB_SERVER, DB_ADDRESS

    print 'Using YouFace server at', DB_ADDRESS
    DB_SERVER = xmlrpclib.ServerProxy(DB_ADDRESS, allow_none=True)
    debug(True)
    run(host='localhost', port=8080, reloader=True)

if __name__ == '__main__':
    main()
