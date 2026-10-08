\# DevForge AI



\### Autonomous AI Software Development System



DevForge AI is an \*\*autonomous AI-powered software development system\*\* designed to transform natural-language software requirements into a structured development workflow.



It uses specialized AI agents for:



\* Requirement analysis

\* Project planning

\* Architecture design

\* Code generation

\* Automated testing

\* Bug detection

\* Debugging

\* Re-testing



The system can automatically detect testing failures, send the project to the Debugger Agent, apply fixes, and run testing again until the workflow reaches a passing state.



\---



\## Key Features



\* Autonomous multi-agent software development

\* AI-powered requirement analysis

\* Automatic project planning

\* Software architecture generation

\* AI-based code generation

\* Automated testing

\* Automatic bug detection and debugging

\* Self-correction and re-testing loop

\* Gemini-powered AI agents

\* LangGraph-based workflow orchestration



\---



\## Autonomous Workflow



```text

User Requirement

&#x20;      |

&#x20;      v

Requirement Agent

&#x20;      |

&#x20;      v

Planning Agent

&#x20;      |

&#x20;      v

Architect Agent

&#x20;      |

&#x20;      v

Developer Agent

&#x20;      |

&#x20;      v

Testing Agent

&#x20;      |

&#x20;      +------ PASS ------> Completed

&#x20;      |

&#x20;      +------ FAIL

&#x20;              |

&#x20;              v

&#x20;       Debugger Agent

&#x20;              |

&#x20;              v

&#x20;       Testing Agent

&#x20;              |

&#x20;              +------ PASS ------> Completed

&#x20;              |

&#x20;              +------ FAIL ------> Debugger

```



\---



\## AI Agents



| Agent             | Responsibility                                   |

| ----------------- | ------------------------------------------------ |

| Requirement Agent | Analyzes and structures user requirements        |

| Planning Agent    | Creates the software development plan            |

| Architect Agent   | Designs the system architecture                  |

| Developer Agent   | Generates application code                       |

| Testing Agent     | Generates tests and evaluates the implementation |

| Debugger Agent    | Identifies bugs and applies fixes                |



\---



\## Self-Correction Loop



One of the main capabilities of DevForge AI is its \*\*automatic debugging loop\*\*.



When the Testing Agent detects failures:



```text

Testing

&#x20;  |

&#x20;  v

FAIL

&#x20;  |

&#x20;  v

Debugger

&#x20;  |

&#x20;  v

Fix Issues

&#x20;  |

&#x20;  v

Testing Again

&#x20;  |

&#x20;  v

PASS

```



This allows the system to automatically move from \*\*development → testing → debugging → re-testing\*\*.



\---



\## Technology Stack



\* \*\*Python\*\*

\* \*\*Google Gemini API\*\*

\* \*\*LangGraph\*\*

\* \*\*LangChain\*\*

\* \*\*Pydantic\*\*

\* \*\*Git \& GitHub\*\*



The generated application can also contain technologies such as:



\* Node.js

\* JavaScript

\* Backend APIs

\* Database components



depending on the requirements provided to DevForge AI.



\---



\## Project Structure



```text

devforge-ai/

|

+-- agent.py

+-- requirements.txt

+-- test\_config.py

+-- test\_debugger.py

+-- test\_gemini.py

|

+-- agents/

|   +-- architect/

|   |   +-- agent.py

|   |   +-- test\_agent.py

|   |

|   +-- debugger/

|   |   +-- agent.py

|   |

|   +-- developer/

|   |   +-- agent.py

|   |   +-- test\_agent.py

|   |

|   +-- planning/

|   |   +-- agent.py

|   |   +-- test\_agent.py

|   |

|   +-- requirement/

|   |   +-- agent.py

|   |   +-- test\_agent.py

|   |

|   +-- testing/

|       +-- agent.py

|       +-- test\_agent.py

|

+-- core/

|   +-- config/

|   |   +-- settings.py

|   |

|   +-- orchestrator/

|   |   +-- workflow.py

|   |   +-- test\_workflow.py

|   |

|   +-- state/

|       +-- agent\_state.py

|

+-- models/

|   +-- test\_config.py

|

+-- backend/

&#x20;   +-- main.py

```



\---



\## Installation



\### 1. Clone the Repository



```bash

git clone https://github.com/harishmishra666/devforge-ai.git

cd devforge-ai

```



\### 2. Create a Virtual Environment



Windows:



```powershell

python -m venv venv

```



Activate it:



```powershell

venv\\Scripts\\activate

```



\### 3. Install Dependencies



```powershell

pip install -r requirements.txt

```



\### 4. Configure Gemini API



Create the required `.env` file and add your Gemini API key:



```env

GEMINI\_API\_KEY=your\_api\_key\_here

```



\*\*Never commit your real API key to GitHub.\*\*



\---



\## Run DevForge AI



After activating the virtual environment and configuring the API key:



```powershell

python -m core.orchestrator.test\_workflow

```



The system will execute the autonomous development workflow.



\---



\## Example Workflow Result



DevForge AI has been tested through a complete autonomous development cycle:



```text

Requirement

&#x20;   |

Planning

&#x20;   |

Architect

&#x20;   |

Developer

&#x20;   |

Testing

&#x20;   |

&#x20; FAIL

&#x20;   |

Debugger

&#x20;   |

Testing

&#x20;   |

&#x20; PASS

&#x20;   |

Completed

```



During testing, the system successfully demonstrated automatic failure detection, debugging, fixing, and re-testing.



\---



\## Security



DevForge AI uses environment variables for API credentials.



Sensitive files such as:



```text

.env

\*.env

venv/

.venv/

\_\_pycache\_\_/

\*.pyc

```



are excluded through `.gitignore`.



\*\*Never upload API keys, passwords, tokens, or other secrets to GitHub.\*\*



\---



\## Future Roadmap



Planned improvements include:



\* More specialized AI agents

\* Improved code generation

\* Better automated testing

\* Advanced debugging strategies

\* Persistent project memory

\* Multi-model support

\* Web-based DevForge AI interface

\* GitHub automation

\* CI/CD integration

\* Advanced RAG-based project knowledge

\* Human-in-the-loop approval workflows



\---



\## Author



\### Harish Mishra



\*\*AI \& Automation | Agentic AI | Generative AI | Python\*\*



DevForge AI is an exploration of autonomous AI agents and intelligent software engineering workflows.



\---



\## License



This project is currently intended as a personal AI engineering and research project.



\---



\## GitHub



Repository:



https://github.com/harishmishra666/devforge-ai



