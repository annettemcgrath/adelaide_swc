import sys

arg_list = sys.argv

items= arg_list[1:len(arg_list)]

items.sort()
items[0]=items[0].title()
joined=', '.join(items[0:2])

joined +=' and ' + items[-1] + '.'

print joined
