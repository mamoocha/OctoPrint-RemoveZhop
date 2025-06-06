import octoprint.plugin
import re

class RemoveZHopPlugin(octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.TemplatePlugin,
                      octoprint.plugin.AssetPlugin,
                      octoprint.plugin.StartupPlugin):

    def get_settings_defaults(self):
        return {
            "enabled": False,
            "z_threshold": 0.0
        }

    def gcode_queuing_hook(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        if not self._settings.get_boolean(["enabled"]):
            return cmd

        if gcode in ("G0", "G1"):
            match = re.search(r"Z([\d\.]+)", cmd)
            if match:
                try:
                    z_val = float(match.group(1))
                    threshold = self._settings.get_float(["z_threshold"])
                    if 0 < z_val <= threshold:
                        self._logger.info(f"[RemoveZHop] Suppressed Z-hop move (commented): {cmd}")

                        # Instead of removing the command, we comment it out
                        # so the firmware does not receive it but the log records it
                        return f"; Suppressed Z-hop: {cmd}\n"
                except ValueError:
                    self._logger.warning(f"[RemoveZHop] Couldn't parse Z value from command: {cmd}")

        return cmd

    def get_template_configs(self):
        return [dict(type="sidebar", name="Remove Z-Hop", template="removezhop_sidebar.jinja2", custom_bindings=True)]

    def get_assets(self):
        return {
            "js": ["static/js/removezhop.js"],
            "css": ["static/css/removezhop.css"]
        }

    def on_after_startup(self):
        self._logger.info("Remove Z-Hop plugin loaded. Enabled: %s, Threshold: %.2f" % (
            self._settings.get_boolean(["enabled"]),
            self._settings.get_float(["z_threshold"])
        ))

__plugin_implementation__ = RemoveZHopPlugin()

__plugin_hooks__ = {
    "octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.gcode_queuing_hook
}
