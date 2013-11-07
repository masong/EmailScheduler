from datetime import date
import json
import smtplib

def is_today(date_string):
  # I assume that the dates are in mm/dd format
  month, day = date_string.split('/')
  return date.today().month == int(month) and date.today().day == int(day)

def send_email(receiver, config):
  server = smtplib.SMTP(config['mail_server'])
  server.starttls()
  server.login(config['username'], config['password'])
  server.sendmail(config['from_email'], receiver + config['receiver_domain_name'], 'test message')
  server.quit()

config = json.loads(open('CONFIG.private').read())
schedule_file = open(config['email_schedule'])

for line in schedule_file.read().splitlines():
  date_string, receiver = line.split('\t')
  if is_today(date_string):
    send_email(receiver, config)
    print 'Sent email to %s' % (receiver)
