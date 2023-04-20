import os
from dotenv import load_dotenv
load_dotenv()


from pynput import keyboard
from pynput.keyboard import Controller, Key
import time
from plyer import notification
import string
from random import randrange

def notif_end(function_name):
	# notification.notify(
	# 	title = "Keystrokes Program",
	# 	message = "The " + function_name + " function has been completed.",
	# 	app_icon = "robot.ico",
	# 	timeout = 1
	# )
	pass

# instantiation
c = Controller()


# 0esb
def email_signature_block():
	print("email_signature_block function called")

	c.release('0')
	c.release('e')
	c.release('m')
	c.release('f')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.type('Respectfully,')
	time.sleep(.1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.1)
	c.type('Christian Kesler')
	time.sleep(.1)

	notif_end("email_signature_block")

	print("email_signature_block function completed")


# 0gpw
def generate_password():
	print("function generate_password called")

	password_raw = ""
	password_shuffled = ""

	digits = "0123456789"

	characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + digits

	password_raw = string.ascii_lowercase[randrange(len(string.ascii_lowercase))] + string.ascii_uppercase[randrange(len(string.ascii_uppercase))] + string.punctuation[randrange(len(string.punctuation))]	+ digits[randrange(len(digits))]

	for x in range(12):
		password_raw = password_raw + characters[randrange(len(characters))]

	for x in range(len(password_raw)):
		index = randrange(len(password_raw))

		password_shuffled = password_shuffled + password_raw[index]
		password_raw = password_raw[0:index] + password_raw[(index+1):]

	bar = ""
	for x in range(32):
		bar = bar + "="

	print(bar)
	print(password_shuffled)
	print(bar)

	notif_end("generate_password")

	print("function generate_password completed")


# 0gla
def gitlab_auth():
	print("gitlab auth function called")

	c.release('g')
	c.release('l')
	c.release('a')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	time.sleep(.5)
	c.type('christian.kesler')
	time.sleep(.1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.5)
	c.type(os.getenv("GITLAB_ACCESS_KEY"))
	time.sleep(.1)
	c.press(Key.enter)
	c.release(Key.enter)

	notif_end("gitlab_auth")

	print("gitlab auth function completed")


# 0gha
def github_auth():
	print("github auth function called")

	c.release('g')
	c.release('h')
	c.release('a')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	time.sleep(.5)
	c.type('christian-kesler')
	time.sleep(.1)
	c.press(Key.enter)
	c.release(Key.enter)
	time.sleep(.5)
	c.type(os.getenv("GITHUB_ACCESS_KEY"))
	time.sleep(.1)
	c.press(Key.enter)
	c.release(Key.enter)

	notif_end("github_auth")

	print("github auth function completed")


# 0nsq
def node_sqlite():
	print("node_sqlite function called")

	c.release('n')
	c.release('s')
	c.release('q')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.type('''
	dtb.all(
	dtb.run(
	'SELECT * FROM table WHERE id = ?;',
	'INSERT INTO table(field) VALUES (?);',
	'UPDATE table SET field = ? WHERE id = ?;',
	'DELETE FROM table WHERE id = ?;',
	[
	field,
	id,
	],
	async function(err, rows) {
	async function(err) {
	if (err) {
	console.error(err)
	response = {
	err: 'database error',
	data: null,
	}
	console.info(response)
	res.send(response)
	res.end()
	} else if (rows.length == 0) {
	console.error(err)
	response = {
	err: 'not found',
	data: null,
	}
	console.info(response)
	res.send(response)
	res.end()
	} else if (this.changes == 0) {
	console.error(err)
	response = {
	err: 'no changes',
	data: null,
	}
	console.info(response)
	res.send(response)
	res.end()
	} else {

	// custom logic here

	}
	}
	)
	''')

	notif_end("node_sqlite")

	print("node_sqlite completed")


# 0nea
def node_express_api():
	print("git push function called")

	c.release('n')
	c.release('e')
	c.release('a')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.type('''
    app.post('/api/category/endpoint', async (req, res) => {
    try {
    if (ugle_auth.apiSession(req, res)) {
    if (ugle_auth.apiPermission(req, res, 'partner')) {

    // custom logic here

    }
    }
    } catch (err) {
    res.send(err)
    res.end()
    }
    })
	''')

	notif_end("node_express_api")

	print("node_express_api completed")


# 0ner
def node_express_routing():
	print("git push function called")

	c.release('n')
	c.release('e')
	c.release('r')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.type('''
    app.get('/route', async (req, res) => {
    try {
    if (ugle_auth.navSession(req, res)) {
    if (ugle_auth.navPermission(req, res, 'partner')) {

    // custom logic here

    }
    }
    } catch (err) {
    res.redirect(`/?err=${err.message}`)
    }
    })
	''')

	notif_end("node_express_routing")

	print("node_express_routing completed")


# 0nar
def node_axios_request():
	print("node_axios_request function called")

	c.release('n')
	c.release('a')
	c.release('r')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.type('''
	axios({
	method: "get",
	url: `https://domain.com/endpoint`,
	params: {
	fields: 'name',
	}
	})
	.catch(error => {
	console.log(error);
	res.send({
	err: error.response.data,
	data: null,
	})
	res.end()
	})
	.then(response => {
	res.send({
	err: null,
	data: response.data.data,
	})
	res.end()
	})
	''')

	notif_end("node_axios_request")

	print("node_axios_request completed")


# 0nfe
def node_for_each():
	print("node_for_each function called")

	c.release('n')
	c.release('a')
	c.release('r')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.type('''
	if (!Array.isArray(myArr)) {
	res.send('error')
	// OR
	res.redirect('/?msg=error')
	} else {

	myArr.forEach((item, index) => {
		// custom logic
	})
	// OR 
	for (let i = 0; i < myArr.length; i++) {
		// custom logic
	}

	}
	''')

	notif_end("node_for_each")

	print("node_for_each completed")


# 0nar
def node_parse_while():
	print("node_parse_while function called")

	c.release('n')
	c.release('p')
	c.release('w')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.type('''
	varObj = varString
	while(typeof varObj == 'string') {
		varObj = JSON.parse(varObj)
	}
	''')

	notif_end("node_parse_while")

	print("node_parse_while completed")


# nc0
def node_check_object():
	print("node_check_object function called")

	c.release('n')
	c.release('c')
	c.release('o')

	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	c.press(Key.backspace)
	c.release(Key.backspace)
	time.sleep(.1)

	c.type('''
	if (myObj === null || Object.prototype.toString.call(myObj) !== '[object Object]') {
		myObj = {};
	}
	''')

	notif_end("node_check_object")

	print("node_check_object completed")


# hotkeys
hotkeys = {
	'0+e+s+b': email_signature_block,
	'0+g+p+w': generate_password,
	'g+l+a': gitlab_auth,
	'g+h+a': github_auth,
	'0+n+s+q': node_sqlite,
	'0+n+e+a': node_express_api,
	'0+n+e+r': node_express_routing,
	'0+n+a+r': node_axios_request,
	'0+n+p+w': node_parse_while,
	'0+n+f+e': node_for_each,
	'n+c+0': node_check_object
}


# greeting
print("Hello. I am your personal keystrokes and hotkeys assistant. Below is a list of commands I currently support.")
print("""
	'0+e+s+b': email_signature_block,
	'0+g+p+w': generate_password,
	'g+l+a': gitlab_auth,
	'g+h+a': github_auth,
	'0+n+s+q': node_sqlite,
	'0+n+e+a': node_express_api,
	'0+n+e+r': node_express_routing,
	'0+n+a+r': node_axios_request,
	'0+n+p+w': node_parse_while,
	'0+n+f+e': node_for_each,
	'n+c+0': node_check_object
""")


# activating listener
with keyboard.GlobalHotKeys(hotkeys) as h:
	h.join()