import os
import shutil
path = '../backend/static/reactjs'
from time import sleep

if os.path.isdir(path) :
    if os.path.isdir(path+'/js') :
        shutil.rmtree(path+'/js')
        print('js folder deleted')
    if os.path.isdir(path+'/css') :
        shutil.rmtree(path+'/css')
        print('css folder deleted')
    sleep(2)
    os.rmdir(path)
shutil.copytree('./build/static/',path)

i = 0
for file in os.listdir(path+'/js') :
    if file.endswith('.js') :
        i += 1
        os.rename(path+'/js/'+file,path+'/js/'+'react_js'+str(i)+'.js')
i = 0
for file in os.listdir(path+'/css') :
    if file.endswith('.css') :
        i += 1
        os.rename(path+'/css/'+file,path+'/css/'+'react_css'+str(i)+'.css')
