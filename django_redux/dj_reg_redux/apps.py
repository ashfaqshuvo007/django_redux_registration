from django.apps import AppConfig


class DjRegReduxConfig(AppConfig):
    name = 'dj_reg_redux'

    def ready(self):
        import dj_reg_redux.mySignal
