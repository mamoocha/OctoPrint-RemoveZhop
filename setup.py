from setuptools import setup

plugin_identifier = "remove_z_hop"
plugin_package = "remove_z_hop"
plugin_name = "Remove Z-Hop"
plugin_version = "1.0.0"
plugin_description = "Removes small Z-hop movements from G-code live during printing."
plugin_author = "Mamoocha"
plugin_author_email = "mamoocha@duck.com"
plugin_url = "https://github.com/mamoocha/OctoPrint-RemoveZHop"
plugin_license = "AGPLv3"
plugin_requires = []

setup(
    name=f"OctoPrint-{plugin_identifier}",
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    author_email=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    packages=[plugin_package],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "octoprint.plugin": [f"{plugin_identifier} = {plugin_package}.remove_z_hop:RemoveZHopPlugin"]
    },
)
