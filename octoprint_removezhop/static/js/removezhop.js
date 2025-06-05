$(function() {
    function RemoveZHopViewModel(parameters) {
        var self = this;

        self.settingsViewModel = parameters[0];
        self.enabled = self.settingsViewModel.settings.plugins.removezhop.enabled;
        self.z_threshold = self.settingsViewModel.settings.plugins.removezhop.z_threshold;
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: RemoveZHopViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#sidebar_plugin_removezhop"]
    });
});