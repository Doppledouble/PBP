# Tugas 6: Javascript dan AJAX


### Deployment Heroku
[Link Heroku TUGAS 6](https://appcijul.herokuapp.com/todolist/json)

#

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Jawab:

Perbedaan dari synchronous dan asynchronous adalah jika synchronous ketika user melakukan request, maka untuk request atau task selanjutnya harus menunggu task sebelumnya untuk selesai terlebih dahulu, karena itu, synchronous programming dianggap lebih tidak efisien dan bisa membuat program freeze. Sedangkan asynchronous programming, kita dapat melakukan request berulang kali dan server akan melakukan task-task tersebut secara terpisah tanpa menunggu selesainya task-task yang lain. Asynchronous programming akan terus berjalan tanpa akan adanya freeze.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini
Jawab:

Event-Driven Programming merupakan programming yang alurnya ditentukan oleh suatu event. Secara gambaran besar, event-driven programming mungkin dapat dilihat mirip dengan pengaplikasian asynchronous programming yang tidak berurutan atau independent. Salah satu contoh penerapannnya adalah ketika user mengklik tombol create-task, ketika tombol tersebut diklik, maka terbuatlah sebuah event untuk user membuat task baru dengan user menampilkan form untuk detail dari task tersebut.
### Jelaskan penerapan asynchronous programming pada AJAX
Jawab:

AJAX adalah singkatan dari Asynchoronous JavaScript and XMLHTTP merupakan salah satu konsep yang memproses HttpRequest dan server akan merespon dan mengembalikan data dalam bentuk XML ataupun JSON ke browser, setelah itu diproses menggunakan javaScript secara asynchronous dan dikembalikan ke user.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
Jawab:

AJAX GET

Pertama-tama, saya menambahkan 2 function pada views yang berguna untuk mengambil data BarangToDoList dalam bentuk json dan menampilkannya. Saya juga menambahkan path pada urls.py agar function di views dapat direcall di HTML. 

```
# TODOLIST AJAX
@login_required(login_url='/todolist/login/')
def todolist_ajax(request):
    ajax_todolist = BarangToDoList.objects.filter(user=request.user)
    context = {
    'ajax_todolist' : ajax_todolist,
    'username' :  request.user.username,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist_ajax.html", context)

# AJAX GET
def get_todolist_json(request):
    data_ajax = BarangToDoList.objects.filter(user=request.user)

    return HttpResponse(serializers.serialize("json", data_ajax), content_type="application/json")

```
    path('json/', todolist_ajax, name='show_json'),
    path('get_todolist_json/', get_todolist_json, name='get_todolist_json'),
   
#

AJAX POST

Setelah itu saya menambahkan function add di views yang berguna untuk menambahkan task di todolist_ajax. Di situ juga berbeda dengan create-task yang sebelumnya karena sekarang add bukan memindahkan user ke page create-task melainkan memunculkan modal. Saya juga menambahkan path add ke dalam urls.py. Di sinilah asynchronous programming diterapkan di mana event yang dimulai oleh add tidak bergantung dengan reques-request yang lain.
```
# ADD TASK MODAL
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        BarangToDoList.objects.create(title=title, description=description, date=date, user=user)
         
        return HttpResponse(b"CREATED", status=201)

```

Setelah itu saya membuat HTML baru yang bernama todolist_ajax yang di situ juga saya mengimport Jquery Ajax yaitu "<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>".