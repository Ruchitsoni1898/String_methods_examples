f_name = "Ruchit Soni"
s_name = f_name.split()
print(f_name)
print(s_name)

f_name = 'Ruchit Soni.'
print(f_name)
name_clean = f_name.strip('.')
print(name_clean)

print(f_name.upper())
print(f_name.lower())

url = "https://www.google.com/"
is_home = url.endswith('.com')
is_absolute = url.startswith('https')
print(is_home)
print(is_absolute)

info = "This %20 is %20 url %20 encoded"
info2 = info.replace("%20","")
print(info)
print(info2)


