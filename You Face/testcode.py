##    if value=='':
##        redirect('/loginscreen')
##    f = open('feed-page.template','r')
##    lines = f.read()
##    feed= template.Template(lines)
##    data= {'updates':[],
##           'friends':[],
##           'name':name}
##    return feed.render(data)
  
##@post('/logout')
def logout():
    response.set_cookie('name', '', path='/')
    response.set_cookie('password', '', path='/')
    redirect('/')

    redirect('/')
