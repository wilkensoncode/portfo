from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('db.txt', mode='a') as detabase:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = detabase.write(f'\n{email}, {subject},{message}')


def write_to_csv(data):
    with open('db.csv', mode='a', newline='\n') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4000)
