from django.shortcuts import render

# Create your views here.
# /index/
def index(request):
    # context = {'city': '深圳'}
    context = {
        'city': '北京',
        'adict': {
            'name': '西游记',
            'author': '吴承恩'
        },
        'alist': [1, 2, 3, 4, 5],
        'html_str': '<a href=https://www.baidu.com>百度一下</a>'
    }
    return render(request, 'index.html', context)
