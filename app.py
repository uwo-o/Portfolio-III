import smtplib
from decouple import config
from flask import Flask, render_template, request, redirect, url_for, flash

app=Flask(__name__)
app.secret_key = config('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(config('EMAIL'), config('PASSWORD'))
            message = 'Subject: {}\n\nNombre: {}\nCorreo: {}\n\n{}'.format(subject, name, email, message)
            server.sendmail(config('EMAIL'), config('EMAIL2'), message)
            server.quit()
            flash('Your message has been sent!')
        except:
            flash('An error occured. Please try again.')
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')