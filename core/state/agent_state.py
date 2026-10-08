from typing import TypedDict, List, Dict, Any


class DevForgeState(TypedDict, total=False):
    """
    Shared state used by all DevForge AI agents.
    """

    # User's original software requirement
    user_requirement: str

    # Requirement analysis
    requirements: List[str]

    # Project planning
    project_plan: Dict[str, Any]

    # System architecture
    architecture: Dict[str, Any]

    # Generated source code
    generated_files: Dict[str, str]

    # Test results
    test_results: List[Dict[str, Any]]
    # Complete testing report
    testing_report: Dict[str, Any]

    # Debugging information
    bugs: List[Dict[str, Any]]
    # Complete debugging report
    debug_report: Dict[str, Any]

    # Security analysis
    security_report: Dict[str, Any]

    # GitHub information
    github_repo: str
    github_url: str

    # Deployment information
    deployment_status: str
    deployment_url: str

    # Human approval
    human_approval: bool

    # Current workflow status
    current_agent: str
    status: str

    # Activity/audit log
    activity_log: List[str]

    # Errors
    errors: List[str]