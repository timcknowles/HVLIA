from flask import Flask, request
from test import do_calculation,round_half_up
# from decimal import Decimal, getcontext
# getcontext().prec = 2


app = Flask(__name__)
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
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)
    return '''
        <html>
            <body>
            {errors}
                <p>Enter your numbers:</p>
                <form method="post" action=".">
                    <p><input name="wt" /></p>
                    <p><input name="vol" /></p>
                    <p><input name="conc" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
