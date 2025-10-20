# Sales Data Analysis Project

A professional data science project demonstrating Git, GitHub, Jupyter, and Docker skills.

## Project Overview
This project analyzes sales data to uncover insights about:
- Revenue trends over time
- Top-performing products and regions
- Sales quantity patterns

## Technologies Used
- **Python**: Data processing and analysis
- **Jupyter**: Interactive notebooks
- **Docker**: Containerized environment
- **Git/GitHub**: Version control

## Quick Start

### Using Docker (Recommended)
```bash
docker-compose up --build
```
Then open: http://localhost:8888

### Without Docker
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

## Project Structure
```
sales-analysis/
├── notebooks/          # Jupyter analysis notebooks
├── data/              # Data files (gitignored)
├── src/               # Python modules
├── Dockerfile         # Docker container definition
└── docker-compose.yml # Docker orchestration
```

## Author
Assad - GitHub: @assadKhurshid