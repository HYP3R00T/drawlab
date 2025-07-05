from diagrams import Cluster
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Service
from diagrams.programming.language import Bash

# Output filename for this diagram
OUTPUT_FILENAME = "kubernetes_deployment"


def create_diagram() -> None:
    """Define a Kubernetes deployment architecture."""
    user = Bash("Developer")

    with Cluster("Ingress"):
        ingress = Service("Ingress Controller")

    with Cluster("Frontend"):
        frontend_svc = Service("Frontend Service")
        frontend_pods = [Pod("Frontend Pod 1"), Pod("Frontend Pod 2")]

    with Cluster("Backend"):
        backend_svc = Service("Backend Service")
        backend_pods = [
            Pod("Backend Pod 1"),
            Pod("Backend Pod 2"),
            Pod("Backend Pod 3"),
        ]

    with Cluster("Database"):
        db_svc = Service("Database Service")
        db_pod = Pod("Database Pod")

    # Define connections
    user >> ingress >> frontend_svc >> frontend_pods
    frontend_pods >> backend_svc >> backend_pods
    backend_pods >> db_svc >> db_pod
