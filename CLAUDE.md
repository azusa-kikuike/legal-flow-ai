# Claude Instructions

## Project Overview
This is a legal flow AI project built with Agent Development Kit (ADK) that appears to handle legal article parsing and agent-based workflows.

## Development Commands
- `make install` - Install dependencies using uv
- `make test` - Run unit and integration tests
- `make playground` - Start the agent playground on port 8501
- `make backend` - Export dependencies and run the agent engine app
- `make lint` - Run code quality checks (codespell, ruff, mypy)
- `make setup-dev-env` - Set up development environment with Terraform
- `uv run streamlit run streamlit_app.py` - Start the Streamlit Web UI for legal document analysis

## Code Quality
Always run `make lint` after making changes to ensure code quality standards are met.

## Project Structure
- `app/` - Main application code
  - `agent.py` - Core agent implementation
  - `agent_engine_app.py` - Agent engine application
  - `utils/` - Utility modules (GCS, tracing, typing)
- `tests/` - Test suites (unit, integration, load tests)
- `notebooks/` - Jupyter notebooks for testing and evaluation
- `deployment/` - Infrastructure and deployment configurations

## Dependencies
This project uses `uv` for dependency management. The main dependencies are defined in `pyproject.toml`.