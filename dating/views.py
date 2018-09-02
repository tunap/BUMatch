from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import UserForm
from .models import *
import math

gachi_query = [["0","What would you do if you were supernatural"], ["1","What would you do if the person you met at Lemon Melon was the ex-girlfriend of a close friend?"], ["2","What would you do if you won the lottery?"]]
favor_query = [["0","Lemon", "Melon"],["1","소주", "맥주"],["2","켄즈", "핀토스"],["3","치킨", "피자"],["4","Extrovert", "Introvert"],["5","Football", "Baseball"],["6","Yolk", "White"],["7","트와이스", "레드벨벳"],["8","칙촉", "홈런볼"],["9","버거킹", "맘스터치"],["10","ACK", "SYNACK"],["11","태진아", "엑소"],["12","노래방가서 스마트폰 만지기", "노래방에서 노래부르기"],["13","그랑", "책다방"],["14","롯데리아", "서브웨이"],["15","ㅇㅅㅇ", "ㅇㅂㅇ"],["16","왕비성", "닭칼"],["17","오라우", "두메"],["18","폰노이만", "아인슈타인"],["19","서울 되기", "소울 되기"]]

# Create your views here.

def index_new(request):
    return render(request, 'dating/index_new.html', {})

def site_info(request):
    if not request.session.get('member_id',False):
        return render(request, 'dating/site_info_logoff.html', {})
    else:
        user_id = request.session['member_id']
        my_user = User.objects.filter(user_id=user_id).first()
        return render(request, 'dating/site_info_logon.html', {'my_user':my_user})

def index(request):
    if not request.session.get('member_id',False):
        return render(request, 'dating/index_logoff.html', {})
    else:
        return render(request, 'dating/index_logon.html', {})

def login(request):
    if not request.session.get('member_id',False):
        return render(request, 'dating/login.html', {})
    else:
        return render(request, 'dating/error.html',{'error_message':"You've already logined!"})

def logout(request):
    if not request.session.get('member_id',False): # not login
        return render(request, 'dating/error.html',{'error_message':"You are not logined yet!"})
    else:
        del request.session['member_id']
        return redirect('index')

def login_sent(request):
    try:
        m = User.objects.get(user_login_id=request.GET['email'])
    except User.DoesNotExist:
        return render(request, 'dating/error.html',{'error_message':"You do not have an ID????????"})
    if m.user_login_pw == request.GET['password']:
        request.session['member_id']=m.user_id
        return redirect('index')
    else:
        return render(request, 'dating/error.html',{'error_message':"Wrong password"})

def join(request):

    if request.method == "POST":
        form = UserForm(request.POST)

        if len(User.objects.filter(user_name=request.POST["user_name"]))!=0:
            return render(request, 'dating/error.html',{'error_message':"Same ID exists...So sorry to hear that..."})

        user = User(user_name = request.POST["user_name"], user_my_gender = request.POST["user_my_gender"], user_ur_gender= request.POST["user_ur_gender"], user_description = request.POST["user_description"], user_phone_no = request.POST["user_phone_no"], user_login_id = request.POST["user_login_id"], user_login_pw = request.POST["user_login_pw"])

        user.save()

        for i in range(len(favor_query)):
            favor = Favor(user_id = user.user_id, favor_id = i, favor_value=request.POST["favor_"+str(i)])
            favor.save()

        for i in range(len(gachi_query)):
            gachi = Gachi(user_id = user.user_id, gachi_id = i, gachi_value=request.POST["gachi_"+str(i)])
            gachi.save()

        update_match_when_join(user)
        return redirect('join_done')
    else:
        form = UserForm()
    return render(request, 'dating/join.html', {'favor_query': favor_query, 'gachi_query': gachi_query, 'form': form})

def join_done(request):
    user = User.objects.last()
    return render(request, 'dating/join_done.html', {'user':user})

def match(request):
    user_id = request.session['member_id']
    my_user = User.objects.filter(user_id=user_id).first()
    if request.method=="POST":
        match_found=Match.objects.filter(user_id_stt=user_id,user_id_end=request.POST["other_user_id"]).first()
        match_found.is_watched=True
        if "pick" in request.POST:
            match_found.is_picked=True
        elif "next" in request.POST:
            match_found.is_picked=False
        match_found.save()

    match_found = Match.objects.filter(user_id_stt=user_id,is_watched=False).order_by('-score').first()
    disab=""
    if match_found==None:
        return render(request, 'dating/error_match.html',{'error_message':"There are no more people!", 'my_user':my_user})
    elif len(Match.objects.filter(user_id_stt=user_id,is_watched=False).order_by('-score')) == 1:
        disab="disabled"

    score = match_found.score
    user = User.objects.filter(user_id=match_found.user_id_end).first()
    gachi_answer = Gachi.objects.filter(user_id=match_found.user_id_end)
    gachi = []
    for i in range(len(gachi_query)) :
        gachi.append([gachi_query[i][1],gachi_answer[i].gachi_value])

    return render(request, 'dating/match.html', {'gachi_query': gachi_query, 'gachi_answer': gachi_answer, 'gachi':gachi, 'score':score, 'user':user,'disabled':disab, 'my_user':my_user})

def mypage(request):
    return render(request, 'dating/mypage.html', {})


def get_corr(user_id1,user_id2):
    user1_favs=list(Favor.objects.filter(user_id=user_id1).order_by('favor_id'))
    user2_favs=list(Favor.objects.filter(user_id=user_id2).order_by('favor_id'))
    res=get_cosine_corr(user1_favs,user2_favs) # out of 100
    return res
def get_cosine_corr(l1,l2):
    sumval=0
    size1=0
    size2=0
    for i in l1:
        size1+=i.favor_value*i.favor_value
    for i in l2:
        size2+=i.favor_value*i.favor_value
    size1=math.sqrt(size1)
    size2=math.sqrt(size2)
    for i in range(len(l1)):
        sumval=sumval+(l1[i].favor_value*l2[i].favor_value)
    ret=(sumval/(size1*size2))*100
    ret=int(ret)
    return ret

def update_match_when_join(user):
    matchable=[]
    #consider other's gender orientation
    if(user.user_my_gender=="0"):
        matchable=list(set(User.objects.filter(user_ur_gender=0)) | set(User.objects.filter(user_ur_gender=2)))
    elif(user.user_my_gender=="1"):
        matchable=list(set(User.objects.filter(user_ur_gender=1)) | set(User.objects.filter(user_ur_gender=2)))
    else:
        matchable=list(User.objects.filter(user_ur_gender=2))
    (matchable)
    for u in matchable:
        if u.user_id!=user.user_id and (user.user_ur_gender == str(u.user_my_gender) or user.user_ur_gender == "2"):
            corr=get_corr(u.user_id,user.user_id)
            a=Match(user_id_stt=u.user_id,user_id_end=user.user_id,is_watched=False,score=corr,is_picked=False)
            a.save()
            b=Match(user_id_stt=user.user_id,user_id_end=u.user_id,is_watched=False,score=corr,is_picked=False)
            b.save()

def hooray(request):
    my_id = request.session['member_id']
    my_user = User.objects.filter(user_id=my_id).first()
    matched=[]
    for user in User.objects.all():
        a=Match.objects.filter(user_id_stt=my_id,user_id_end=user.user_id,is_picked=True).first()
        b=Match.objects.filter(user_id_stt=user.user_id,user_id_end=my_id,is_picked=True).first()
        if a!=None and b!=None:
            matched.append([user,a.score])
    matched.sort(key=lambda a:a[1])
    seq_num=0

    if request.method == "POST":
        seq_num=int(request.POST['seq_num'])

    disab_left=""
    disab_right=""
    print(seq_num,len(matched))
    if seq_num>=len(matched):
        return render(request, 'dating/error_match.html',{'error_message':"없는데 오또카지?", 'my_user':my_user})
    if seq_num==len(matched)-1:
        disab_right="disabled"
    if seq_num<=0:
        disab_left="disabled"
    user=User.objects.get(user_id=matched[seq_num][0].user_id)
    gachi_answer = Gachi.objects.filter(user_id=matched[seq_num][0].user_id)
    gachi = []
    for i in range(len(gachi_query)) :
        gachi.append([gachi_query[i][1],gachi_answer[i].gachi_value])

    return render(request, 'dating/hooray.html', {'gachi_query': gachi_query, 'gachi_answer': gachi_answer, 'gachi':gachi, 'score':matched[seq_num][1], 'user':user,'disabled_left':disab_left,'disabled_right':disab_right,'seq_num':seq_num, 'my_user':my_user})


def please(request):

    user_id = request.session['member_id']
    my_user = User.objects.filter(user_id=user_id).first()
    if request.method=="POST":
        match_found=Match.objects.filter(user_id_stt=user_id,user_id_end=request.POST["other_user_id"]).first()
        match_found.is_watched=True
        if "pick" in request.POST:
            match_found.is_picked=True
        elif "next" in request.POST:
            match_found.is_picked=False
            print("here")
        match_found.save()

    picked_by_other=list(Match.objects.filter(user_id_end=user_id,is_picked=True).order_by('score'))
    match_found=None
    for m in picked_by_other:
        temp=Match.objects.get(user_id_end=m.user_id_stt,user_id_stt=m.user_id_end)
        if not temp.is_watched:
            match_found=temp
            break
    if match_found==None:
        return render(request, 'dating/error_match.html',{'error_message':"요청이 없는데여? 분발하자!", 'my_user':my_user})
    score = match_found.score
    user = User.objects.filter(user_id=match_found.user_id_end).first()
    gachi_answer = Gachi.objects.filter(user_id=match_found.user_id_end)
    gachi = []
    for i in range(len(gachi_query)) :
        gachi.append([gachi_query[i][1],gachi_answer[i].gachi_value])

    return render(request, 'dating/please.html', {'gachi_query': gachi_query, 'gachi_answer': gachi_answer, 'gachi':gachi, 'score':score, 'user':user, 'my_user':my_user})

def mypage(request):

    user_id = request.session['member_id']
    my_user = User.objects.filter(user_id=user_id).first()

    gachi_answer = Gachi.objects.filter(user_id=user_id)
    gachi = []
    for i in range(len(gachi_query)) :
        gachi.append([gachi_query[i][1],gachi_answer[i].gachi_value])

    if my_user.user_my_gender == 0 :
        my_gender = "Female"
    elif my_user.user_my_gender == 1 :
        my_gender = "Male"
    else : my_gender = "Other"

    if my_user.user_ur_gender == 0 :
        ur_gender = "Female"
    elif my_user.user_ur_gender == 1 :
        ur_gender = "Male"
    else : ur_gender = "Other"

    return render(request, 'dating/mypage.html', {'gachi':gachi, 'my_user':my_user, 'my_gender':my_gender, 'ur_gender':ur_gender})
