# 📄 PDF Summarizer & CV Analyzer

An intelligent PDF summarization tool that analyzes CV/resume documents using OpenAI's GPT model to evaluate candidates for software engineering positions, specifically for AWS event-driven systems.

## 🌟 Features

- **PDF Text Extraction**: Extracts text content from PDF documents using PyPDF2
- **AI-Powered Analysis**: Uses OpenAI's GPT model to analyze CV content
- **Structured Output**: Returns parsed data with candidate information, skills, and suitability assessment
- **Database Storage**: Stores analysis results in a local SQLite database
- **Candidate Evaluation**: Specifically evaluates candidates for senior software engineer roles in AWS event-driven systems

## 🛠️ Tech Stack

- **Python 3.12+**
- **OpenAI API** - For AI-powered document analysis
- **PyPDF2** - PDF text extraction
- **Pydantic** - Data validation and parsing
- **SQLite** - Local database storage (no installation required)
- **python-dotenv** - Environment variable management
- **uv** - Modern Python package manager

## 📁 Project Structure

```
PDF_summarise/
├── main.py                 # Main application entry point
├── pyproject.toml         # Project configuration and dependencies
├── uv.lock               # Dependency lock file
├── .env                  # Environment variables (create this)
├── pdf_summarizer.db     # SQLite database (auto-created)
├── pdfs/                 # Directory for PDF files
│   └── example-cv.pdf
└── utils/
    ├── __init__.py       # Package initialization
    ├── get_pdf_content.py # PDF text extraction
    ├── prompt.py         # AI prompt templates
    └── setup_db.py       # Database setup and operations
```

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd PDF_summarise
```

### 2. Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Install Dependencies

This project uses `uv` for dependency management:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

### 4. Run the Application

```bash
uv run main.py
```

## 💼 How It Works

### 1. **PDF Processing**
- User provides path to a CV/resume PDF file
- System extracts text content using PyPDF2
- Text is cleaned and prepared for AI analysis

### 2. **AI Analysis**
- Content is sent to OpenAI's GPT model with a specialized prompt
- AI analyzes the candidate's suitability for AWS event-driven system roles
- Extracts structured information: name, email, skills, experiences

### 3. **Data Validation**
- Uses Pydantic models to ensure data structure consistency
- Validates extracted information format

### 4. **Database Storage**
- Stores analysis results in local SQLite database
- No external database setup required

### 5. **Output**
```python
# Example output structure
{
    "name": "John Doe",
    "email": "john.doe@email.com",
    "skills": ["React.js", "AWS Lambda", "Node.js", "Python"],
    "experiences": ["5 years full-stack development", "AWS event-driven systems"],
    "summary": "Excellent fit for senior software engineer role...",
    "reasoning": [
        "Has React.js experience for frontend development",
        "Proven experience with AWS event-driven systems",
        "Strong backend development skills"
    ]
}
```

## 📊 Database Schema

The SQLite database stores candidate information in the following structure:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    skills TEXT,           -- JSON string of skills array
    experiences TEXT,      -- JSON string of experiences array
    summary TEXT,
    reasoning TEXT         -- JSON string of reasoning points
);
```

## 🔧 Configuration

### OpenAI Model Configuration
- Currently configured for GPT models
- Model can be changed in `main.py`
- Supports structured output parsing

### Prompt Customization
- Edit `utils/prompt.py` to modify analysis criteria
- Customize for different job roles or requirements
- Adjust evaluation parameters

## 📋 Usage Examples

### Basic Usage
```bash
$ uv run main.py
Enter the path to the PDF file: ./pdfs/candidate-cv.pdf
```

### Expected File Structure
```
pdfs/
├── john-doe-cv.pdf
├── jane-smith-resume.pdf
└── candidate-portfolio.pdf
```


## 🔒 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## 📈 Future Enhancements

- [ ] Support for multiple PDF formats
- [ ] Batch processing of multiple CVs
- [ ] Web interface for easier usage
- [ ] Export results to CSV/Excel
- [ ] Custom scoring algorithms
- [ ] Support for different job role templates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Important Notes

- **API Costs**: This application uses OpenAI's API which incurs costs per request
- **Privacy**: Ensure CV data is handled according to privacy regulations
- **Rate Limits**: Be aware of OpenAI API rate limits for production usage
- **Local Database**: SQLite database is created locally and might contain sensitive candidate information

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure you're using the correct Python environment with `uv`
2. **API Key Issues**: Verify your OpenAI API key is correctly set in `.env`
3. **PDF Reading Errors**: Ensure PDF files are not password-protected or corrupted
4. **Database Errors**: Check file permissions in the project directory

### Getting Help

- Check the error messages for specific issues
- Ensure all dependencies are installed with `uv sync`
- Verify your OpenAI API key has sufficient credits
- Make sure PDF files are readable and properly formatted

---

**Made with ❤️ for efficient CV analysis and candidate evaluation**
