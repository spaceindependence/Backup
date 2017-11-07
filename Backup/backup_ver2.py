import os
import time

source = ['/home/alex/Documents', '/home/alex/Шаблоны']

target_dir = '/home/alex/Backup'

# Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее имя служит именем zip-архива
now = time.strftime('%H%M%S')

# Создаем каталог, если его еще нет
if not os.path.exists(today):
    os.mkdir(today)
print('Каталог успешно создан', today)

# Имя zip-файла
target = today + os.sep + now + '.zip'
#Помещаем файлы в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

#Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
