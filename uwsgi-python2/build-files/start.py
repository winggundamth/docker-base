#!/usr/bin/python3

################################################################################
#####################  This file intend to be only sample  #####################
################################################################################

import os
import argparse
import subprocess

project_name = 'xxx'
python_path = os.getenv('PYTHONPATH', "/home/web/" + project_name)

# Add options
parser = argparse.ArgumentParser()
parser.add_argument("--branch",
    help="Specific branch name that you want to checkout")
parser.add_argument("--develop",
    help="Start container with routing.py for development environment",
    action="store_true")
parser.add_argument("--update",
    help="Tell script to do git pull and pip install -r requirements.txt when" +
         "start container",
    action="store_true")
parser.add_argument("--pip-update",
    help="Tell script to do pip install -r requirements.txt when start" +
         "container",
    action="store_true")
args = parser.parse_args()

# Change directory to project home
os.chdir(python_path)
change_to_web_user = ["sudo", "-u", "web", "-H"]

# Doing first initial start container
if os.path.isfile("/first-initial"):

    if not args.develop:

        # Fetch code
        if args.branch or args.update:
            subprocess.call(change_to_web_user + ["git", "fetch"])

        # Check if branch exist and checkout branch
        if args.branch:
            try:
                subprocess.check_call(change_to_web_user +
                                      ["git", "show-ref", "|", "grep", "-q",
                                      "/",args.branch,"$"])
                subprocess.call(change_to_web_user +
                                ["git", "checkout", args.branch])
            except:
                print('ERROR: Branch {:s} is not exist.'.format(args.branch))
                exit(1)

        # Always merge code
        subprocess.call(change_to_web_user + ["git", "pull"])

    # Check if pip install -r requirements.txt
    if args.branch or args.update or args.pip_update or args.develop:
        subprocess.call(["pip", "install", "-r", python_path +
                        "/requirements.txt"])

    # Remove first-initial file
    os.remove("/first-initial")

# Run start process commands
if args.develop:
    uwsgi_protocol_option = "--http-socket"
    uwsgi_autoreload_option = "1"
else:
    uwsgi_protocol_option = "--socket"
    uwsgi_autoreload_option = "0"

subprocess.call(["rm", "-rf", "/var/run/rsyslogd.pid"])
subprocess.call(["service", "rsyslog", "start"])
# Work around fix cron not working on overlayfs as describe here
# https://github.com/docker/docker/issues/16813
subprocess.call(["touch", "/etc/crontab"])
subprocess.call(["cron"])
subprocess.call(["uwsgi", "--python-autoreload", uwsgi_autoreload_option,
                uwsgi_protocol_option, "0.0.0.0:5000", "/etc/uwsgi.ini"])
