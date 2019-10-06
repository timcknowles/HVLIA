from flask import Flask, request, render_template
from test import do_calculation,round_half_up, saline_vol
from flask_materialize import Material
# from decimal import Decimal, getcontext
# getcontext().prec = 2


app = Flask(__name__)
Material(app)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def adder_page():




    errors = ""
    if request.method == "POST":

        KetVol = 0
        block_type = 0




        try:
            wt = float(request.form["wt"])
            block_info = int(request.form.get('block_info'))
            KetVol = int(request.form.get('KetVol'))

        except:
            errors

        if wt is not None:

            result = do_calculation(wt,block_type)
            saline = saline_vol(100,do_calculation(wt,block_type),0.5,0.5,(KetVol))
            return render_template ('result.html').format(result=result,saline=saline, KetVol=KetVol, wt=wt, block_type=block_type)
    return render_template('calculator.html').format(errors=errors)
