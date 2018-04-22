from django.contrib import admin
from django.shortcuts import reverse
from django.utils.html import format_html

from testboard.models import (
    Machine, Relay, Touch
)
from utils.driver import (
    test_relay, test_touch
)

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):

    list_filter = ('type', )
    list_display_links = ('id', 'no')
    list_display = ('id', 'no', 'type', 'log_relay', 'log_touch', 'test_record')

    actions = ('test_relay', 'test_touch')

    def log_relay(self, obj):
        return format_html(
            '<a href="{}?machine={}">日志</a>',
            reverse('admin:testboard_relay_changelist'), obj.no
        )
    log_relay.short_description = '继电器'

    def log_touch(self, obj):
        return format_html(
            '<a href="{}?machine={}">日志</a>',
            reverse('admin:testboard_touch_changelist'), obj.no
        )
    log_touch.short_description = '触点'

    def test_record(self, obj):
        return format_html(
            '<a href="{}">统计</a>',
            reverse('dashboard')
        )
    test_record.short_description = '测试记录'

    def test_relay(self, request, queryset):
        for machine in queryset:
            record = test_relay()
            Relay(
                close=record.get('CV'),
                open=record.get('OV'),
                type=0,
                machine=machine.no
            ).save()
        self.message_user(request, '已保存测试结果到日志记录')
    test_relay.short_description = '测试 继电器'

    def test_touch(self, request, queryset):
        for machine in queryset:
            record = test_touch()
            Touch(
                close=record.get('CT'),
                open=record.get('OT'),
                type=3,
                machine=machine.no
            ).save()
            Touch(
                close=record.get('NCR'),
                open=record.get('NOR'),
                type=2,
                machine=machine.no
            ).save()
        self.message_user(request, '已保存测试结果到日志记录')
    test_touch.short_description = '测试 触点'



@admin.register(Touch)
class TouchAdmin(admin.ModelAdmin):

    list_per_page = 20

    list_filter = ('type', 'machine')
    list_display = (
        'id', 'close_2f', 'open_2f', 'type', 'time_joined', 'machine'
    )

    def close_2f(self, obj):
        return ['%.2f' % close for close in obj.close]
    close_2f.short_description = '闭合'

    def open_2f(self, obj):
        return ['%.2f' % open for open in obj.open]
    open_2f.short_description = '释放'


@admin.register(Relay)
class RelayAdmin(admin.ModelAdmin):

    list_per_page = 20

    list_filter = ('type', 'machine')
    list_display = (
        'id', 'close_2f', 'open_2f', 'type', 'time_joined', 'machine'
    )

    def close_2f(self, obj):
        return '%.2f' % obj.close
    close_2f.short_description = '闭合'

    def open_2f(self, obj):
        return '%.2f' % obj.open
    open_2f.short_description = '释放'

admin.site.site_header = '信号继电器综合测试台'