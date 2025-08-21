from flask import Flask, request

app = Flask(_name_)

# Dummy sensitive info (for vulnerability demo)
DUMMY_USERNAME = "admin"
DUMMY_PASSWORD = "password123"
DUMMY_API_KEY = "12345-ABCDE-SECRET"
DUMMY_IP = "192.168.1.10"

@app.route("/")
def home():
    return """
    <h2>Welcome to Flask Security Demo</h2>
    <p><a href='/login'>Login Page</a></p>
    <p><a href='/secrets'>Sensitive Info (Vulnerable)</a></p>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == DUMMY_USERNAME and password == DUMMY_PASSWORD:
            return f"<h3>Welcome, {username}!</h3><p>Go to <a href='/secrets'>Secrets Page</a></p>"
        else:
            return "<h3>Invalid credentials</h3>"

    return """
    <form method='POST'>
        <label>Username:</label>
        <input type='text' name='username'><br>
        <label>Password:</label>
        <input type='password' name='password'><br>
        <button type='submit'>Login</button>
    </form>
    """

@app.route("/secrets")
def secrets():
    return f"""
    <h2>🚨 Sensitive Information (Demo Only) 🚨</h2>
    <p><b>Username:</b> {DUMMY_USERNAME}</p>
    <p><b>Password:</b> {DUMMY_PASSWORD}</p>
    <p><b>API Key:</b> {DUMMY_API_KEY}</p>
    <p><b>Server IP:</b> {DUMMY_IP}</p>
    <p><i>This is intentionally vulnerable for scanning practice.</i></p>
    """

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)

