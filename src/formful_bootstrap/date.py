from .meta import Input
from formful import widgets


class DateInput(Input, widgets.DateInput):
    pass


class DateTimeInput(Input, widgets.DateTimeInput):
    pass


class DateTimeLocalInput(Input, widgets.DateTimeLocalInput):
    pass


class TimeInput(Input, widgets.TimeInput):
    pass


class MonthInput(Input, widgets.MonthInput):
    pass


class WeekInput(Input, widgets.WeekInput):
    pass
