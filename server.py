from microdot import Microdot

app = Microdot()


@app.route("/")
def insex():
	return "Welcome to use the clock_reader."


@app.route("/control")
def control(request):
	key = request.args.get("key")

	return {"status": "OK"}
