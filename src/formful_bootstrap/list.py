from .meta import Input
from formful import widgets
from markupsafe import Markup


class ListWidget(widgets.ListWidget):

    def __init__(self, **kws):
        pass

    def __call__(self, field, **kwargs):
        subfields = "".join((subfield() for subfield in field))
        return Markup(f"<div class='col-sm-10'>{subfields}</div>")


class ListWidgetWithAlternative(ListWidget):

    def __call__(self, field, **kwargs):
        kwargs['class'] += ' form-control'
        current = super().__call__(field, **kwargs)
        if field.choices:
            return current + (
                Markup(
                    "<div class='col-sm-10 form-group'><input %s></div>" % html_params(
                    id=field.id + ".alt",
                    name=field.name + ".alt",
                    rel=field.name,
                    type="text",
                    **kwargs
                ))
            )
        return current
