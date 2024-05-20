from extras.plugins import PluginConfig
from .version import __version__, __min_version__, __max_version__


class TunnelsConfig(PluginConfig):
    """This class defines attributes for the NetBox Tunnels Plugin."""
    name = "fedele_tunnels2"
    verbose_name = "Network Tunnels"
    version = __version__
    description = "Subsystem for tracking IP Tunnels"
    base_url = "tunnels"
    author = "Octupus"
    author_email = "maxi@octupus.com"
    min_version = __min_version__
    max_version = __max_version__


config = TunnelsConfig 
