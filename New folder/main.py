import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask,render_template,request
from flask_mail import  Mail,Message
app = Flask(__name__)
mail=Mail(app)

msg = MIMEMultipart()
msg['From'] = 'me@gmail.com'
msg['To'] = 'you@gmail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

@app.route('/' ,methods=['GET','POST'])
def homepage():
    if request.method=='POST':
        name=request.form.get('Name')
        email=request.form.get('Email')
        subject=request.form.get('Subject')
        message=request.form.get('Message')

        msg = MIMEMultipart()
        msg['From'] = name+"  "+email
        msg['To'] = 'amanuelgirma108@gmail.com'
        msg['Subject'] = subject
        message1 = "From :"+""+email +"\n" + message
        msg.attach(MIMEText(message1))
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("amanuelgirma108@gmail.com", "hxcivfhefmhcpuph")
        server.sendmail(email,"amanuelgirma108@gmail.com",msg.as_string())
        return render_template("index.html")
    return render_template("index.html")

if __name__== '__main__':
    app.run(debug=True)
