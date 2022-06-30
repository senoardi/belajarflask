from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
	namaUser = ""
	if request.method == 'POST':
		namaUser =  "Namamu adalah " + request.form['name']
	return render_template('register.html', namaUser = namaUser)








# @app.route('/nama/<namanya>')
# def cetakNama(namanya):
# 	pesan = "Nama anda adalah : " + namanya
# 	return pesan

if __name__ == '__main__':
    app.run(
    	host='0.0.0.0',
    	debug = True
    	)