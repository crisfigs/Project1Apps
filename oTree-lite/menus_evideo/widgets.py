from otree.api import widgets

class OrderedChoice(widgets.TextInput):
    template_name = 'school_choice/widgets/ordered_choice.html'

    def __init__(self, choices=[]):
        super().__init__()
        self.choices = choices

    def get_context(self, name, value, attrs):
        ctx = super().get_context(name, value, attrs)
        ctx['choices'] = self.choices
        ctx['name'] = name
        return ctx