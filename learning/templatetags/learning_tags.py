from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def say(text, speed='normal', voice='', size=''):
    """Nút loa phát một câu tiếng Anh. speed=slow/slower hiện icon đồng hồ cát (đọc chậm)."""
    slow = speed in ('slow', 'slower')
    return format_html(
        '<button type="button" class="say-btn {} {}" data-say="{}"{}{} title="{}" aria-label="{}">'
        '<i class="bi {}"></i></button>',
        size, 'slow' if slow else '', text,
        # Không ghi tốc độ "normal" để nút dùng tốc độ trong Cài đặt
        format_html(' data-speed="{}"', speed) if speed != 'normal' else '',
        format_html(' data-voice="{}"', voice) if voice else '',
        'Nghe chậm' if slow else 'Nghe', 'Nghe chậm' if slow else 'Nghe',
        'bi-hourglass-split' if slow else 'bi-volume-up',
    )


@register.filter
def initial(name):
    return (name or '?')[:1].upper()
