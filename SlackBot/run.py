from flask import Flask
from flask import request
import re
from twilio import twiml
import sqlite3
import time

app = Flask(__name__)

@app.route('/', methods=['POST'])


def sms():
    response = twiml.Response()
    body = request.form['Body']
    helper="Text CONNECT and a skill or major to meet a developer!\
		 Ex: Connect me with an engineer"

    if "USAGE" in body.upper():
	response.message(helper)
    elif "CONNECT" in body.upper():

	if "ENGINEER" in body.upper():
		result=re.search(r"\'(.*?)\'", str(searchDB("ENGINEER")))
		
		response.message("Connecting with: "+str(result.group(0)))

	elif "WEB" in body.upper():
		
		response.message("Connecting with: "+str(searchDB("ENGINEER")))

    elif "/CONVO END" in body.upper():
		response.message("Conversation with Ric has been terminated")

    elif "HI" in body.upper():
		if "DEV" not in body.upper():
			response.message("Hello Alex! Welcome to SmartMix's connection service. Type USAGE for assistance.")
		else:
			#time.sleep(10)
			response.message("Ric: Sup Alex hope your presentation is going well bro")
    elif "LOOKING" in body.upper():
		response.message("Hey Alex! What do you need help making today?")
    elif "AWS" in body.upper():
		
		response.message("Connecting you with a server expert right now!")
   
    else:
		response.message("Sorry, could not find that command. Text USAGE for help.")
    #else:
#	response.message("You sent me: {0}".format(body)
    return str(response)

def searchDB(text):
        conn=sqlite3.connect('bot.db')
	cursor=conn.cursor()
        if text=="ENGINEER":
                major='CMPE'
        cursor.execute("SELECT * FROM USERS WHERE MAJOR = \'" + major+"\'")
        found=cursor.fetchone()
	conn.close()
        return found


if __name__ == "__main__":
    # Since this is a development project, we will keep debug on to make our
    # lives easier. We would want to configure our app more conservatively
    # in production.
    app.debug= True
    app.run(host='0.0.0.0')


