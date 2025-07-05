from diagrams import Cluster
from diagrams.k8s.compute import Pod
from diagrams.k8s.ecosystem import Helm
from diagrams.onprem.gitops import Flux
from diagrams.onprem.network import Traefik
from diagrams.programming.language import Bash

# Output filename for this diagram
OUTPUT_FILENAME = "homelab_overview"


def create_diagram() -> None:
    """Define the homelab diagram structure."""
    user = Bash("Client")

    with Cluster("Ingress"):
        cloudflared = Pod("Cloudflared")
        traefik = Traefik("Traefik")

    with Cluster("Platform"):
        flux = Flux("FluxCD")
        helm = Helm("Helm")

    with Cluster("Secrets"):
        eso = Pod("ESO")

    with Cluster("Apps"):
        homepage = Pod("Homepage")
        linkding = Pod("Linkding")
        mealie = Pod("Mealie")

    # Define connections
    user >> cloudflared >> traefik >> homepage
    traefik >> linkding
    traefik >> mealie

    flux >> helm >> [homepage, linkding, mealie, eso]
