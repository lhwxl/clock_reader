from microdot import Microdot

app = Microdot()


@app.route("/")
def insex():
	return "<h1>hello!</h1><hr><h2>Welcome to use the clock_reader.</h2>"
