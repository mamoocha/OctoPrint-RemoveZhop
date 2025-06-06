$(function() {
    function RemoveZHopViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];

        self.enabled = ko.observable(self.settings.settings.plugins.removezhop.enabled());
        self.z_threshold = ko.observable(self.settings.settings.plugins.removezhop.z_threshold());

        self.enabled.subscribe(function(newVal) {
            self.settings.settings.plugins.removezhop.enabled(newVal);
            self.settings.saveData();
        });

        self.z_threshold.subscribe(function(newVal) {
            var val = parseFloat(newVal);
            if (!isNaN(val)) {
                self.settings.settings.plugins.removezhop.z_threshold(val);
                self.settings.saveData();
            }
        });
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: RemoveZHopViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#sidebar_plugin_removezhop"]
    });
});
