import octoprint.plugin
import re

class RemoveZHopPlugin(octoprint.plugin.OctoPrintPlugin):
def get_api_commands(self):
    return dict(
        set_threshold=["threshold"]
    )

def on_api_command(self, command, data):
    if command == "set_threshold":
        try:
            threshold = float(data.get("threshold", 0.4))
            self._settings.set_float(["z_threshold"], threshold)
            self._settings.save()
        except ValueError:
            self._logger.warning("Invalid threshold provided.")
def get_settings_defaults(self):
    return {
        "enabled": True,
        "z_threshold": 0.4
    }
    def gcode_queuing_hook(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        # Only target G0 or G1 moves
        if not self._settings.get_boolean(["enabled"]):
            # check if plugin is on
    return cmd
        if gcode in ("G0", "G1"):
            # Use regex to extract Z value if it exists
            match = re.search(r"Z([\d\.]+)", cmd)
            if match:
                try:
                    z_val = float(match.group(1))
                    if 0 < z_val <= 0.4:
                        self._logger.info(f"[RemoveZHop] Suppressed Z-hop move: {cmd}")
                        return None  # Suppress the command
                except ValueError:
                    pass  # Not a number, ignore

        return cmd  # Allow all other commands

__plugin_name__ = "Remove Z-Hop"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Removes small Z-hop movements from G-code live during printing."
__plugin_implementation__ = RemoveZHopPlugin()

__plugin_hooks__ = {
    "octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.gcode_queuing_hook
}  # Register hook
