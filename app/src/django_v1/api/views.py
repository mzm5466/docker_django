from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from .models import BasicUser,BasicEmail
from django.http import JsonResponse
import random,datetime
# Create your views here.
def send_email(request):
    email = request.GET.get("email")
    send_mail(subject="demo_test",message="hello world",\
              from_email="收件人邮箱",\
              recipient_list=[email], \
              fail_silently = False
    )
    return HttpResponse("OK!")
def send_email_by_code(request):
    code = random.randint(1000,9999)
    email = request.GET.get("email")
    try:
        check_email_code=BasicEmail.objects.filter(email=email).order_by("-createTime")[0]
    except Exception as e:
        BasicEmail.objects.create(code=code, email=email)
        send_mail(subject="demo_test", message=("您的验证码为%d" % code), \
                  from_email="发件人邮箱", \
                  recipient_list=[email], \
                  fail_silently=False
                  )
        return JsonResponse({'status': 200, 'data': '邮箱验证码已经发送'})
    if check_email_code:
        nowTime=datetime.datetime.now()
        lastTime=check_email_code.createTime
        timeS = int((nowTime-lastTime).total_seconds())
        if timeS>10:
            BasicEmail.objects.create(code=code,email=email)
            send_mail(subject="demo_test", message=("您的验证码为%d" % code), \
                      from_email="收件人邮箱", \
                      recipient_list=[email], \
                      fail_silently=False
                      )
            return JsonResponse({'status': 200, 'data': '邮箱验证码已经发送'})
        else:
            return JsonResponse({'status': 205, 'data': '您操作过于频繁'})
def register(request):
    #获取get请求的参数 拼url
    phone = request.GET.get("phone")
    email = request.GET.get("email")
    password = request.GET.get("password")
    qianduan_code = request.GET.get("code",0)
    # register/?phone=13359707473&email=1107771338@qq.com&password=123456&code=0
    '''
    判断注册用户的注册信息是否唯一
    '''
    if BasicUser.objects.filter(phone=phone,email=email):
        return HttpResponse("手机号+邮箱都存在")
    else:
        check_info_phone=BasicUser.objects.filter(phone=phone)
        if check_info_phone: #判断有没有账户#校验是否存在该用户
            return HttpResponse("该手机号已经存在，请更换手机号注册")
        check_info_email = BasicUser.objects.filter(email=email)
        if check_info_email:  # 判断有没有账户#校验是否存在该用户
            return HttpResponse("该邮箱已经存在，请更邮箱号注册")
    # 判断状态码是否输入
    if int(qianduan_code) != 0:
        #判断是否是发送过验证码的邮箱
        try:
            code = BasicEmail.objects.filter(email=email).order_by("-createTime")[0]
        except:
            return JsonResponse({'status': 208, 'data': '您还未发送验证码邮件'})
        #验证邮箱验证码5分钟有效
        nowTime = datetime.datetime.now()
        lastTime = code.createTime
        timeS = int((nowTime - lastTime).total_seconds())
        if timeS > 300:
            return JsonResponse({'status': 205, 'data': '验证码已经失效!'})
        else:
            #验证通过
            if code.code == int(qianduan_code):
                BasicUser.objects.create(phone=phone,email=email,password=password)
                return JsonResponse({'status': 200, 'data': '注册成功!'})
            else:
                #验证不通过
                return JsonResponse({'status': 207, 'data': '验证码无效!'})
    else:
        return JsonResponse({'status': 206, 'data': '验证码没有输入!'})