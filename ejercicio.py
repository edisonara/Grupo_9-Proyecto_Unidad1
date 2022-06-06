import calendar
import locale
locale.setlocale(locale.LC_ALL, "es_EC.utf8") # nombre de los dias en ecuador
print(list(calendar.day_name))
print(list(calendar.month_name[1]))
print(calendar.month(2022, 4, 1, 1))#imprimir calendario [año, mmes, columnas, ]

import holidays# moodulo de ver los dias festivos 