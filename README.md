## 📥 Mangadex Downloader

A CLI tool to download manga chapters (solo or bulk) from MangaDex.

### 🪐 Features

- Bulk download multiple chapters at once.
- Choose specific chapters interactively.
- Supports multiple languages.
- Saves all chapter pages as images inside a .zip archive.
- Automatically sanitizes filenames.

### 🧩 Requirements

- Python `3.7` or higher

Dependencies are automatically installed with `pip`:

- `requests`
- `tqdm`
- `questionary`

### 🚀 Installation

```bash
pip install mangadex-dl
```

> 🔒 Make sure you have Python 3.7+ and pip installed.

### 💎 Supported Languages

| Code               | Language                    |
|--------------------|-----------------------------|
| `ar`               | Arabic                      |
| `de`               | German                      |
| `en`               | English                     |
| `es`               | Spanish                     |
| `es-la`            | Spanish (Latin America)     |
| `fr`               | French                      |
| `id`               | Indonesian                  |
| `it`               | Italian                     |
| `ko`               | Korean                      |
| `pt`               | Portuguese (Portugal)       |
| `pt-br`            | Portuguese (Brazil)         |
| `ru`               | Russian                     |
| `tr`               | Turkish                     |
| `uk`               | Ukrainian                   |
| `vi`               | Vietnamese                  |
| `zh`               | Chinese                     |

### ✨ Usage

Once installed, run the command:

```bash
mangadex-dl
```

You’ll be prompted with two modes:

- **Solo** → Download by chapter ID.
- **Bulk** → Download by manga ID and select chapters from an interactive list.

The result will be `.zip` archives containing clean, ordered images of the manga chapter(s).

### ❓ Example

**Solo Mode** (Chapter ID):

```md
Enter Chapter ID: cd0dbfeb-3e6b-4f93-907c-8b2e71b41ae2
```

This will save the chapter as:

```md
chapter-1-en.zip
```

**Bulk Mode** (Manga ID):

```md
Enter Manga ID: 559c5fc6-6a57-43a6-93cb-b43328bc1957
```

Then select chapters interactively, e.g.:

```md
✔ Chapter 1 [English]
✔ Chapter 1 [Arabic]
✔ Chapter 2 [English]
```

Files will be saved like:

```md
chapter-1-en.zip
chapter-1-ar.zip
chapter-2-en.zip
```

### 📜 License

This project is available under the [MIT License](LICENSE).