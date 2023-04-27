from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
# 存服务器端的函数


def index(request):
    return render(request, "web.html")


def getinfo(request):
    data = request.GET
    x0 = data.get('x0')
    y0 = data.get('y0')
    x1 = data.get('x1')
    y1 = data.get('y1')
    w = data.get('w')
    h = data.get('h')
    levelIdx = data.get('levelIndex')

    # add some stupid operations
    cntSubTar = data.get('cnt_st')
    xx0 = data.get('xx0')
    yy0 = data.get('yy0')
    xx1 = data.get('xx1')
    yy1 = data.get('yy1')
    xx2 = data.get('xx2')
    yy2 = data.get('yy2')
    print(cntSubTar)
    # TODO: here you got the information you want, you should do your algorithm job, modify the file name of png
    #  in the following line, the `.png` file is that the picture show your algorithm results. "testpic3.png" => ?

    sent_img_path = "./static/image/" + "testpic3.png"
    return JsonResponse({
        'result': "success",
        'img': sent_img_path,
    })


def getimg(request):
    data = request.GET
    filename = data.get('file')

    # TODO: choose your `.png` file corresponding to the selected `.dsn` file. You firstly generate the `.png`,
    #  and store it into ./static/image, then you justify the file name in the following line, "testpic2.png" => ?
    sent_img_path = "./static/image/" + "testpic2.png"
    return JsonResponse({
        'result': "success",
        'img': sent_img_path,
    })


def saveres(request):
    data = request.GET
    x = data.get('x')

    # TODO: you should save your algorithm result here, write your code.

    return JsonResponse({
        'result': "success",
    })