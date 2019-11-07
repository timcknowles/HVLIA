from flask import Flask, request, render_template, send_file
from calculator import do_calculation,round_half_up, saline_vol
from flask_materialize import Material
from flask_cachebuster import CacheBuster

app = Flask(__name__)
Material(app)
app.config["DEBUG"] = True
config = { 'extensions': ['.js', '.css'], 'hash_size': 5 }
cache_buster = CacheBuster(config=config)
cache_buster.init_app(app)

@app.route('/guideline/')
def show_hvlia_static_pdf():
    return send_file('static/HVLIA.pdf', attachment_filename='HVLIA.pdf')

@app.route('/erp')
def show_erp_static_pdf():
    return send_file('static/ERP.pdf', attachment_filename='ERP.pdf')

@app.route('/disclaimer/')
def disclaimer_page():
    return render_template('disclaimer.html')

@app.route('/blocks/')
def block_page():
    return render_template('blocks.html')

@app.route('/acb/')
def acb_page():
    return render_template('acb.html')

@app.route('/sifib/')
def fib_page():
    return render_template('sifib.html')

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        wt=None
        KetVol=None
        block_info=None
        maxBlockVol=None
        try:
            wt = float(request.form["wt"])
            block_info = int(request.form.get('block_info'))
            KetVol = int(request.form.get('KetVol'))

        except:
            errors

        if wt is not None:
            result = do_calculation(wt,block_info)
            saline = saline_vol((maxBlockVol),do_calculation(wt,block_info),0.5,0.5,(KetVol),(block_info))
            return render_template ('result.html').format(result=result,saline=saline, KetVol=KetVol, wt=wt, block_info=block_info)
    return render_template('calculator.html').format(errors=errors)
