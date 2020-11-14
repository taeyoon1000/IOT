from flask import Flask,request
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
app = Flask(__name__)
LED=8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)
@app.route("/")
def helloworld():
    return "Hello world"
@app.route("/led")
def led():
    state = request.values.get("state","error")
    if state == "on":
        GPIO.output(8,GPIO.HIGH)
    elif state == "off":
        GPIO.output(8,GPIO.LOW)
    elif state == "error":
        return "쿼리스트링 state가 전달되지 않았습니다"
    else:
        return "잘못된 쿼리스트링이 전달되었습니다"
    return "LED"+state
@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEANUP"
if __name__ == "__main__":
    app.run(host="0.0.0.0") 