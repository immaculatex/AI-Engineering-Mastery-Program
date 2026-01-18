# High-Level Architecture

## Architecture Overview
The system is designed to run fully locally using Ollama as the LLM runtime.

---

## Components
1. **User Interface**
   - Command Line Interface (CLI)
   - Future scope: Web UI

2. **Application Layer**
   - Handles user prompts
   - Sends requests to the LLM

3. **LLM Runtime**
   - Ollama
   - Executes the selected LLM locally

4. **Model Layer**
   - llama3:8b (primary model)
   - mistral:7b (optional)

---

## Data Flow
1. User submits a query
2. Application layer processes input
3. Request sent to Ollama
4. LLM generates a response
5. Response returned to the user

---

## Non-Functional Considerations
- Performance: Depends on local hardware
- Security: No external data transfer
- Scalability: Single-user local system

---

## Future Enhancements
- REST API integration
- Document ingestion (RAG)
- Vector database support
