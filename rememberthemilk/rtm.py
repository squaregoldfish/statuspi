# Requires RTMApi https://pypi.python.org/pypi/RtmAPI/
import time
from datetime import date
from datetime import timedelta
import sys
import webbrowser
from rtmapi import Rtm

API_KEY="e9e716aa8dfd1204538df16585484ba2"
SHARED_SECRET="5d84e9d9317ac7d7"
TOKEN="3c4fcf60ed866d0a85d9c6460294ac4d3bd11deb"
READING_LIST="36739788"
WORK_LIST="22205173"

if __name__ == '__main__':
    # call the program as `listtasks.py api_key shared_secret [optional: token]`
    # get those parameters from http://www.rememberthemilk.com/services/api/keys.rtm
    api = Rtm(API_KEY, SHARED_SECRET, "delete", TOKEN)

    # authenication block, see http://www.rememberthemilk.com/services/api/authentication.rtm
    # check for valid token
    if not api.token_valid():
        # use desktop-type authentication
        url, frob = api.authenticate_desktop()
        # open webbrowser, wait until user authorized application
        webbrowser.open(url)
        raw_input("Continue?")
        # get the token for the frob
        api.retrieve_token(frob)
        # print out new token, should be used to initialize the Rtm object next time
        # (a real application should store the token somewhere)
        print "New token: %s" % api.token

    # get all open tasks, see http://www.rememberthemilk.com/services/api/methods/rtm.tasks.getList.rtm
    all_tasks = api.rtm.tasks.getList(filter="status:incomplete")

    overdue = 0
    dueToday = 0
    impending = 0
    reading = 0
    oldest_overdue = 0
    total_count = 0

    today = date.today()

    for tasklist in all_tasks.tasks:
        for taskseries in tasklist:
            total_count = total_count + 1
            datestring = taskseries.task.due.strip()
            tz = taskseries.task.timezone
            if datestring != "":
                due_hour = int(datestring[11:13])
                due_date = date(int(datestring[0:4]), int(datestring[5:7]), int(datestring[8:10]))
                if due_hour > 0:
                    due_date = due_date + timedelta(days=1)


                if due_date < today:
                    overdue = overdue + 1
                    overdue_by = (today - due_date).days
                    if overdue_by > oldest_overdue:
                        oldest_overdue = overdue_by
                elif due_date == today:
                    dueToday = dueToday + 1
                else:
                    diff = due_date - today
                    if diff.days <= 1:
                        impending = impending + 1


    f = open("../rtm_all.txt", "w")
    f.write(str(total_count))
    f.close()

    f = open("../rtm_overdue.txt", "w")
    f.write(str(overdue))
    f.close()

    f = open("../rtm_today.txt", "w")
    f.write(str(dueToday))
    f.close()

    f = open("../rtm_impending.txt", "w")
    f.write(str(impending))
    f.close()

    f = open("../rtm_longestoverdue.txt", "w")
    f.write(str(oldest_overdue))
    f.close()

    #time.sleep(5)
    #reading_tasks = api.rtm.tasks.getList(list_id=READING_LIST,filter="status:incomplete")
    #oldest_reading_task = 0
    #for tasklist in reading_tasks.tasks:
    #    for taskseries in tasklist:
    #        reading = reading + 1
    #        datestring = taskseries.task.added.strip()
    #        task_date = date(int(datestring[0:4]), int(datestring[5:7]), int(datestring[8:10]))
    #        age = (today - task_date).days
    #        if age > oldest_reading_task:
    #            oldest_reading_task = age
#
#    f = open("../rtm_reading.txt", "w")
#    f.write(str(reading))
#    f.close()

#    f = open("../rtm_oldest_reading.txt", "w")
#    f.write(str(oldest_reading_task))
#    f.close()

    work = 0
    work_tasks = api.rtm.tasks.getList(list_id=WORK_LIST,filter="status:incomplete AND isRepeating:false")

    for tasklist in work_tasks.tasks:
        for taskseries in tasklist:
            work = work + 1


    f = open("../rtm_work.txt", "w")
    f.write(str(work))
    f.close()

