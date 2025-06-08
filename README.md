
# 🚀 version-consistency

Automatically ensures your GitHub tag or release version matches the version declared in your project's key metadata files.

---

## 📦 What does it do?

🛡️ This GitHub Action **blocks a release or tag** if the version in your GitHub tag/release does not match the version declared in your project files.

Helps ensure:
✅ Reproducibility  
✅ Correct citations  
✅ Consistent packaging metadata  
✅ Accurate DOIs (Zenodo)  
✅ Cross-language version consistency (Python / JS / metadata)

---

## 🎯 When does it run?

- On **push** of version tags (e.g. `v1.2.3`)
- On **published GitHub release**
- Can also be run **manually** via `workflow_dispatch`

---

## 📋 Features

✅ Canonical tag version parsing (PEP 440)  
✅ Compare GitHub tag/release version to:

- `CITATION.cff`
- `pyproject.toml`
- `setup.py`
- `codemeta.json`
- `.zenodo.json`
- `package.json`

✅ Cross-language support (Python, JS, metadata)  
✅ Blocks incorrect GitHub releases/tags  
✅ Runs on push, release, or manual trigger  
✅ Lightweight, pure Python — no third-party services  
✅ Easy to configure via GitHub Action inputs  
✅ Suitable for reproducible research and software citation best practices

---

## 🔍 What files does it check?

| File             | Parser used |
|------------------|-------------|
| `CITATION.cff`   | PEP 440 |
| `pyproject.toml` | PEP 440 |
| `setup.py`       | PEP 440 |
| `package.json`   | Strict SemVer (converted from canonical PEP 440 tag) |
| `codemeta.json`  | PEP 440 |
| `.zenodo.json`   | PEP 440 |

---

## 🛠 How to use

```yaml

jobs:
  check-version:
    name: Check version consistency
    runs-on: ubuntu-latest

    steps:
      - name: Run version-consistency
        uses: willynilly/version-consistency@v1.0.0
        with:
          event_name: ${{ github.event_name }}
          ref: ${{ github.ref }}
          release_tag: ${{ github.event.release.tag_name }}

          check_pyproject_toml: true
          pyproject_toml_path: python/pyproject.toml
        
          check_codemeta_json: true
          codemeta_json_path: metadata/codemeta.json
        
          check_zenodo_json: true
          zenodo_json_path: metadata/.zenodo.json
        
          check_package_json: true
          package_json_path: web/package.json
        
          check_setup_py: true
          setup_py_path: python/setup.py
```

---

## ⚙️ Inputs

| Input                          | Description                             | Default           |
|-------------------------------|-----------------------------------------|-------------------|
| `cff_path`                     | Path to `CITATION.cff`                   | `CITATION.cff`    |
| `check_pyproject_toml`         | Check `pyproject.toml`? (`true/false`)   | `false`           |
| `pyproject_toml_path`          | Path to `pyproject.toml`                 | `pyproject.toml`  |
| `check_codemeta_json`          | Check `codemeta.json`? (`true/false`)    | `false`           |
| `codemeta_json_path`           | Path to `codemeta.json`                  | `codemeta.json`   |
| `check_zenodo_json`            | Check `.zenodo.json`? (`true/false`)     | `false`           |
| `zenodo_json_path`             | Path to `.zenodo.json`                   | `.zenodo.json`    |
| `check_package_json`           | Check `package.json`? (`true/false`)     | `false`           |
| `package_json_path`            | Path to `package.json`                   | `package.json`    |
| `check_setup_py`               | Check `setup.py`? (`true/false`)         | `false`           |
| `setup_py_path`                | Path to `setup.py`                       | `setup.py`        |
| `event_name`                   | GitHub event name (`push` or `release`)  | *(required)*      |
| `ref`                          | GitHub ref (for `push`)                  | *(optional)*      |
| `release_tag`                  | GitHub release tag name (for `release`)  | *(optional)*      |

---

## 🚦 Example workflow trigger

```yaml
on:
  push:
    tags:
      - 'v*.*.*'
  release:
    types: [published]
```

---

## 💥 Example output

```
📦 Detected release tag version: 1.2.3
📖 CITATION.cff version: 1.2.3
📖 pyproject.toml version: 1.2.3
📖 codemeta.json version: 1.2.3
📖 .zenodo.json version: 1.2.3
📖 package.json version: 1.2.3
📖 setup.py version: 1.2.3
✅ All versions match!
```

---

## 🔍 Comparisons with similar tools

| Tool / Action | Scope / Limitations |
|---------------|--------------------|
| [`check-version`](https://github.com/marketplace/actions/check-version) | Typically compares only `package.json` or `pyproject.toml` to Git tag |
| [`validate-version-tag-action`](https://github.com/marketplace/actions/validate-version-tag-action) | Focused on NPM (`package.json` only), no support for Python or metadata files |
| [`python-semantic-release`](https://python-semantic-release.readthedocs.io/) | Automated release tool — not designed for cross-file version consistency checking |
| `check-tag-version` (various community actions) | Usually limited to one file — no multi-ecosystem, no citation support |

✅ **`version-consistency` is currently the only GitHub Action that provides:**

- Canonical **PEP 440 tag version parsing**
- Cross-ecosystem validation:
    - Python (`pyproject.toml`, `setup.py`)
    - JavaScript (`package.json`)
    - Citation / metadata (`CITATION.cff`, `codemeta.json`, `.zenodo.json`)
- Ability to **block incorrect releases** directly in GitHub CI
- Lightweight, non-invasive — designed to fit **any workflow**

---

## 💡 Why use this?

✅ Prevents **broken citations**  
✅ Keeps **version metadata consistent**  
✅ Avoids mismatches between **GitHub releases** and:
- Python packaging
- JS packaging
- Citation metadata

---

## 📜 License

Apache License 2.0 — free to use, fork, extend 🚀

---

## 🙏 Acknowledgements

Inspired by best practices for reproducible research and software citation!

---
