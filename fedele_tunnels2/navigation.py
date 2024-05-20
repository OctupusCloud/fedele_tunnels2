from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link="plugins:fedele_tunnels2:tunnel_list",
        link_text="Tunnels",
        permissions=["fedele_tunnels2.view_tunnel"],
        buttons=(PluginMenuButton(
            link='plugins:fedele_tunnels2:tunnel_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN,
            permissions=["fedele_tunnels2.add_tunnel"]
        ),)
    ),
    PluginMenuItem(
        link="plugins:fedele_tunnels2:tunneltype_list",
        link_text="Tunnel Types",
        permissions=["fedele_tunnels2.view_tunneltype"],
        buttons=(PluginMenuButton(
            link='plugins:fedele_tunnels2:tunneltype_add',
            title='Add',
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN,
            permissions=["fedele_tunnels2.add_tunneltype"]
        ),)
    ),
)
