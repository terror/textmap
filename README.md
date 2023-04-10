### textmap

Playing around with heatmap-like visualizations for text-based content.

![](https://files.catbox.moe/fr34s2.png)

### Development

Install dependencies:

```
$ poetry install
$ python3 -m spacy download en_core_web_sm
```

_n.b. The second line is optional if you already have to model installed._

Launch a shell:

```
$ poetry shell
```

Finally, run the server:

```
$ python3 app.py
```

You can now navigate to `http://127.0.0.1:5000`.
