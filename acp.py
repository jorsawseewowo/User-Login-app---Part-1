from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    number_of_vowels = None

    if request.method == "POST":
        input_string = request.form.get("input_string", "").lower()

        number_of_vowels = 0
        for char in input_string:
            if char in "aeiou":
                number_of_vowels += 1

    return render_template(
        "index.html",
        number_of_vowels=number_of_vowels
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)