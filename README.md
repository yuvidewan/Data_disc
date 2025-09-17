# 🧭 Open Data Discovery & Insight Engine

### 🔎 Overview

The **Open Data Discovery & Insight Engine** is a tool designed to **find, explore, and analyze publicly available datasets**.

Millions of datasets exist online (Kaggle, World Bank, WHO, government portals), but discovering the right one is often time-consuming. This project solves that by:

* **Searching across multiple open data sources**
* **Previewing dataset contents instantly** (columns, sample rows, size)
* **Profiling data** (basic statistics, missing values, unique categories)
* **Visualizing patterns** (histograms, line plots, distributions)
* **Exporting & merging datasets** for further analysis
* (Future) **Providing automatic insights** using machine learning

---

### 🌍 Real-World Problem It Solves

Data is everywhere, but it’s not always accessible to non-experts.

* Students waste hours browsing Kaggle/government portals.
* Journalists/researchers struggle to quickly judge if a dataset is useful.
* Policymakers and NGOs need quick insights, not raw CSVs.

This project acts as a **data assistant** — making raw data **searchable, understandable, and usable**.

---

### ⚙️ Features (Planned Roadmap)

* ✅ Phase 1: CLI input/output setup (done)
* 🔄 Phase 2: Integrate Kaggle & open APIs for dataset discovery
* 📊 Phase 3: Dataset profiling (summary stats + sample rows)
* 📈 Phase 4: Basic visualization (plots & charts)
* 🔗 Phase 5: Dataset merging & export
* 🧠 Phase 6: Semantic search + basic ML insights
* 🌐 Phase 7: Web UI with Flask/FastAPI

---

### 🏗️ Project Structure

```
open-data-discovery/
│
├── src/              # Source code
│   ├── main.py       # Entry point
│   └── __init__.py
│
├── data/             # Downloaded datasets
│
├── notebooks/        # Jupyter experiments
│
├── tests/            # Unit tests
│
├── requirements.txt  # Dependencies
├── .gitignore        # Ignore unnecessary files
└── README.md         # Project documentation
```

---

### 🚀 Getting Started

#### 1. Clone Repo

```bash
git clone https://github.com/yuvidewan/Data_disc.git  
cd open-data-discovery
```

#### 2. Setup Virtual Environment

```bash
python -m venv env1
source env1/bin/activate  # Linux/Mac
env1\Scripts\activate     # Windows
pip install -r requirements.txt
```

#### 3. Run the Program

```bash
python src/main.py
```

Output:

```
🔎 Open Data Discovery Engine
Type 'exit' to quit.

Enter your query: rainfall in India
Searching for: rainfall in India
```

---

### 📦 Requirements

* Python 3.9+
* Libraries: `pandas`, `numpy`, `requests` (see `requirements.txt`)

---

### 💡 Example Use Cases

* *“Show me datasets about air pollution in India”*
* *“Find earthquake records in Asia since 2000”*
* *“Summarize health statistics datasets for 2020”*

---

### 👨‍💻 Author

**Yuvraj Dewan**
