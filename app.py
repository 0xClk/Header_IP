from flask import Flask, request, render_template_string

app = Flask(__name__)

# Allowed headers and IPs
ALLOWED_HEADER = 'True-Client-IP'
ALLOWED_IPS = {'::1'}

# HTML templates
SUCCESS_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #dff0d8;
            color: #3c763d;
            text-align: center;
            padding: 50px;
        }
        .container {
            border: 1px solid #d6e9c6;
            border-radius: 5px;
            padding: 20px;
            display: inline-block;
            background-color: #dff0d8;
        }
        h1 {
            font-size: 2em;
            margin-bottom: 10px;
        }
        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Success!</h1>
        <p>You got me, here's the flag : FlagY{f12519bb497d6e454ead5c859b82a96b}</p>
    </div>
</body>
</html>
'''

ERROR_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access Denied</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2dede;
            color: #a94442;
            text-align: center;
            padding: 50px;
        }
        .container {
            border: 1px solid #ebccd1;
            border-radius: 5px;
            padding: 20px;
            display: inline-block;
            background-color: #f2dede;
        }
        h1 {
            font-size: 2em;
            margin-bottom: 10px;
        }
        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Access Denied</h1>
        <p>Oops! It looks like you're trying to access this server from an unauthorized device. If you believe this is a mistake, please contact support.</p>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    # Check if the allowed header contains an allowed IP
    if request.headers.get(ALLOWED_HEADER) in ALLOWED_IPS:
        return render_template_string(SUCCESS_HTML)
    
    # Check if the remote address is allowed
    if request.remote_addr in ALLOWED_IPS:
        return render_template_string(SUCCESS_HTML)
    
    return render_template_string(ERROR_HTML), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)
                                                                                                                                                            
