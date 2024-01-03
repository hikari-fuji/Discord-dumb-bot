def get_help_text(prefix):
    help_text = f"""Các lệnh của bot:
- `/help`: hiện hướng dẫn sử dụng bpt
- `/meme`: một meme ngẫu nhiên
- `/joke`: đùa một câu ngẫu nhiên
- `/anime`: tìm một anime theo tên
- `/manga`: tìm một manga theo tên
"""
    return help_text
def command_response(prefix):
    return get_help_text(prefix)
