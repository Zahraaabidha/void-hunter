content = open(r'C:\Users\Aabidha\Desktop\hand-movement\_src.html', encoding='utf-8').read()
open(r'C:\Users\Aabidha\Desktop\hand-movement\index.html', 'w', encoding='utf-8').write(content)
print('Done, bytes:', len(content))
