import os

class Config:
    SECRET_KEY = 'pudin'  # Cambia esto en producción
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Gfl_25030@localhost:3307/notas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False #(Evita warnings y mejora el rendimiento).