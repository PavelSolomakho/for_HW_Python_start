data = {'name1': 100, 'name2': 200, 'name3': 300}
bonus = ['10.25%', '5%', '7.5%']
result = {k: v * (1 + float(bonus[i].strip('%')) / 100)
          for i, (k, v) in enumerate(data.items())}

names = ['Павел', 'Мария', 'Максим']
wages = [15000, 25000, 20000]
bonuses = ['10.25%', '6%', '7.5%']
result = {k: v * (1 + float(bonuses[i].strip('%')) / 100)
          for i, (k, v) in enumerate(zip(names, wages))}
print(result)
