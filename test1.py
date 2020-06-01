 <form name="loginform" method="post" action="userinfo.php">


import requests
url = 'http://example.com/userinfo.php'
values = {'username': 'user',
          'password': 'pass'}

r = requests.post(url, data=values)
print r.content
