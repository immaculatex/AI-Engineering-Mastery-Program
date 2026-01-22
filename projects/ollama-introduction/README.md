# Self-Study: Introduction to Ollama – Install & Run Models

## Objective
To install Ollama, verify the setup, and download and run a small open-source language model locally using the Ollama command-line interface (CLI).

---

## 1. Installation & Initial Setup

### Action
Downloaded and installed Ollama on the local operating system (Windows, macOS, or Linux) using the official documentation.

### Resource
- Ollama Official Documentation  
- Search keywords used:
  - "Ollama official documentation"
  - "How to install Ollama"

### Installation Verification
Verified the installation using the following command:

```bash
ollama --version
```

Successful output confirmed that Ollama was installed correctly.

### Initial Test Command
Executed the initial test command to validate the setup:

```bash
ollama run llama3
```

This confirmed that Ollama can successfully pull and run a model locally.

---

## 2. Model Selection & Download

### Model Chosen
A small and popular open-source model was selected:
- **llama3:8b**
- *(Alternative: mistral:7b)*

### Model Download
Downloaded the model using the Ollama CLI:

```bash
ollama pull llama3:8b
```

### Running the Model
Ran the downloaded model locally:

```bash
ollama run llama3:8b
```

The model launched successfully and responded to prompts via the terminal.

---

## Outcome
- ✔ Ollama installed successfully
- ✔ Installation verified using CLI
- ✔ Open-source model downloaded
- ✔ Model executed locally

---

## Key Takeaway
This exercise demonstrates how open-source large language models can be installed and run locally using Ollama with minimal setup and no cloud dependency.

---

## Author
Immaculate Xavier  
AI Engineering Mastery – Self Study
