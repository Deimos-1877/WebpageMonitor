import requests
import os
from bs4 import BeautifulSoup
import yagmail
import time
import logging
import datetime

# With Led on raspberry Pi?
WithLED = False

URL_TO_MONITOR = "http://reservation.livingscience.ch/wohnen"  # change this to the URL you want to monitor
Real_DELAY_TIME = 10  # seconds

SENDING_EMAIL_USERNAME = "webpagechangealert"  # replace with the username of the gmail account you created (e.g. "john.webmonitor" if the email is "john.webmonitor@gmail.com")
SENDING_EMAIL_PASSWORD = "Schrottmail1"  # replace with the password of the gmail account you created
Recipient_emails = ["fabian.repplinger@hotmail.com", "fhrepplinger@gmail.com"] # replace with the email addresses that will receive the notification
RECIPIENT_EMAIL_ADDRESS0 = "fabian.repplinger@hotmail.com"
RECIPIENT_EMAIL_ADDRESS1 = "renate.repplinger-hach@ec.europa.eu"
RECIPIENT_EMAIL_ADDRESS2 = "crepplinger@hotmail.de"
RECIPIENT_EMAIL_ADDRESS3 = "karl-peter.repplinger@ep.europa.eu"

DELAY_TIME = Real_DELAY_TIME / 2

# imports gpiozero and configures LED if with LED and accordingly defined ElsSeq()
if WithLED:
    from gpiozero import LED

    # selects GPIO Pin 17 for the LED
    ledred = LED(17)


    def ElsSeq():
        ledred.on()
        time.sleep(DELAY_TIME)
        ledred.off()
else:
    def ElsSeq():
        time.sleep(DELAY_TIME)

# Limits the program checking the website between 7am and 7pm. Most errors/false alarms occur between 11pm and 5am
Time_start = datetime.datetime(2009, 1, 1, 7, 0, 0, 198130).time()
Time_end = datetime.datetime(2000, 1, 1, 19, 0, 0, 198130).time()


def timecondition():
    now_time = datetime.datetime.now().time()
    if Time_start < now_time < Time_end:
        print("tested - true")
        return True
    else:
        print("tested - false")
        return False


def send_email(alert_str, RECIPIENT_EMAIL_ADDRESS):
    """Sends an email alert. The subject and body will be the same. """
    yagmail.SMTP(SENDING_EMAIL_USERNAME, SENDING_EMAIL_PASSWORD).send(
        RECIPIENT_EMAIL_ADDRESS, alert_str, alert_str)


def send_email_alert():
    for email in Recipient_emails:
        send_email(f"URGENT! {URL_TO_MONITOR} WAS CHANGED!", email)


def process_html(string):
    soup = BeautifulSoup(string, features="lxml")
    # make the html look good
    soup.prettify()
    # remove script tags
    for s in soup.select('script'):
        s.extract()
    # remove meta tags 
    for s in soup.select('meta'):
        s.extract()
    # convert to a string, remove '\r', and return
    return str(soup).replace('\r', '')


def webpage_was_changed():
    """Returns true if the webpage was changed, otherwise false."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
    response = requests.get(URL_TO_MONITOR, headers=headers)

    # create the previous_content.txt if it doesn't exist
    if not os.path.exists("previous_content.txt"):
        open("previous_content.txt", 'w+').close()

    filehandle = open("previous_content.txt", 'r')
    previous_response_html = filehandle.read()
    filehandle.close()

    processed_response_html = process_html(response.text)

    if processed_response_html == previous_response_html:
        return False
    else:
        filehandle = open("previous_content.txt", 'w')
        filehandle.write(processed_response_html)
        filehandle.close()
        return True


def main():
    log = logging.getLogger(__name__)
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(message)s')
    log.info("Running Website Monitor")
    while True:
        try:
            if timecondition() != 1:
                log.info("time condition not fulfilled:" + str(timecondition()))
            elif webpage_was_changed():
                log.info("WEBPAGE WAS CHANGED.")
                send_email_alert()
                # send_email(f"URGENT! {URL_TO_MONITOR} WAS CHANGED!", RECIPIENT_EMAIL_ADDRESS0)
                # send_email(f"URGENT! {URL_TO_MONITOR} WAS CHANGED!", RECIPIENT_EMAIL_ADDRESS1)
                # send_email(f"URGENT! {URL_TO_MONITOR} WAS CHANGED!", RECIPIENT_EMAIL_ADDRESS2)
                # send_email(f"URGENT! {URL_TO_MONITOR} WAS CHANGED!", RECIPIENT_EMAIL_ADDRESS3)
            else:
                log.info("Webpage was not changed.")
                ElsSeq()
        except:
            log.info("Error checking website.")
        time.sleep(DELAY_TIME)


if __name__ == "__main__":
    main()
