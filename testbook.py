import pandas as pd
import numpy as np
import random

# Генерируем исходные данные
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем столбцы для One-Hot Encoding
data['robot'] = np.where(data['whoAmI'] == 'robot', 1, 0)
data['human'] = np.where(data['whoAmI'] == 'human', 1, 0)

# Проверяем результат
print(data.head())
