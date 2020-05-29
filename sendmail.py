#!/usr/bin/env python
# coding: utf-8

# In[2]:


import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "asdf@gmail.com"  # Enter your address
receiver_email = "qwer@gmail.com"  # Enter receiver address
password = "pass"
message = """Subject: Hi there
Your model has sucessfully achieved 80%+ accuracy  
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# In[ ]:




