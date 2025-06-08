
# 🚀 check-software-version-for-citation

Ensures your GitHub **tag/release version** matches the version declared in:

✅ `CITATION.cff`  
✅ `pyproject.toml`  
✅ `codemeta.json`  
✅ `.zenodo.json`  
✅ `package.json`  
✅ `setup.py`

---

## 📦 What does it do?

🛡️ This GitHub Action automatically blocks a release or tag if the version in your GitHub tag/release does not match the version declared in your project files.

It helps you keep all your metadata **synchronized**, which is critical for:  
✅ reproducibility  
✅ citation tools  
✅ package managers  
✅ DOIs (Zenodo)  
✅ Python/JS packaging  

---

## 🎯 When does it run?

- On **push** of version tags (e.g. `v1.2.3`)
- On **published GitHub release**
- Can also be run **manually** via `workflow_dispatch`

---

## 🔍 What files does it check?

| File             | Always checked? | Optional flag |
|------------------|-----------------|---------------|
| `CITATION.cff`   | ✅ Yes          |               |
| `pyproject.toml` |                 | `check_pyproject_toml` |
| `codemeta.json`  |                 | `check_codemeta_json` |
| `.zenodo.json`   |                 | `check_zenodo_json` |
| `package.json`   |                 | `check_package_json` |
| `setup.py`       |                 | `check_setup_py` (via `python setup.py --version`) |

---

## 🛠 How to use

1️⃣ Add this action to your workflow:

```yaml
uses: your-org/check-software-version-for-citation@v1
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

| Input                | Description                                  | Default           |
|----------------------|----------------------------------------------|-------------------|
| `cff_path`           | Path to `CITATION.cff`                        | `CITATION.cff`    |
| `check_pyproject_toml`| Check `pyproject.toml`? (`true/false`)        | `false`           |
| `pyproject_toml_path`| Path to `pyproject.toml`                      | `pyproject.toml`  |
| `check_codemeta_json`| Check `codemeta.json`? (`true/false`)         | `false`           |
| `codemeta_json_path` | Path to `codemeta.json`                       | `codemeta.json`   |
| `check_zenodo_json`  | Check `.zenodo.json`? (`true/false`)          | `false`           |
| `zenodo_json_path`   | Path to `.zenodo.json`                        | `.zenodo.json`    |
| `check_package_json` | Check `package.json`? (`true/false`)          | `false`           |
| `package_json_path`  | Path to `package.json`                        | `package.json`    |
| `check_setup_py`     | Check `setup.py`? (`true/false`)              | `false`           |
| `setup_py_path`      | Path to `setup.py`                            | `setup.py`        |
| `event_name`         | GitHub event name (`push` or `release`)       | *(required)*      |
| `ref`                | GitHub ref (for `push`)                       | *(optional)*      |
| `release_tag`        | GitHub release tag name (for `release`)       | *(optional)*      |

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

If a mismatch occurs:

```
❌ Version mismatch with codemeta.json!
❌ One or more version mismatches detected:
- codemeta.json
```

---

## 💡 Why use this?

✅ Prevents **broken citations**  
✅ Keeps **version metadata consistent**  
✅ Avoids mismatches between **GitHub releases** and:
- package managers
- citation tools (Zenodo, CodeMeta, CFF)
- Python packaging
- JS packaging

---

## ✨ Future plans

- Support for **custom file matchers**
- Support for **multiple version fields** per file (for advanced use cases)

---

## 📜 License

Apache License 2.0 — free to use, fork, extend 🚀

---

## 🙏 Acknowledgements

Inspired by best practices for reproducible research and software citation!

---
