<a href="https://github.com/kennethenevoldsen/augmenty"><img src="https://github.com/KennethEnevoldsen/augmenty/blob/main/img/icon.png?raw=true" width="200" align="right" /></a>
# Augmenty: The cherry on top of your NLP pipeline


[![PyPI version](https://badge.fury.io/py/augmenty.svg)](https://pypi.org/project/augmenty/)
[![python version](https://img.shields.io/badge/Python-%3E=3.8-blue)](https://github.com/kennethenevoldsen/augmenty)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)]([ruff])
[![github actions pytest](https://github.com/kennethenevoldsen/augmenty/actions/workflows/tests.yml/badge.svg)](https://github.com/kennethenevoldsen/augmenty/actions)
[![github actions docs](https://github.com/kennethenevoldsen/augmenty/actions/workflows/documentation.yml/badge.svg)]([action])
[![status](https://joss.theoj.org/papers/df84463b79f27f40a4da97f20b08a958/status.svg)]([joss])

[action]: https://kennethenevoldsen.github.io/augmenty/
[ruff]: https://github.com/astral-sh/ruff
[joss]: https://joss.theoj.org/papers/df84463b79f27f40a4da97f20b08a958


Augmenty is an augmentation library based on spaCy for augmenting texts. Besides a wide array of highly flexible augmenters, Augmenty provides a series of tools for working with augmenters, including combining and moderating augmenters. Augmenty differs from other augmentation libraries in that it corrects (as far as possible) the assigned labels under the augmentation, thus making many of the augmenters valid for training in a wider range of tasks.

## 🔧 Installation
To get started using augmenty simply install it using pip by running the following line in your terminal:

```
pip install augmenty
```

Do note that this is a minimal installation. As some augmenters requires additional packages please write the following line to install all dependencies.

```
pip install "augmenty[all]"
```

For more detailed instructions on installing augmenty, including specific language support, see the [installation instructions](https://kennethenevoldsen.github.io/augmenty/installation).

## 🍒 Simple Example
The following shows a simple example of how you can quickly augment text using Augmenty. For more on using augmenty see the [usage guides].

```python
import augmenty
import spacy

nlp = spacy.load("en_core_web_md")
# if not installed run: python -m spacy download en_core_web_md

doc = nlp("Augmenty is a great tool for text augmentation")

# check that the pipeline detects the entities (this done by SpaCy and is not a 100%)
print(doc.ents)
# (Augmenty,) is detected as an entity

doc.ents[0].label_
# 'GPE'. Depending on the model, the label might be different (e.g. 'ORG')

entity_augmenter = augmenty.load(
    "ents_replace_v1", ent_dict={"GPE": [["spaCy"], ["spaCy", "Universe"]]}, # label=GPE,
    level=1
)

for augmented_doc in augmenty.docs([doc], augmenter=entity_augmenter, nlp=nlp):
    print(augmented_doc)
```

```
spaCy Universe is a great tool for text augmentation.
```

## 📖 Documentation

| Documentation              |                                                                             |
| -------------------------- | --------------------------------------------------------------------------- |
| 📚 **[Usage Guides]**       | Guides and instructions on how to use augmenty and its features.            |
| 📰 **[News and changelog]** | New additions, changes and version history.                                 |
| 🎛 **[API References]**     | The detailed reference for augmenty's API. Including function documentation |
| 🍒 **[Augmenters]**         | Contains a full list of current augmenters in augmenty.                     |
| 🙋 **[FAQ]**                | Frequently asked question regarding augmenty                                |
| 🤝 **[How to contribute]**  | How to contribute to augmenty                                               |

[usage guides]: https://kennethenevoldsen.github.io/augmenty/tutorials/introduction.html
[api references]: https://kennethenevoldsen.github.io/augmenty/
[Augmenters]: https://kennethenevoldsen.github.io/augmenty/augmenters_overview.html
[Demo]: https://share.streamlit.io/kennethenevoldsen/augmenty/dev/streamlit.py
[News and changelog]: https://kennethenevoldsen.github.io/augmenty/news.html
[FAQ]: https://kennethenevoldsen.github.io/augmenty/faq.html
[How to contribute]: CONTRIBUTING.md

## 💬 Where to ask questions

| Type                           |                        |
| ------------------------------ | ---------------------- |
| 🚨 **Bug Reports**              | [GitHub Issue Tracker] |
| 🎁 **Feature Requests & Ideas** | [GitHub Issue Tracker] |
| 👩‍💻 **Usage Questions**          | [GitHub Discussions]   |
| 🗯 **General Discussion**       | [GitHub Discussions]   |
| 🍒 **Adding an Augmenter**      | [Adding an augmenter]  |

[github issue tracker]: https://github.com/kennethenevoldsen/augmenty/issues
[github discussions]: https://github.com/kennethenevoldsen/augmenty/discussions
[Adding an augmenter]: https://kennethenevoldsen.github.io/augmenty/adding_an_augmenter.html

