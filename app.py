import dataclasses
import json
import typing as t
from dataclasses import dataclass

import numpy as np
import spacy
from flask import Flask, jsonify, render_template, request

MODEL = spacy.load('en_core_web_sm')

@dataclass
class Phrase:
  score: float
  text: str

@dataclass
class Document:
  phrases: t.List[Phrase]

class EnhancedJSONEncoder(json.JSONEncoder):
  def default(self, o):
    if dataclasses.is_dataclass(o):
      return dataclasses.asdict(o)
    return super().default(o)

def cosine_similarity(a, b):
  return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def textmap(text: str) -> Document:
  doc = MODEL(text)

  sentences = [sent.text for sent in doc.sents]

  return Document([
    Phrase(float(score), sent) for sent,
    score in list(
      zip(
        sentences,
        [
          cosine_similarity(sent_emb, doc.vector)
          for sent_emb in [MODEL(sent).vector for sent in sentences]
        ]
      )
    )
  ])

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/map', methods=['POST'])
def map():
  return jsonify(
    json.dumps(
      textmap(request.get_data(as_text=True)), cls=EnhancedJSONEncoder
    ),
  )

if __name__ == '__main__':
  app.run(debug=True)
