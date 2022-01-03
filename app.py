import os
import re
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    txt = "test"
    return jsonify({"output-text": txt})


@app.route('/post', methods=['POST'])
def post_route():
    if request.method == 'POST':

        data = request.get_json(force=True)
        txt = data['text']

        out = []
        for t in txt:
            temp = use_phonemizer(t)
            temp = re.sub(r'[^\w]', ' ', temp)
            out.append(temp)
        print('Data Received: "{data}"'.format(data=data))
        return jsonify({"output-text": out})


def use_phonemizer(txt, language="pl", backend='espeak'):
    shell_cmd = f"\
        echo '{txt}' | phonemize -b {backend} -l {language} -p ' ' -w '|' --words-mismatch ignore \
    "
    output = os.popen(shell_cmd).read()
    return output


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# curl 172.17.0.2:5000/post -d '{"text": ["Andrzej", "traktor", "Szekspir"]}' -H 'Content-Type: application/json'
