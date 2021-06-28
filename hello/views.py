from django.http import HttpResponse


def myview(request):

    if 'dj4e_cookie' in request.COOKIES:

        oldval = request.COOKIES.get('cookie')
        oldval = str(int(oldval)+1)
        resp = HttpResponse("view count="+(oldval))
        resp.set_cookie('cookie',str(oldval))

    else:
        oldval = 1
        resp = HttpResponse("view count="+str(oldval))
        resp.set_cookie('cookie',str(oldval))

    resp.set_cookie('dj4e_cookie', value='b99c61ac', max_age=10)
    return resp



    # if oldval :
    #     resp.set_cookie('dj4e_cookie', int(oldval)+1) # No expired date = until browser close
    # else :
    #     resp.set_cookie('dj4e_cookie', 42) # No expired date = until browser close
    #     resp.set_cookie('dj4e_cookie', 'b99c61ac', max_age=1000) # seconds until expire
    # return resp

    # https://www.youtube.com/watch?v=Ye8mB6VsUHw

#def sessfun(request) :
#    num_visits = request.session.get('num_visits', 0) + 1
#    request.session['num_visits'] = num_visits
#    if num_visits > 4 : del(request.session['num_visits'])
#    resp = HttpResponse('view count='+str(num_visits))
#    return resp


# def myview(request):
#     print(request.COOKIES)
#     old_value = request.COOKIES['num_views',0]
#     return HttpResponse("num_views = "+str(old_value))








