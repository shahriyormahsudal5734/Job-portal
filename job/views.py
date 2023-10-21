from .models import Job,Viloyat,Category,Apply_job,Message
from .filters import UserFilter
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def homepage(request):
    user_list = Job.objects.all().order_by('-id')
    viloyat =  Viloyat.objects.all()
    category =  Category.objects.all()
    user_filter =   UserFilter(request.GET, queryset=user_list)
   

    data = 'home'
    messages = Message.objects.all().order_by('-id')
    if request.method == 'POST':
        Message.objects.create(
        body=request.POST.get('body'),
        name=request.POST.get('name'),
        rating= request.POST.get('rating'),
        img= request.FILES.get('img55')
    )
        return redirect('/')

    return render(request, 'index.html',
{ 'user_filter1':user_filter, 'data':data, 'list':user_list , 'viloyat':viloyat,'category':category ,'messages':messages}
)

def likespage(request):
    data = 'lekis'
    
    user_list = Job.objects.all().order_by('-id')
    return render(request, 'job-list.html',{'posts':user_list,'data':data})


class Createjob(LoginRequiredMixin , CreateView):
    model = Job
    fields = ['title','body','pricemin','pricemax','manzil','phoneNumber','category5','viloyat5',]

    template_name = "about.html"
    success_url = '/'
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

def detail(request,id):
    job = Job.objects.get(id=id)

    applys = job.apply_job_set.all().order_by('-id')
    viloyatlar = Viloyat.objects.all()
    job.counter = applys.count()
    job.save()
    if request.method == 'POST':

        Apply_job.objects.create(
        categ=job,
        body=request.POST.get('body'),
        title=request.POST.get('title'),
        phoneNumber=request.POST.get('phoneNumber'),
        manzil=request.POST.get('manzil'),
        img= request.FILES.get('img'),
     
    )
        print(job.counter)


        return redirect('detail',id=job.id)


    return render(request,'job-detail.html',{'job':job,'applys':applys ,'viloyatlar':viloyatlar})


    
    

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('home')