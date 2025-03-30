from flask import Flask

app = Flask(__name__)

# Mmebers API
@app.route("/members")
def members():
    return {"members": ["Members", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(debug=True)