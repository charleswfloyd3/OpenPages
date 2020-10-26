import webbrowser
while True:
     openbrowser = input("Type 1 to open web browser: ")
     if openbrowser == '1':
         urls = ['https://stackoverflow.com/', 'https://github.com/', 'https://smccd.instructure.com/courses/31456/assignments', 'https://www.chegg.com/reader/9781118890875/0/']

         for i in urls:
             webbrowser.open_new(i)
     else:
         print('Are you an idiot? ENTER 1')
