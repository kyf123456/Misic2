import os

#设置上传文件存放的位置
BASE_DIR=os.path.dirname(os.path.abspath(__name__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR=os.path.join(STATIC_DIR,'uploads')


class Config():
    ENV='development'
    DEBUG=True

    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@127.0.0.1/users'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    SECRET_KEY='aaaaa'

    #设置上传文件存放的位置
    BASE_DIR=os.path.dirname(os.path.abspath(__name__))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    MEDIA_DIR=os.path.join(STATIC_DIR,'uploads')