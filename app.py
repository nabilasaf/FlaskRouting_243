from flask import Flask, redirect, url_for, request, render_template  # Mengimpor kelas dan fungsi yang diperlukan dari Flask
app = Flask(__name__)  # Membuat instance dari aplikasi Flask

@app.route('/success/<name>')  # Mendefinisikan rute untuk URL '/success' dengan parameter 'name'
def success(name):  # Fungsi yang akan dipanggil ketika rute ini diakses
   return f'welcome {name}'  # Mengembalikan pesan sambutan yang menyertakan nama pengguna

@app.route('/login', methods=["GET", 'POST'])  # Mendefinisikan rute untuk URL '/login' yang menerima metode GET dan POST
def loginGET():  # Fungsi yang akan dipanggil ketika rute ini diakses
    if(request.method == "POST"):  # Memeriksa apakah metode permintaan adalah POST
         user = request.form['nm']  # Mengambil data dari form dengan nama 'nm'
         return redirect(url_for('success', name=user))  # Mengalihkan pengguna ke rute 'success' dengan nama pengguna sebagai parameter
@app.route("/")
def homr():
   return render_template('index.html')  # Merender template 'index.html' jika metode permintaan adalah GET

if __name__ == '__main__':  # Memeriksa apakah file ini dijalankan sebagai program utama
   app.run(debug=True)  # Menjalankan aplikasi Flask dalam mode debug
