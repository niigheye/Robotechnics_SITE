from django.contrib import admin
from static_data.models import StaticData  # noqa: F401


@admin.register(StaticData)
class StaticDataAdmin(admin.ModelAdmin):
    """!
    @brief Админ панель для статических данных
    @param list_display Паля модели, отображаемые на сайте: адрес, телефон, email, ссылка на вк, ссылка на телеграм
    """
    list_display = [
        'address',
        'phone',
        'email',
        'link_to_vk',
        'link_to_telegram'
    ]
