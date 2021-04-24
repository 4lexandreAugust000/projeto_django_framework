from django.shortcuts import render, redirect, HttpResponseRedirect
from musica.forms import MusicaForm
from artista.forms import ArtistaForm
from musica.models import Musica
from artista.models import Artista
from django.http import HttpResponse
from musica.models import Login_artista
import xlwt

# Create your views here.  

# definindo a view que permite o usuário adicionar um novo registro
def addnew(request):  
    if request.method == "POST":  
        form = MusicaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = MusicaForm()  
    return render(request,'index.html',{'form':form})  
def index(request):  
    musicas = Musica.objects.all()  
    return render(request,"show.html",{'musicas':musicas})

# definindo a view que permite o usuário editar um registro
def edit(request, id):  
    musica = Musica.objects.get(id=id)  
    return render(request,'edit.html', {'musica':musica}) 
# definindo a view que permite o usuário atualizar um registro 
def update(request, id):  
    musica = Musica.objects.get(id=id)  
    form = MusicaForm(request.POST, instance = musica)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'musica': musica})
# definindo a view que permite o usuário deletar um registro
def destroy(request, id):  
    musica = Musica.objects.get(id=id)  
    musica.delete()  
    return redirect("/")  

# definindo a view que permite o usuário exportar todos os dados cadastrados em formato '.xls'
def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="listademusicas.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # cabeçalho da folha
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Titulo', 'Duração', 'Spotify', 'Youtube', 'Artista' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Corpo da folha, linhas restantes
    font_style = xlwt.XFStyle()

    rows = Musica.objects.all().values_list('titulo', 'duracao', 'spotify', 'youtube', 'artista')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

# definindo a view que permite o artista se cadastrar, indo até o login e de fato entrando no CRUD de musicas e com a opção de exportar

def index_login(request):
    if request.method == 'POST':
        login_artista = Login_artista(usuario=request.POST['usuario'], senha=request.POST['senha'],  nome=request.POST['nome'], sobrenome=request.POST['sobrenome'])
        login_artista.save()
        return redirect('/')
    else:
        return render(request, 'index_login.html')

def login(request):
    return render(request, 'login.html')

# definindo a view que permite o usuário logar no seu admin
def home(request):
    if request.method == 'POST':
        if Login_artista.objects.filter(usuario=request.POST['usuario'], senha=request.POST['senha']).exists():
            login_artista = Login_artista.objects.get(usuario=request.POST['usuario'], senha=request.POST['senha'])
            return render(request, 'show.html', {'login_artista': login_artista})
        else:
            context = {'msg': 'Os dados inseridos estão errados'}
            return render(request, 'login.html', context)
