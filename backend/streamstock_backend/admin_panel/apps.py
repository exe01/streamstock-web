from django.apps import AppConfig


class AdminPanelConfig(AppConfig):
    name = 'streamstock_backend.admin_panel'

    def ready(self):
        import streamstock_backend.admin_panel.signals
