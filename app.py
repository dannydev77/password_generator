from flask import Flask, render_template, request, jsonify
import subprocess
import base64

app = Flask(__name__)

# Generate password using OpenSSL rand -base64
@app.post('/generate')
def generate():
    length = int(request.form.get('length', 16))
    use_upper = request.form.get('uppercase') == 'true'
    use_lower = request.form.get('lowercase') == 'true'
    use_nums = request.form.get('numbers') == 'true'
    use_syms = request.form.get('symbols') == 'true'

    # Base64 gives approx 0.75 * bytes output size.
    openssl_len = int(length * 0.75) + 2

    try:
        raw = subprocess.check_output(["openssl", "rand", "-base64", str(openssl_len)])
        pwd = raw.decode().strip().replace("\n", "")
    except Exception as e:
        return jsonify({"error": str(e)})

    # Filter characters based on options
    allowed = ""
    if use_upper: allowed += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lower: allowed += "abcdefghijklmnopqrstuvwxyz"
    if use_nums: allowed += "0123456789"
    if use_syms: allowed += "!@#$%^&*()-_=+[]{};:,.<>?"

    if not allowed:
        return jsonify({"error": "No character types selected."})

    filtered = ''.join([c for c in pwd if c in allowed])

    # If filtering reduces too much, pad using allowed chars
    import random
    while len(filtered) < length:
        filtered += random.choice(allowed)

    return jsonify({"password": filtered[:length]})

@app.get('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
