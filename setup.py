from setuptools import setup

plugin_identifier = "removezhop"
plugin_package = "octoprint_removezhop"
plugin_name = "OctoPrint-RemoveZHop"
plugin_version = "1.0.1"
plugin_description = "Removes small Z-hop moves from G-code during printing"
plugin_author = "mamoocha"
plugin_author_email = "mamoocha@duck.com"
plugin_url = "https://github.com/mamoocha/OctoPrint-RemoveZhop"
plugin_license = "AGPLv3"
plugin_requires = []

setup(
    name=plugin_name,
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
        "octoprint.plugin": ["%s = %s" % (plugin_identifier, plugin_package)]
    },
)
