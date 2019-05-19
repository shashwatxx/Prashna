from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from uttar.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from uttar.serializers import *
from uttar.permissions import *

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

@login_required
def like(request): 
    ans = Answer.objects.get(pk=request.POST.get("aid"))
    Like.objects.create(answer=ans, like_by=request.user)
#     return render(request, "contact.html")
    return redirect("/prashna/question/"+ request.POST.get("qid")+"/")

@method_decorator(login_required, name='dispatch')
class QuestionCreate(CreateView):
        model = Question
        fields = ("question", "attach1", "topic")
        success_url ="/prashna/"
        def form_valid(self, form):
                form.instance.ask_by = self.request.user
                return super(QuestionCreate, self).form_valid(form)        
#         def get_context_data(self, **kwargs):
#             ctx = CreateView.get_context_data(self, **kwargs)
#             ctx['actCreate'] = 'active'
#             return ctx        


@method_decorator(login_required, name='dispatch')
class AnswerCreate(CreateView):
        model = Answer
        fields = ("answer", "attach1")
        success_url ="/prashna/question/"
        def form_valid(self, form):
                form.instance.ans_by = self.request.user
                q = Question.objects.get(pk=self.request.GET.get("qid"))
                q.status = 'answered'
                q.save()
                form.instance.question = q
                return super(AnswerCreate, self).form_valid(form)        

class QuestionList(ListView):
        model = Question
        def get_queryset(self):
            si = self.request.GET.get('si')
            if si==None:
                si=''        
            return Question.objects.all().filter(question__icontains = si).order_by('-id')        


class QuestionDetails(DetailView):
        model = Question
        def get_context_data(self, **kwargs):
            ctx = DetailView.get_context_data(self, **kwargs)
            ctx["answers2"] = Answer.objects.all().filter(question = ctx["object"])
            ans = []
            for a1 in ctx["answers2"]:
                d1 = {}
                d1["ans"] = a1;              
                likes = Like.objects.all().filter(answer = a1)
                uLiked =False
                for L1 in likes:              
                    if L1.like_by == self.request.user:
                        uLiked = True
                d1["likes"] = likes;
                d1["uLiked"] = uLiked;
                ans.append(d1)
            ctx["answers2"] = ans                
            return ctx        
        
# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-id')
    serializer_class = QuestionSerializer
    def get_queryset(self):
            si = self.request.GET.get('si')
            if si==None:
                si=''   
            return Question.objects.all().filter(question__icontains = si).order_by('-id')           
    permission_classes= (MyObjPer,)

# Create your views here.
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('-id')
    serializer_class = AnswerSerializer
    permission_classes= (MyObjPer,)

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all().order_by('-id')
    serializer_class = LikeSerializer
    permission_classes= (MyObjPer,)


# Create your views here.
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('-id')
    serializer_class = TopicSerializer
    permission_classes= (MySuperOrReadOnlyPers,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes= (MyUserPers,)

