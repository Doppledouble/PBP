# PENJELASAN TUGAS 4

**Link aplikasi Heroku TODOLIST Tugas 4 PBP** : https://appcijul.herokuapp.com/todolist/


**1. Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**

{% csrf_token %} pada elemen form berfungsi untuk membandingkan dua token yang terdapat pada sisi user dan pada sisi _request_. Digunakan untuk mengamankan data yang akan digunakan pada elemen form. Jika token CSRF dari server tidak sesuai dengan token yang dimiliki user atau user tidak mempunyai token, maka eksekusi request tidak akan dilakukan. Jika CSRF tidak ada di elemen form, maka input tidak akan dicek karena berarti bahwa input tersebut tidak aman. Biasa digunakan jika menggunakan method POST, karena method POST menampilkan informasi-informasi penting kepada user, berbeda dengan method GET yang mengembalikan informasi umum dan bersifat non-privat.

**2. Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.**

Pada dasarnya, kita bisa membuat elemen form secara manual. Cara yang bisa kita lakukan adalah dengan membuat tabel tersendiri dan menggunakan method POST pada elemen form juga menggunakan {% csrf_token %}. Secara garis besar,kita membuat elemen form dengan method POST terlebih dahulu lalu membuat table menggunakan <table>. Lalu, membuat tag tr didalamnya dan melengkapi beberapa atribut seperti deskripsi. Tag tr digunakan untuk sebagai wadah untuk input.

**3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

Pertama, user akan melakukan page request ke server, jika request merupakan request perdana, maka form akan dibuat kosong dengan value default dan ditampilkan pada user, data yang disubmisikan oleh user akan disimpan di database untuk request-request selanjutnya dan dapat diakes di dalam HTML jika ingin ditampilkan menggunakan method POST. Jika bukan pertama kali, maka form akan langsung memvalidasi data yang dimasukkan user, sehingga jika sesuai dengan data di database, maka data akan disave dan user akan diredirect ke page dengan data yang sesuai dengan yang direquest. Jika tidak valid, maka akan diredirect ke page pengisian form ulang. 

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. Membuat aplikasi dengan nama todolist, dengan melakukan perintah python manage.py startapp todolist pada cmd dan mendaftarkan aplikasi todolist ke dalam variabel INSTALLED_APPS pada settings.py project_django

2. membuat fungsi show_todolist dan mendaftarkan path dari todolist.urls pada urls.py di project_django

3. membuat sebuah model Task pada models.py dan membuat field user yang menggunakan ForeignKey, date menggunakan DateField, title dan description menggunakan TextField, dan is_finished menggunakan BooleanField.

4. Membuat method login, logout, dan register pada views dan juga template html untuk register dan login, yang kemudian fungsi views-views tersebut akan dipetakan ke template yang telah dibuat. Lalu saya menambahkan @login_required(login_url='/todolist/login/') agar setiap ingin mengakses website todolist maka user harus login dengan akun yang valid terlebih dahulu

5. Melalukan modifikasi pada todolist.html, mulai cara pengambilan data dan melakukan sinkronisasi terhadap fungsi masing-masing button

6. Membuat fungsi baru pada views.py yaitu add_task yang berfungsi untuk membuat form yang berisi judul dan deskripsi yang ingin ditambahkan. Data yang ditambahkan akan diupdate dan di save, dan dihungkan pada template html create-task

7. Melakukan routing terhadap seluruh fungsi views.py dengan membuat urls.py pada aplikasi todolist.

8. Melakukan git add,commit, dan push serta melakukan deployment ke heroku

9. Membuat 2 akun yang masing-masing akun berisikan 3 dummy data

Akun yang saya buat adalah :
1. username : IanIan, Password : dumdum123
2. username : yujin,  Password : hastaluego22



# PENJELASAN TUGAS 5

**1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**
Untuk Inline CSS karena dia menggunakan atribut <style> agar memberikan sebuah style kepada tag HTML tertentu, kekurangannya adalah jika ingin memberikan perubahan yang merata atau besar, maka inline CSS harus diterapkan pada setiap elemen yang ingin diubah. Namun kelebihannya, karena perubahan yang terjadi hanya di element tertentu, maka dapat digunakan untuk menguji atau melihat perubahan, berguna untuk perbaikan cepat, dan ukuran request HTTPnya lebih kecil.
Untuk internal CSS, biasa diletakkan di bagian <head> pada sebuah halaman HTML. Ini merupakan better practice dari inline CSS karena dapat merubah sekelompok element sekaligus, berbeda dengan inline yang harus diterapkan pada setiap element masing-masing. Opsi ini ideal untuk web yang hanya mempunyai 1 halaman HTML karena perubahan hanya terjadi di 1 halaman. Namun kekurangannya jika web mempunyai beberapa halaman dan kita ingin membuat perubahan pada semua halaman, maka kurang efisien karena jika kita ingin memakai CSS yang sama, maka perlu meng-upload file terlebih dahulu pada setiap halaman.
Untuk external CSS, opsi ini dikenal menjadi opsi yang paling nyaman untuk digunakan. Sama seperti internal, biasa diletakkan di bagian <head> halaman. Kelebihan dari external CSS adalah file CSS yang sama dapat digunakan di halaman-halaman lain, setelah itu kecepatan loading juga lebih cepat, dan ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapih. kekurangannya mungkin cukup sedikit dibandingkan yang lain, salah satunya adalah halaman belum tampil secaraa sempurna hingga file CSS selesai dipanggil.

**2. Jelaskan tag HTML5 yang kamu ketahui.**
terdapat <font> untuk menentukan font, warna, dan ukuran dari sebuah text. Ada <div> untuk membuat bagian-bagian pada halaman. <h1>-<h6> untuk mendefinisikan sebuah header dengan ukuran dari besar sampai kecil. <link> Mendefinisikan hubungan antara file dengan external resource.<script> Membuat script