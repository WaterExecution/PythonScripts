import ftplib
from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)

@app.route("/getscore", methods = ['GET'])
def getscore():
    ftp = ftplib.FTP("")
    ftp.login('', '')

    ftp.cwd('/plugins/scoreboarddata/')
    ftp.retrbinary("RETR score.txt", open("score.txt", 'wb').write)
    ftp.close()

    f = open("score.txt", "r")
    score = f.read()
    f.close()
    return score

@app.route('/')
def index():
    return render_template('index.html', score=getscore())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)




