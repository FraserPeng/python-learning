# flask_pi.py
import math
from flask import Flask, request
app = Flask(__name__)


@app.route("/pi")
def pi():
    # 默认参数
    n = int(request.args.get('n', '100'))
    s = 0.0
    for i in range(1, n):
        s += 1.0 / i / i
    return str(math.sqrt(6 * s))


if __name__ == '__main__':
    app.run()
