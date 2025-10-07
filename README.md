## 🛸 Mangadex Downloader

A sleek CLI tool to download single or multiple manga chapters from MangaDex with ease.

### 🪐 Features

- Bulk download multiple chapters at once.
- Choose specific chapters interactively.
- Supports multiple languages.
- Saves chapter pages inside a `.zip` or `.cbz` archive.
- Lets you choose archive format (ZIP or CBZ).
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
| `bg`               | Bulgarian                   |
| `de`               | German                      |
| `en`               | English                     |
| `es`               | Spanish                     |
| `es-la`            | Spanish (Latin America)     |
| `fr`               | French                      |
| `id`               | Indonesian                  |
| `it`               | Italian                     |
| `ko`               | Korean                      |
| `nl`               | Dutch                       |
| `pl`               | Polish                      |
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

You'll also be asked to choose the archive format:

- **zip** → A standard ZIP archive.
- **cbz** → A ZIP archive with a `.cbz` extension.

The result will be `.zip` or `.cbz` archives containing clean, ordered images of the manga chapter(s).

### ❓ Example

**Solo Mode** (Chapter ID):

```md
Enter Chapter ID: 2c580bdd-0b72-4734-8c11-8a47d7525c7f
```

This will save the chapter as:

```md
chapter-[number]-[lang].zip
```

**Bulk Mode** (Manga ID):

```md
Enter Manga ID: d1a9fdeb-f713-407f-960c-8326b586e6fd
```

It will ask you to select 1 or more languages:

```md
Select Languages:
✔ ar - Arabic
✔ bg - Bulgarian
✔ de - German
✔ en - English
...
```

You’ll then be asked:

```md
Include NSFW? (Default is No)
```

- Select `Yes` to include mature chapters.
- Select `No` to only include safe chapters.

Then select chapters, e.g.:

```md
✔ Chapter 1 [English]
✔ Chapter 1 [Arabic]
✔ Chapter 2 [English]
...
```

Files will be saved like:

```md
chapter-1-en.zip
chapter-1-ar.zip
chapter-2-en.zip
```

### 📜 License

This project is available under the [MIT License](LICENSE).