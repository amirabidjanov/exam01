text = int(input('ball kiriting:'))
if 90 <= text <= 100:
    print("A A'lo")
elif 80 <= text <= 89:
    print('B yaxshi') 
elif 70 <= text <= 79:
    print('C Qonoqarli')
elif 60 <= text <= 69:
    print('D Qonoqarsiz')
elif 0 <= text <= 59:
    print('F yomon ')
else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")