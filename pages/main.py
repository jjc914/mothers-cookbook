import os



# print(text)

files = sorted(list(os.listdir()))

for file in files:
    if file.split('.')[-1] == 'html':
        val = file.split('-')[0]
        text = f'''<a href="pages/{file}">
        <div class="grid-item">
        <div class="background">
        <img src="res/{val}.png">
        </div>
        <div class="foreground">Easy Cold Noodles</div>
        </div>
        </a>'''
        print(text)
