# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    user_text=request.GET['text']  #获取用户输入的文本
    total_count=len(user_text)
    word_dict={}
    # 通过循环求出每个字符出现的次数
    for word in user_text:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    #给字典排序
    sort_dict=sorted(word_dict.items(),key=lambda w:w[1],reverse=True)
    # 在count.html中 ----->   通过字典  获得总字数 文本信息  每个字出现的次数
    return render(request, 'count.html', {'count': total_count,'text':user_text,'wordict':word_dict,'sorted':sort_dict})
