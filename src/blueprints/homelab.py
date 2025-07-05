from diagrams import Diagram, Cluster
from diagrams.k8s.compute import Pod
from diagrams.k8s.ecosystem import Helm
from diagrams.onprem.gitops import Flux
from diagrams.onprem.network import Traefik
from diagrams.programming.language import Bash


def create_homelab_diagram(
    filename: str = "output/homelab_overview",
    title: str = "Homelab Overview",
    direction: str = "TB",
    show: bool = False,
) -> None:
    with Diagram(title, filename=filename, direction=direction, show=show):
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

        flux >> helm
        helm >> homepage
        helm >> linkding
        helm >> mealie
        helm >> eso
