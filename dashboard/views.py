from django.views.generic import TemplateView

from dashboard.charts import LineChart
from testboard.models import Machine, Relay, Touch

class Dashboard(TemplateView):

    machines = Machine.objects.all()
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        mno = self.request.GET.get('machine', None)
        if not mno:
            mno = self.machines[0].no
        machine = Machine.objects.get(no=mno)
        volts = Relay.objects.filter(machine=mno, type=0).order_by('-id').values()[:10][::-1]
        times = Touch.objects.filter(machine=mno, type=3).order_by('-id').values()[:10][::-1]
        resis = Touch.objects.filter(machine=mno, type=2).order_by('-id').values()[:10][::-1]
        volt, time, resi = volts[-1], times[-1], resis[-1]
        open_time = max(time['open']) - min(time['open'])
        close_time = max(time['close']) - min(time['close'])

        chart_volts = LineChart(
            '吸合/释放电压', ('CV', 'OV'), volts,
            lambda x: x,
            width='100%', height=400
        ).chart()
        chart_times = LineChart(
            '吸合/释放时间', ('CT', 'OT'), times,
            lambda arr: max(arr) - min(arr),
            width='100%', height=400
        ).chart()
        chart_resis = LineChart(
            '吸合/释放电阻', ('NCR', 'NOR'), resis,
            lambda arr: sum(arr) / len(arr),
            width='100%', height=400
        ).chart()

        return {
            'host': "https://pyecharts.github.io/assets/js",
            'machines': self.machines,
            'machine': machine,
            'volt': volt, 'time': time, 'resi': resi,
            'open_time': open_time,
            'close_time': close_time,
            'chart_volts': chart_volts.render_embed(),
            'chart_times': chart_times.render_embed(),
            'chart_resis': chart_resis.render_embed(),
            'chart_js': chart_volts.get_js_dependencies(),
        }

    def post(self):
        return
