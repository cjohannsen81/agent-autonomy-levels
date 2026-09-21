# Contributing

Feedback is most useful in these forms:

- **Deployment experience**: a use case, the level you chose, and whether the controls and thresholds held up.
- **Mapping corrections**: cite the OWASP or ISO text you are comparing against.
- **Implementations**: add `implementations/<name>.md` mapping AL-01 to AL-16 to your product's mechanisms, with how each is verified.

Before opening a pull request, run:

```bash
pip install pyyaml jsonschema pytest
cd tools && python -m pytest -q
```

Changes to level definitions or control IDs need an issue first, since certificates reference them.
