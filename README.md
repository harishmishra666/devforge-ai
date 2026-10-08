# DevForge AI



### Autonomous AI Software Development System



DevForge AI is an autonomous AI-powered software development system that transforms natural-language software requirements into a structured software development workflow.



It uses specialized AI agents for requirement analysis, planning, architecture, code generation, testing, debugging, and re-testing.



The system can detect testing failures, send the project to a Debugger Agent, apply fixes, and run testing again.



---



## Key Features



* Autonomous multi-agent software development

* AI-powered requirement analysis

* Automatic project planning

* Software architecture generation

* AI-based code generation

* Automated testing

* Automatic bug detection and debugging

* Self-correction and re-testing loop

* Gemini-powered AI agents

* LangGraph-based workflow orchestration



---



## Autonomous Workflow



```text

User Requirement

         |

         v

Requirement Agent

         |

         v

Planning Agent

         |

         v

Architect Agent

         |

         v

Developer Agent

         |

         v

Testing Agent

         |

         +------ PASS ------> Completed

         |

         +------ FAIL

                 |

                 v

          Debugger Agent

                 |

                 v

          Testing Agent

                 |

                 +------ PASS ------> Completed

                 |

                 +------ FAIL ------> Debugger

```



---



## AI Agents



| Agent             | Responsibility                                   |

| ----------------- | ------------------------------------------------ |

| Requirement Agent | Analyzes and structures user requirements        |

| Planning Agent    | Creates the software development plan            |

| Architect Agent   | Designs the system architecture                  |

| Developer Agent   | Generates application code                       |

| Testing Agent     | Generates tests and evaluates the implementation |

| Debugger Agent    | Identifies bugs and applies fixes                |



---



## Self-Correction Loop



One of the main capabilities of DevForge AI is its automatic debugging and re-testing loop.



```text

Testing

     |

     v

FAIL

     |

     v

Debugger

     |

     v

Fix Issues

     |

     v

Testing Again

     |

     v

PASS

```



This allows DevForge AI to automatically move through:



**Development -> Testing -> Debugging -> Re-testing -> Completion**



---



## Technology Stack



* Python

* Google Gemini API

* LangGraph

* LangChain

* Pydantic

* Git

* GitHub



The generated applications can also use technologies such as Node.js, JavaScript, backend APIs, and databases depending on the project requirements.



---



## Project Structure



```text

devforge-ai/

|

+-- agent.py

+-- requirements.txt

+-- test_config.py

+-- test_debugger.py

+-- test_gemini.py

|

+-- agents/

|   +-- architect/

|   |   +-- agent.py

|   |   +-- test_agent.py

|   |

|   +-- debugger/

|   |   +-- agent.py

|   |

|   +-- developer/

|   |   +-- agent.py

|   |   +-- test_agent.py

|   |

|   +-- planning/

|   |   +-- agent.py

|   |   +-- test_agent.py

|   |

|   +-- requirement/

|   |   +-- agent.py

|   |   +-- test_agent.py

|   |

|   +-- testing/

|       +-- agent.py

|       +-- test_agent.py

```



