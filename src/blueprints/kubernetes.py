from diagrams import Diagram, Cluster
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Service
from diagrams.programming.language import Bash


def create_kubernetes_diagram(
    filename: str = "output/kubernetes_deployment",
    title: str = "Kubernetes Deployment",
    direction: str = "LR",
    show: bool = False,
) -> None:
    with Diagram(title, filename=filename, direction=direction, show=show):
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
        user >> ingress >> frontend_svc
        frontend_svc >> frontend_pods[0]
        frontend_svc >> frontend_pods[1]

        for frontend in frontend_pods:
            frontend >> backend_svc

        backend_svc >> backend_pods[0]
        backend_svc >> backend_pods[1]
        backend_svc >> backend_pods[2]

        for backend in backend_pods:
            backend >> db_svc

        db_svc >> db_pod
