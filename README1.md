1.

2.
Tujuan dasar penggunaan Virtual environment ketika membuat sebuah Web-Based app adalah untuk melengkapi beberapa ketergantungan yang dibutuhkan oleh project-project
yang berbeda dengan membuat sebuah wadah yang terisolasi untuk project itu sendiri. Contoh konkretnya adalah ketika kita sedang membuat sebuah project web, namun 
kedua project tersebut menggunakan django dengan versi yang berbeda, sehingga di situlah virtual environment dapat berguna untuk melengkapi kebutuhan kedua project.
3.
### views.py
pada file views.py saya hanya menambahkan beberapa data dengan
menginisiasi nama dan npm di dalam sebuah dictionary bernama context yang berada di fungsi show_katalog yang nantinya fungsi ini akan dipanggil di katalog.html
### urls.py
Pada file urls.py yang terdapat di folder project_django berguna untuk menghubungkan file itu sendiri ke file urls.py di folder katalog, karena file urls.py di folder katalog memanggil fungsi show_katalog 
yang akan ditampilkan nantinya.
### katalog.html
Pada file katalog.html, terdapat beberapa pengambilan key dengan data yang terdapat di views.py di folder katalog. Setelah itu,terdapat pemanggilan loop
pada list_barang dari key list_barang di views.py dan memanggil variable dari class CatalogItem di file models.py di folder katalog.
### deploy
Implementasi deploy adalah dengan cara menghubungkan akun github dengan akun heroku terlebih dahulu, setelah itu membuat beberapa _secrets_ di github dengan 
membuat beberapa 2 variable, yaitu HEROKU_API_KEY dan HEROKU_APP_NAME dengan mencantumkan API KEY ke variable pertama dan nama app yang sudah dinamakan ke variable kedua.
Setelah itu, pada bagian actions di repository, kembali menjalankan semua failed files sampai proses deployment berhasil.
