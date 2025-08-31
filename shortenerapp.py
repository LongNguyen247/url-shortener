from flask import Flask, request, redirect, render_template, flash
import db
import utils

app = Flask(__name__)
app.secret_key = "supersecretkey"  # replace with env var in production


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form["long_url"]

        # Validate URL
        if not utils.is_valid_url(long_url):
            flash("Invalid URL. Please use http:// or https://", "error")
            return render_template("index.html")

        # Generate unique short code
        short = utils.generate_short_code()

        # Save to DB
        db.save_url(short, long_url)

        short_url = request.host_url + short
        return render_template("index.html", short_url=short_url)

    return render_template("index.html")


@app.route("/<short>")
def redirect_url(short):
    long_url = db.get_url(short)
    if long_url:
        return redirect(long_url)
    return render_template("404.html"), 404


if __name__ == "__main__":
    db.init_db()  # Ensure DB is set up
    app.run(debug=True)
