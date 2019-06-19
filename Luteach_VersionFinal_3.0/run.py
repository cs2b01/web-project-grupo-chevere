from luteach_web import application

if __name__ == '__main__':
    application.secret_key = ".."
    application.run(port=8080, threaded=True, host=('127.0.0.1'))
