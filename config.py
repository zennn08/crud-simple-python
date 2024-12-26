import os

class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'tugas3prakpmp'
    SECRET_KEY = 'APAJALAH'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/upload')  # Lokasi penyimpanan file
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # Batas ukuran file 10MB