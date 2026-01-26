# GenerativeAi

A collection of Machine Learning and Generative AI projects for the USDA Forest Service, focused on natural language processing, document analysis, and public comment processing.

## Projects

### Forest_Wizard

A Flask-based AI chatbot for answering questions about the USDA Forest Service.

| Component | Technology |
|-----------|------------|
| Backend | Flask (Python 3.9) |
| AI Provider | Azure OpenAI (GPT-3.5 Turbo) |
| NLP | NLTK |
| Container | Docker (Alpine Linux) |

**Features:**
- Forest Service-focused conversational AI
- Document upload and summarization
- Dual API support (Azure APIM / Direct OpenAI)
- CSRF protection

**Endpoints:**
- `/` - Chat UI
- `/ai/pipeline/chat` - Chat via Azure APIM
- `/openai/direct/chat` - Direct Azure OpenAI
- `/openai/direct/chat/pdf` - PDF/text summarization

---

### ML-007_SentimentAnalysis

A comprehensive pipeline for analyzing public comments submitted during NEPA environmental review periods. Processes data from the Forest Service's CARA (Comment Analysis and Response Application) system.

**Pipeline Stages:**

| Notebook | Purpose |
|----------|---------|
| `EMC_001_DataLtrParser` | Parse raw letter data from CARA exports |
| `EMC_002_DataAnalysis` | Validate projects against authoritative category codes |
| `EMC_003_DataComment_a_Prep` | Clean, tokenize, remove PII |
| `EMC_003_DataComment_b_Analysis` | Statistical analysis |
| `EMC_004_GenAI` | LLM-powered sentiment analysis & classification |

**AI Output Schema:**
```json
{
  "Sentiment": -0.5,
  "SentimentConfidence": 0.8,
  "Category": "Hydrology",
  "CitingLaw": true,
  "BriefSummary": "...",
  "SpecificFeedback": true,
  "ProposedResolution": "..."
}
```

**Categories:** Air Quality, Botany, Climate Change, Cultural/Heritage, Facilities, FireFuels, Fisheries, Hydrology, Lands/Special Uses, Minerals/Geology, NEPA/Proj Development, Recreation, Silviculture/Veg, SocioEconomic, Soils, Transportation, Wildlife, and more.

**Features:**
- Multi-environment support (GCP Vertex AI / Azure OpenAI)
- PII scrubbing (emails, phones, addresses, credit cards)
- Prompt injection defense
- Token management with recursive summarization
- Category validation against authoritative domain

---

### ML-MP-DocumentSummary

A Microsoft CoPilot-like meeting transcription analyzer for processing MS Teams VTT transcripts.

**Outputs:**
- Abstractive summaries
- Action items extraction
- Follow-up questions
- Unresolved questions
- Class/training session analysis
- Word clouds

**Notebooks:**

| Notebook | Purpose |
|----------|---------|
| `ML-MP-DocumentSummary.ipynb` | Main VTT transcript pipeline |
| `ML-MP-VTTSummary.ipynb` | Focused summarization |
| `ML-MP-VTTAnalysisOfAnalysis.ipynb` | Meta-analysis |

**Features:**
- Speaker diarization
- Multi-day/session processing
- Educational content analysis (timeline, curriculum, teaching methods)
- Theme extraction

---

### Other Projects

| Project | Description |
|---------|-------------|
| `ML-025_ResumeHRCIOAST` | HR/Resume processing |
| `ML-041_PHNExemption` | Exemption processing |
| `ML-042_SLP` | Speech/Language processing |
| `ML-Support` | Shared utilities and logging framework |
| `Speech_Text` | Speech-to-text functionality |

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| **AI/ML** | Azure OpenAI, Google Vertex AI (Gemini), TensorFlow, PyTorch |
| **NLP** | NLTK, spaCy, HuggingFace Transformers |
| **Data Science** | Pandas, NumPy, SciPy |
| **Visualization** | Matplotlib, WordCloud, Power BI |
| **Web** | Flask, Flask-WTF |
| **Container** | Docker |
| **Cloud** | GCP, Azure |

## Environment Setup

### Required Environment Variables

```bash
# Azure OpenAI
OPENAI_API_KEY=<your-azure-openai-key>
APIM_SUBSCRIPTION_KEY=<your-apim-key>
OPENAI_USFS_API_BASE=<endpoint-url>
OPENAI_USFS_API_KEY=<api-key>
OPENAI_USFS_API_VERSION=<api-version>

# GCP (if using Gemini)
GEMINI_USFS_API_KEY=<your-gemini-key>
```

### Local Development

```bash
# Clone the repository
git clone https://github.com/jvalenzano/GenerativeAi.git
cd GenerativeAi

# For Forest_Wizard
cd Forest_Wizard
pip install -r requirements.txt
python app.py

# For Jupyter notebooks
pip install jupyter
jupyter notebook
```

### Docker (Forest_Wizard)

```bash
docker build -t forest-wizard .
docker run -p 80:80 \
  -e OPENAI_API_KEY=<key> \
  -e APIM_SUBSCRIPTION_KEY=<key> \
  -e secret_key=<secret> \
  forest-wizard
```

## Data Sources

- **CARA System** - Forest Service Comment Analysis and Response Application
- **MS Teams** - VTT transcript exports
- **PDF/Text Documents** - Various document types for summarization

## Project Structure

```
GenerativeAi/
├── Forest_Wizard/          # Flask chatbot application
├── ML-007_SentimentAnalysis/   # NEPA comment analysis pipeline
├── ML-025_ResumeHRCIOAST/      # HR processing
├── ML-041_PHNExemption/        # Exemption processing
├── ML-042_SLP/                 # Speech/language processing
├── ML-MP-DocumentSummary/      # Meeting transcript analyzer
├── ML-Support/                 # Shared utilities
├── Speech_Text/                # Speech-to-text
├── shared/                     # Shared resources
├── .devcontainer/              # VS Code dev container config
├── .env_ai                     # AI environment config
├── .env_cloud                  # Cloud environment config
└── _config.yml                 # GitHub Pages config
```

## License

Internal USDA Forest Service use.

## Author

Jay Valenzano
