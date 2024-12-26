from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object("config.Config")

mysql = MySQL(app)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
  os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'avif'}

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/breeds")
def breeds():
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM cat")
  cats = cur.fetchall()
  return render_template("breeds.html", cats=cats)

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/crud", methods=['GET'])
def crud():
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM cat")
  cats = cur.fetchall()
  return render_template("crud.html", cats=cats)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    name = request.form['name']
    desc = request.form.get('desc', '')
    image = request.files['image']

    if name == '' or not name:
      flash('Nama tidak boleh kosong', 'danger')
      return redirect(request.url)
    if 'image' not in request.files:
      flash('No file part in the request', 'danger')
      return redirect(request.url)
    if image.filename == '':
      flash('No selected file', 'danger')
      return redirect(request.url)
    if not allowed_file(image.filename):
      flash('File type not allowed. Only PNG, JPG, JPEG, and GIF are allowed.', 'danger')
      return redirect(request.url)
    
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO cat (`name`, `desc`, `image_url`) VALUES (%s, %s, %s);", (name, desc, filename))
        mysql.connection.commit()
        flash('Data berhasil ditambahkan!', 'success')
        return redirect(url_for('crud'))

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM cat WHERE id = %s", (id,))
    data = cursor.fetchone()

    if not data:
      flash('Data tidak ditemukan', 'danger')
      return redirect(url_for('breeds'))

    if request.method == 'GET':
        return render_template('update.html', data=data)
    name = request.form['name']
    desc = request.form.get('desc', '')
    image = request.files['image']

    if name == '' or not name:
      flash('Nama tidak boleh kosong', 'danger')
      return redirect(request.url)
    
    if image and allowed_file(image.filename):
        if data[3]:
            old_image_path = os.path.join(app.config['UPLOAD_FOLDER'], data[3])
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

        filename = secure_filename(image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)

        cursor.execute("UPDATE cat SET `name`=%s, `desc`=%s, `image_url`=%s WHERE `id`=%s", (name, desc, filename, id))
    else:
        cursor.execute("UPDATE cat SET `name`=%s, `desc`=%s WHERE `id`=%s", (name, desc, id))
    
    mysql.connection.commit()
    flash('Data berhasil diubah!', 'success')
    return redirect(url_for('crud'))
    
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM cat WHERE id = %s", (id,))
    data = cursor.fetchone()

    if not data:
      flash('Data tidak ditemukan', 'danger')
      return redirect(url_for('breeds'))

    if data[3]:
      old_image_path = os.path.join(app.config['UPLOAD_FOLDER'], data[3])
      if os.path.exists(old_image_path):
          os.remove(old_image_path)

    cursor.execute("DELETE FROM cat WHERE `id` = %s", (id,))
    mysql.connection.commit()
    flash('Data berhasil dihapus!', 'success')
    return redirect(url_for('crud'))

if __name__ == "__main__":
  app.run(debug=True)
