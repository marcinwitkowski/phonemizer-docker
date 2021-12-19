#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, jsonify
from phonemizer.backend import EspeakBackend
from phonemizer.punctuation import Punctuation
from phonemizer.separator import Separator

app = Flask(__name__)


@app.route('/')
def home():
    txt = "złodziej"
    return jsonify({"output-text": use_phonemizer(txt)})


@app.route('/json', methods=['POST'])
def use_phonemizer(txt):
    text = Punctuation(';:,.!"?()-').remove(txt)
    words = {w.lower() for line in text for w in line.strip().split(' ') if w}
    backend = EspeakBackend('pl')
    separator = Separator(phone=' ', word=None)

    # build the lexicon by phonemizing each word one by one. The backend.phonemize
    # function expect a list as input and outputs a list.
    lexicon = {
        word: backend.phonemize([word], separator=separator, strip=True)[0]
        for word in words}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
