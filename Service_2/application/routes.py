from application import app
import random


@app.route('/randomcolor', methods=['GET'])
def beginning():

	list = ['Your Outfit colour is Red','Your Outfit colour is Yellow','Your Outfit colour is Blue']
	
	return list[random.randrange(3)]