from collections import Iterable

from pyecharts import Line


class LineChart:

    def __init__(self, title, params, records, calc, **kwargs):
        self._chart = Line(title, **kwargs)
        self._calc, self._params, self._records = calc, params, records

    def _open(self):
        return [
            float('%.2f' % self._calc(item.get('open')))
            for item in self._records
        ]

    def _close(self):
        return [
            float('%.2f' % self._calc(item.get('close')))
            for item in self._records
        ]

    def _time(self):
        return [
            item.get('time_joined').strftime('%m.%d %H:%M:%S')
            for item in self._records
        ]

    def chart(self):
        close, open = self._params
        self._chart.add(
            close, self._time(), self._close(),
            mark_point=['max', 'min'], mark_line=['average'],
            line_opacity=0.5, tooltip_tragger='axis',
            is_toolbox_show=False
        )
        self._chart.add(
            open, self._time(), self._open(),
            mark_point=['max', 'min'], mark_line=['average'],
            line_opacity=0.5, tooltip_tragger='axis',
            is_toolbox_show=False
        )
        return self._chart