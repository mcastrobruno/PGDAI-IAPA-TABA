# Intelligent Agents and Process Automation - TABA
## National College of Ireland
Bruno Castro - x22155686@student.ncirl.ie

# How to start
#### Cloning the repo:
1) Clone this repository
2) Run the code ```python main.py``` using terminal

#### Configuring the applicaiton for SMTP sending

> **Note**
> The project is ready to send e-mail using a third part SMTP server such as Mailchimp, Sendgrind, etc
> But for the purpose of this, there is a config on the ```config.py``` to disable SMTP, in this case the sending will be skipped and a stub version of the email sender will be executed, which will allow to all the steps to be executed.


1) open the ```config.py``` file and define the configuration values for the following:
- smtp_server
- smtp_port
- smtp_username
- smtp_password
- smtp_enabled = True
