from django import template
from ..models import MenuItem

register = template.Library()


# тэг отправляет рекурсивный запрос для выборки необходимых элементов меню из БД
@register.inclusion_tag('UpTraderApp/tag/draw_menu.html')
def draw_menu(slug):
    menu_items = MenuItem.objects.raw(f"""
    WITH RECURSIVE category(id, name, slug, parent_id, depth) AS (
          SELECT id, name, slug, parent_id, depth
          FROM UpTraderApp_menuitem
          WHERE slug = '{slug}'
        UNION ALL
          SELECT mi.id, mi.name, mi.slug, mi.parent_id, mi.depth
          FROM UpTraderApp_menuitem AS mi, category AS c
          WHERE mi.id = c.parent_id
        ) 
    SELECT mi.id, mi.name, mi.slug, mi.parent_id, mi.depth FROM category AS c, UpTraderApp_menuitem AS mi
	WHERE c.parent_id = mi.parent_id
    UNION
    SELECT id, name, slug, parent_id, depth FROM UpTraderApp_menuitem
    WHERE parent_id = (SELECT id FROM UpTraderApp_menuitem WHERE slug = '{slug}') OR parent_id ISNULL
    ORDER BY depth
    """)

    # из полученных элементов составляется очередь по грубине
    menu_items_dict = {}
    for item in menu_items:
        depth = item.depth
        if depth in menu_items_dict:
            menu_items_dict[depth].append(item)
        else:
            menu_items_dict[depth] = [item]

    return {'menu': menu_items_dict}
