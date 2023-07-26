import smtplib

my_email = "andifarhan1094@gmail.com"
password = "mmmbtchpwvufbnjj"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = my_email, password = password)
connection.sendmail(
    from_addr = my_email, 
    to_addrs = "19623112@mahasiswa.itb.ac.id", 
    msg = "Subject:Mail using Python\n\nHai, Han!"
)
connection.close()