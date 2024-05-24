from flask import Flask, render_template, request
from utils.calculation_functions import calc_circle

# initiate the app
app = Flask(__name__)


# initiate the first route
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/circle", methods=['GET', 'POST'])
def circle():

    # conditional statement, based on the method
    if request.method == 'POST':
        # get the data from the form
        diameter = float(request.form.get("diameter"))

        # run the circle function
        circle_size = calc_circle(diameter)
    
        return render_template("circle.html", 
                               circle_size=circle_size, 
                               diameter=diameter)
    
    return render_template("circle.html")


if __name__ == "__main__":
    app.run()