# Python Full-Stack AI Engineer Portfolio

Welcome to my comprehensive Python portfolio showcasing advanced AI/ML implementations, full-stack development skills, and mastery of Python fundamentals. This repository demonstrates expertise in building production-ready AI applications with modern technologies.

## 🚀 Featured Projects

### 1. **LangGraph Memory System** (`langGraph/`)
Advanced conversational AI with persistent memory using LangGraph, mem0, and Qdrant vector database.

**Key Features:**
- Long-term memory storage with vector embeddings
- Context-aware conversations using OpenAI GPT-4o
- Qdrant vector store for semantic search
- Memory retrieval and injection into system prompts

**Technologies:** LangGraph, mem0, Qdrant, OpenAI, text-embedding-3-small, Docker

### 2. **RAG Queue System** (`rag_queue/`)
Production-ready Retrieval-Augmented Generation system with asynchronous job processing.

**Key Features:**
- Redis Queue (RQ) for background job processing
- FastAPI REST API for query submission
- Qdrant vector store for document retrieval
- PDF document indexing with metadata
- Asynchronous job status tracking

**Technologies:** FastAPI, Redis Queue, LangChain, Qdrant, OpenAI Embeddings, Uvicorn, Docker

### 3. **Weather AI Assistant** (`weatherAPI/`)
AI-powered weather assistant with Chain of Thought reasoning and tool calling.

**Key Features:**
- Chain of Thought reasoning with structured JSON output
- Tool calling for weather data retrieval
- Groq API integration with Llama-3.3-70b
- Pydantic models for structured output validation
- System command execution capabilities

**Technologies:** Groq API, Pydantic, Chain of Thought, Tool Calling, FastAPI

### 4. **Multi-Model AI Integration** (`helloWWorld/`)
Comprehensive exploration of AI prompting techniques and model integrations.

**Key Features:**
- OpenAI to Gemini API migration
- Chain of Thought (COT) reasoning implementation
- Few-shot prompting techniques
- Persona-based AI systems
- Automated reasoning workflows

**Technologies:** OpenAI, Google Gemini API, JSON structured outputs

### 5. **Ollama FastAPI Integration** (`ollama/`)
Local LLM deployment with FastAPI wrapper.

**Key Features:**
- FastAPI REST endpoints
- Ollama integration for local inference
- Contact management system

**Technologies:** FastAPI, Ollama

## 📚 Python Mastery Modules

### **Object-Oriented Programming** (`oops/`)
Comprehensive OOP implementations including:
- Class inheritance and polymorphism
- Property decorators and getters/setters
- Static methods and class methods
- Access control and encapsulation

### **Advanced Python Concepts**
- **Comprehensions** (`comprehensions/`): List, dictionary, set, and generator comprehensions
- **Generators** (`generators/`): Generator functions, yield statements, infinite generators
- **Decorators** (`decorators/`): Authentication decorators, logging decorators, function wrapping
- **Functions** (`function/`): Lambda functions, closures, scope, multiple returns, built-in functions
- **Data Structures** (`datatypes/`): Advanced list operations, dictionaries, sets, strings, tuples
- **Control Flow** (`loops/`): Advanced loop patterns and iterations
- **Exception Handling** (`exceptionHandling/`): Try-catch patterns, custom exceptions

## 🛠️ Technical Stack

### **AI/ML Technologies**
- **LLM Integration:** OpenAI (GPT-4o, GPT-3.5-turbo), Google Gemini, Groq (Llama-3.3-70b)
- **Frameworks:** LangGraph, LangChain, mem0
- **Vector Databases:** Qdrant
- **Embeddings:** OpenAI text-embedding-3-small, text-embedding-3-large

### **Backend Development**
- **Web Frameworks:** FastAPI
- **Task Queues:** Redis Queue (RQ)
- **API Design:** RESTful APIs, async/await patterns
- **Validation:** Pydantic models
- **Server:** Uvicorn

### **DevOps & Infrastructure**
- **Containerization:** Docker, Docker Compose
- **Environment Management:** python-dotenv
- **Version Control:** Git

### **Python Proficiency**
- **Advanced Concepts:** Generators, decorators, comprehensions, closures
- **OOP:** Inheritance, polymorphism, encapsulation
- **Functional Programming:** Lambda, map/filter/reduce
- **Error Handling:** Exception patterns, custom exceptions

## 🎯 Key Skills Demonstrated

1. **AI/ML Engineering**
   - RAG system architecture
   - Memory management in AI systems
   - Chain of Thought reasoning
   - Tool calling and function execution
   - Multi-model API integration

2. **Full-Stack Development**
   - RESTful API design
   - Asynchronous job processing
   - Database integration
   - Container orchestration

3. **Software Engineering**
   - Clean code principles
   - Modular architecture
   - Environment configuration
   - Error handling and validation

4. **Python Mastery**
   - Advanced Python features
   - Design patterns
   - Performance optimization
   - Best practices

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/AmishaKri/Python-FullStack-Notes-with-project.git

# Navigate to project directory
cd Python-FullStack-Notes-with-project

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🏃 Running Projects

### LangGraph Memory System
```bash
cd langGraph
docker-compose up -d  # Start Qdrant
python memo.py
```

### RAG Queue System
```bash
cd rag_queue
docker-compose up -d  # Start Redis and Qdrant
python main.py
```

### Weather AI Assistant
```bash
cd weatherAPI
python weather.py
```

### AI Prompting Examples
```bash
cd helloWWorld
python openAIToGemini.py
python COT.py
```

## 🔧 Configuration

Create `.env` files in respective project directories:

```env
# For AI projects
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_gemini_key
```

## 📊 Project Statistics

- **Total Projects:** 5+ production-ready AI applications
- **Python Modules:** 8+ comprehensive learning modules
- **Lines of Code:** 2000+
- **Technologies Used:** 15+
- **API Integrations:** 3+ LLM providers

## 🤝 Contributing

This is a personal portfolio repository showcasing my skills. Feel free to explore the code and reach out for collaborations!

## 📞 Contact

- **Email:** amishagwp123@gmail.com
- **GitHub:** [AmishaKri](https://github.com/AmishaKri)

## 🎓 Learning Journey

This repository represents my journey from Python fundamentals to advanced AI engineering. Each module demonstrates progressive skill development, from basic data structures to complex AI systems with memory, reasoning, and tool integration.

---

**Built with passion for AI and Python excellence** 🚀
