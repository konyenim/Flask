# Flask
Membuat web_app
## Quick start flask
- Import flask
- Create object app = Flask
- Create app.route
- Definisikan isi
- Return 'hallo flask'
- Jalankan code pada localhost 0.0.0.0 debug=True
- Cek pada browser

## Using docker dan Docker-compose
- Create Dockerfile
- Tentuka sistem operasi yang akan kita kebangkan
- Tambahkan informasi admin/maintain
- Buat variabel ENV INSTALL_PATH dengan folder web_app
- Pastikan bahwasanya folder tersebut ada pada server
- Buat file requirements.txt
- Isi flask
- Kembali ke dockerfile copy requirements.txt
- Jalankan perintah pip untuk menginstall requirements.txt
- Copy semua file yang ada didalam web_app ke Istall app
- Buat directory web_app
- Pindahkan app.py ke directory web_app
- Tambahkan gunicorn pada requirements.txt
- Perintahkan CMD untuk menambahkan server yang dipakai pada docker file dengan menggunakan gunicorn
- Alamat internet 8000
- Buat file docker-compose.yml
- Tentukan versi docker-compose yang dipakai
- Atur services web_app
- Jalankan services dengan perintah gunicorn yang ada pada docker file dengan tambahan perintah reload
- Pastikan bahwa semua output python langsung dikirim pada konsole dengan perintah PYTHONUNBUFFERED jadikan true
- Tentukan volumes
- Pastikan ports
- Jalankan dengan perintah sudo docker-compose up --build