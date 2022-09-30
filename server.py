from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<color1>')
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard(x=8,y=8,color1='#556C2F',color2='#FEFFE0'):
    return render_template("index.html", row = x, col = y, color_one = color1, color_two = color2)


if __name__=="__main__":
    app.run(debug=True, port=5001)
