

from firebase import firebase

firebase = firebase.FirebaseApplication('https://project1-e90e6.firebaseio.com/', None)

new_user = "SPOT1"

#result = firebase.get('/users', None)

#print result

#firebase.post('/users', new_user)
status = "Empty"
#firebase.post('/users/%s %s', % (new_user,status))

result = firebase.put('users/', new_user, status)