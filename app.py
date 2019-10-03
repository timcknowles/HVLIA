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
        KetVol = 0



        try:
            wt = float(request.form["wt"])
            vol = float(request.form["vol"])
            conc = float(request.form["conc"])
            KetVol = int(request.form.get('KetVol'))
            print(KetVol*1000)
        except:
            errors

        if wt is not None and vol is not None and conc is not None:

            result = do_calculation(wt, vol, conc)
            saline = saline_vol(100,do_calculation(wt, vol, conc),0.5,0.5,(KetVol))
            return render_template ('result.html').format(result=result,saline=saline, KetVol=KetVol, wt=wt)
    return render_template('calculator.html').format(errors=errors)
