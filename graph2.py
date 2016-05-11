import seaborn as sb



x = ['uniform', 'm=Ⅰ', 'm=4', 'm=9', 'm=12']
y = [1, 2, 3, 4, 5]

sb.barplot(x, y)
sb.despine(bottom=True)
