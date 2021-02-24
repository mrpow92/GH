def namelist(names):
    if len(names) <= 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return names[0]['name']+" & "+ names[1]['name']
    else:
        finalstring =""
        for i, name in enumerate(names):
            if i!=0 and i<len(names)-1:
                finalstring+=", "+name['name']
            elif i == 0:
                finalstring+=name['name']
            if i==len(names)-1:
                finalstring+=" & "+name['name']
        return finalstring