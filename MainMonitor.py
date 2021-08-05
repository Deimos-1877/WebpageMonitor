import requests
import os
from bs4 import BeautifulSoup
import yagmail
import time
import logging
import datetime
import json


def timecondition(Time_start, Time_end):
    now_time = datetime.datetime.now().time()
    if Time_start < now_time < Time_end:
        print("tested - true")
        return True
    else:
        print("tested - false")
        return False


def send_email(alert_str, RECIPIENT_EMAIL_ADDRESS, SENDING_EMAIL_USERNAME, SENDING_EMAIL_PASSWORD):
    """Sends an email alert. The subject and body will be the same. """
    yagmail.SMTP(SENDING_EMAIL_USERNAME, SENDING_EMAIL_PASSWORD).send(
        RECIPIENT_EMAIL_ADDRESS, alert_str, alert_str)


def send_email_alert(URL_TO_MONITOR, RECIPIENT_EMAILS, SENDING_EMAIL_USERNAME, SENDING_EMAIL_PASSWORD):
    for email in RECIPIENT_EMAILS:
        send_email(f"URGENT! {URL_TO_MONITOR} WAS CHANGED!", email, SENDING_EMAIL_USERNAME, SENDING_EMAIL_PASSWORD)


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


def webpage_was_changed(URL_TO_MONITOR):
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



# imports gpiozero and configures LED if with LED and accordingly defined ElsSeq()
def df_ElsSeq(WITH_LED):
    global ElsSeq
    if WITH_LED:
        try:
            from gpiozero import LED
            # selects GPIO Pin 17 for the LED
            ledred = LED(17)

            def ElsSeq(DELAY_TIME):
                ledred.on()
                time.sleep(DELAY_TIME)
                ledred.off()
        except:
            print('Please check that you are on a raspberryPi and have gpioZero installed.')
            def ElsSeq(DELAY_TIME):
                time.sleep(DELAY_TIME)
    else:
        def ElsSeq(DELAY_TIME):
            time.sleep(DELAY_TIME)


def main(URL_TO_MONITOR, RECIPIENT_EMAILS, SENDING_EMAIL_USERNAME, SENDING_EMAIL_PASSWORD, Time_start_end, Time_start_int, Time_end_int, REAL_DELAY_TIME, WITH_LED):
    DELAY_TIME = REAL_DELAY_TIME / 2
    Time_start = datetime.datetime(2009, 1, 1, Time_start_int, 0, 0, 198130).time()
    Time_end = datetime.datetime(2000, 1, 1, Time_start_end, 0, 0, 198130).time()
    df_ElsSeq(WITH_LED)
    log = logging.getLogger(__name__)
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(message)s')
    log.info("Running Website Monitor")
    while True:
        try:
            if Time_start_end == True and timecondition(Time_start, Time_end) != 1:
                log.info("time condition not fulfilled:" + str(timecondition(Time_start, Time_end)))
            elif webpage_was_changed(URL_TO_MONITOR):
                log.info("WEBPAGE WAS CHANGED.")
                send_email_alert(URL_TO_MONITOR, RECIPIENT_EMAILS, SENDING_EMAIL_USERNAME, SENDING_EMAIL_PASSWORD)

            else:
                log.info("Webpage was not changed.")
                ElsSeq(DELAY_TIME)
        except:
            log.info("Error checking website.")
        time.sleep(DELAY_TIME)


if __name__ == "__main__":
    main()
