from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "만나서 반갑습니다."

@app.route("/user/<userId>")
def profile(userId):
    return f"{userId}\" profile"

if __name__ == "__main__":
    app.run()




    # 홈페이지 만들기
    # 가상환경 만들고 플라스크 인스톨 하고
    # python 파일명.py