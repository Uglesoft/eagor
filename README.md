# Eagor

A keystrokes assistant

## Quickstart

Assuming you have python and pip installed

```bash
git clone https://gitlab.com/uglesoft/openware/eagor
cd eagor
bash setup
python3 main.py
```

## Installation

Navigate to a directory of your choosing and execute the following

```bash
git clone https://gitlab.com/uglesoft/openware/eagor
```

## Configuration

This program is meant to be cutomizable, I use it for my annoying and frequently changing access tokens to GitHub and GitLab. If you want to use it for something else, modify the code to your heart's content. If you want to use the access key helpers, I recommend adding them to the .env file so you don't commit them into the codebase by accident. Execute the following

```bash
bash setup
```

Which will create your .env file for you and install necessary dependencies. Now open the `.env` file, the contents are self explanatory.

## Usage

From the project directory, execute the following:

```bash
python3 main.py`
```

Eagor will start listening for a variety of keystroke patterns, which will be explained in the terminal menu. The output will look something like this:

```bash
Hello. I am your personal keystrokes and hotkeys assistant. Below is a list of commands I currently support.

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
```

By pressing these key combinations, the program will activate and output keystrokes to the foreground application. For example, when I press the `0`, `e`, `s`, and `b` keys simultaneously while I have a text editor open and selected, the following is typed out into the text editor:

```
Respectfully,
Christian Kesler
```

And the content below is printed to the terminal where the program provided the menu and is still listening:

```bash
email_signature_block function called
email_signature_block function completed
```

(note, the listener is blocked by the terminal on some devices)

## Authors

Christian J Kesler, Uglesoft