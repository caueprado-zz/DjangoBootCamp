from django.shortcuts import render
from evolution_app.models import Cliente
from evolution_app.forms import Login, NewUser, FormName


# Create your views here
def index(request):
    my_dict = {'value': "wpg_list"}
    return render(request, 'index.html', context=my_dict)


def test(request):
    return render(request, 'test.html')


def help(request):
    wpg_list = Cliente.objects.order_by('nome')
    wpg_dict = {'access_record': wpg_list}
    return render(request, 'help.html', context=wpg_dict)


def login(request):
    form = Login()
    return render(request, 'login.html', {'form': form})


def new_user(request):
    user = NewUser()
    if request.method == "POST":
        user = NewUser(request.POST)
        if user.is_valid():
            user.save(commit=True)
            return index(request)
        else:
            print('ERROR')
    return render(request,
                  'cadastro.html',
                  {"form": user}
                  )


def form(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request, 'form.html', {'form': form})
