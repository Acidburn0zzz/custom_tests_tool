#!/usr/bin/env python3
# -*- coding:utf-8 -*
#
# Florent Jacquet <florent.jacquet@free-electrons.com>
#


from xmlrpc import client
from pprint import pprint
from datetime import datetime, timedelta

import configparser

import smtplib
from email.mime.text import MIMEText

from boards import boards

hostname = "farm"

username = "my-user"
token = "my-awesome-token"

config = configparser.ConfigParser()
config.read("notifications.conf")
kwargs = dict(config["mail"])

JOB_STATUS = {
        0: "Submitted",
        1: "Running",
        2: "Complete",
        3: "Incomplete",
        4: "Canceled",
        5: "Canceling",
        }

def main():
    username = config.get("lava", "user")
    token = config.get("lava", "token")

    server = client.ServerProxy("http://%s:%s@%s/RPC2" % (username, token, hostname))
    end_date = datetime.now().replace(hour=11, minute=0, second=0,
            microsecond=0)
    start_date = end_date - timedelta(hours=72)
    mail_list = {}
    incomplete_tests = server.results.query("testjob",
            "testjob__end_time__gt__%s,"
            "testjob__end_time__lt__%s,"
            "testjob__submitter__exact__custom-tests,"
            "testjob__status__exact__Incomplete"
            % (start_date, end_date))
    failed_tests = server.results.query("testjob",
            "testjob__end_time__gt__%s,"
            "testjob__end_time__lt__%s,"
            "testcase__result__exact__Test failed,"
            "testjob__submitter__exact__custom-tests,"
            "testsuite__name__exact__1_custom-tests"
            % (start_date, end_date))
    for j in failed_tests + incomplete_tests:
        d = j["description"].split("--")
        job_report = "".join([
            '{:<10}'.format(d[1]),
            '{:<35}'.format(d[0]),
            '{:<30}'.format(d[2]),
            '{:<14}'.format(d[3]),
            '{:<12}'.format(JOB_STATUS[j["status"]]),
            "http://farm/scheduler/job/%s" % j["id"],
            ])
        board = boards.get(j["requested_device_type_id"], None)
        if board:
            for email in board.get("notify", []):
                if email in mail_list.keys():
                    mail_list[email].append(job_report)
                else:
                    mail_list[email] = [job_report]

    server = smtplib.SMTP(kwargs["server"], kwargs["port"])
    server.ehlo()
    server.starttls()
    server.login(kwargs["login"], kwargs["password"])
    for user,job_list in mail_list.items():
        msg_list = []
        msg_list.append("".join([
            '{:<10}'.format("tree"),
            '{:<35}'.format("device"),
            '{:<30}'.format("defconfig"),
            '{:<14}'.format("test"),
            '{:<12}'.format("job status"),
            "link",
            ])
        )
        msg_list += job_list
        print("\nMessage to %s:" % user)
        print('\n'.join(msg_list))
        msg = MIMEText(
                "The following jobs failed during the last 24 hours:\n"
                "\n" + '\n'.join(msg_list))
        msg['Subject'] = "CI summary"
        msg['From'] = kwargs["mail"]
        msg['To'] = user
        server.sendmail(kwargs["mail"], [user], msg.as_string())
    server.quit()
    return

if __name__ == "__main__":
    main()

