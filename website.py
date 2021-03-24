from pywebcopy import save_webpage as sw

url = 'https://farmx.co.in/'
aapd = 'C:/Users/Arun Ahirwar/Desktop/Full website Clone in python'    

kwargs = {'bypass_robots': True, 'project_name': 'Arunwebsite'}

sw(url, aapd, **kwargs)
