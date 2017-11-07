import os
import time

source = ['/home/alex/Documents', '/home/alex/Шаблоны']

target_dir = '/home/alex/Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # Проверяем, введен ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
print('Каталог успешно создан', today)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
