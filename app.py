from flask import Flask, request, render_template
from test import do_calculation,round_half_up, saline_vol
from flask_material import Material
# from decimal import Decimal, getcontext
# getcontext().prec = 2


app = Flask(__name__)
Material(app)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def adder_page():


    errors = ""
    if request.method == "POST":
        wt = None
        vol = None
        conc = None
        try:
            wt = float(request.form["wt"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["wt"])
        try:
            vol = float(request.form["vol"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["vol"])
        try:
            conc = float(request.form["conc"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["conc"])

        if wt is not None and vol is not None and conc is not None:

            result = do_calculation(wt, vol, conc)
            saline = saline_vol(100,do_calculation(wt, vol, conc))
            return render_template ('result.html').format(result=result,saline=saline)

    return render_template('calculator.html').format(errors=errors)
