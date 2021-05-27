from flask import Flask , render_template #html 문서이름을 받으면 파일->text로 변환

app = Flask(__name__) #__name__ -main-


@app.route('/', methods=['GET' , 'POST']) #경로 @명령의 다음줄을실행
def hello_world():
    return '<h1>Hello World!<h1>'

if __name__ == '__main__': #최초출발점
    app.run(port=5000, debug=True) #실행

