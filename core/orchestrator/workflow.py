from langgraph.graph import StateGraph, START, END

from core.state.agent_state import DevForgeState

from agents.requirement.agent import requirement_agent
from agents.planning.agent import planning_agent
from agents.architect.agent import architect_agent
from agents.developer.agent import developer_agent
from agents.testing.agent import testing_agent
from agents.debugger.agent import debugger_agent


def should_continue_after_requirement(state: DevForgeState):
    """
    Continue to Planning only if Requirement Agent
    completed successfully.
    """

    status = state.get("status", "")

    if status == "requirements_analyzed":
        return "planning"

    return "end"


def should_continue_after_planning(state: DevForgeState):
    """
    Continue to Architect only if Planning Agent
    completed successfully.
    """

    status = state.get("status", "")

    if status == "planning_completed":
        return "architect"

    return "end"


def should_continue_after_architect(state: DevForgeState):
    """
    Continue to Developer only if Architect Agent
    completed successfully.
    """

    status = state.get("status", "")

    if status == "architecture_completed":
        return "developer"

    return "end"


def should_continue_after_developer(state: DevForgeState):
    """
    Continue to Testing only if Developer Agent
    completed successfully.
    """

    status = state.get("status", "")

    if status == "code_generation_completed":
        return "testing"

    return "end"


def should_continue_after_testing(state: DevForgeState):
    """
    If testing passes, finish the workflow.

    If testing fails, send the project to Debugger Agent.
    """

    status = state.get("status", "")

    testing_report = state.get("testing_report", {})

    overall_status = testing_report.get(
        "overall_status",
        ""
    )

    # Testing completed successfully
    if status == "testing_completed":

        # If tests pass, workflow is complete
        if overall_status.upper() == "PASS":
            return "end"

        # If tests fail, send to Debugger
        if overall_status.upper() == "FAIL":
            return "debugger"

    return "end"


def should_continue_after_debugger(state: DevForgeState):
    """
    After debugging, send the fixed project back to Testing.
    """

    status = state.get("status", "")

    if status == "debugging_completed":
        return "testing"

    return "end"


def build_workflow():

    workflow = StateGraph(DevForgeState)

    # -------------------------
    # Add Agents
    # -------------------------

    workflow.add_node(
        "requirement",
        requirement_agent
    )

    workflow.add_node(
        "planning",
        planning_agent
    )

    workflow.add_node(
        "architect",
        architect_agent
    )

    workflow.add_node(
        "developer",
        developer_agent
    )

    workflow.add_node(
        "testing",
        testing_agent
    )

    workflow.add_node(
        "debugger",
        debugger_agent
    )

    # -------------------------
    # Start
    # -------------------------

    workflow.add_edge(
        START,
        "requirement"
    )

    # -------------------------
    # Requirement → Planning
    # -------------------------

    workflow.add_conditional_edges(
        "requirement",
        should_continue_after_requirement,
        {
            "planning": "planning",
            "end": END
        }
    )

    # -------------------------
    # Planning → Architect
    # -------------------------

    workflow.add_conditional_edges(
        "planning",
        should_continue_after_planning,
        {
            "architect": "architect",
            "end": END
        }
    )

    # -------------------------
    # Architect → Developer
    # -------------------------

    workflow.add_conditional_edges(
        "architect",
        should_continue_after_architect,
        {
            "developer": "developer",
            "end": END
        }
    )

    # -------------------------
    # Developer → Testing
    # -------------------------

    workflow.add_conditional_edges(
        "developer",
        should_continue_after_developer,
        {
            "testing": "testing",
            "end": END
        }
    )

    # -------------------------
    # Testing → Debugger / End
    # -------------------------

    workflow.add_conditional_edges(
        "testing",
        should_continue_after_testing,
        {
            "debugger": "debugger",
            "end": END
        }
    )

    # -------------------------
    # Debugger → Testing
    # -------------------------

    workflow.add_conditional_edges(
        "debugger",
        should_continue_after_debugger,
        {
            "testing": "testing",
            "end": END
        }
    )

    # -------------------------
    # Compile Workflow
    # -------------------------

    return workflow.compile()


devforge_workflow = build_workflow()