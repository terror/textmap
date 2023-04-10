### textmap

Playing around with heatmap-like visualizations for text-based content.

![Screenshot 2023-04-10 at 7 22 18 PM](https://user-images.githubusercontent.com/31192478/231017843-0adcd27b-5464-4a2e-8056-8abb63ed9d7c.png)

### Development

Install dependencies:

```
$ poetry install
$ python3 -m spacy download en_core_web_sm
```

_n.b. The second line is optional if you already have the model installed._

Launch a shell:

```
$ poetry shell
```

Finally, run the server:

```
$ python3 app.py
```

You can now navigate to `http://127.0.0.1:5000`.
