driving = input('請問您是否開過車(有/沒有)?')
if driving != '有' and driving != '沒有':
	print('請輸入 有/沒有')
	raise SystemExit
age = input('請輸入您的年齡:')
age = int(age)
if driving == '有':
	if age >= 18:
		print('您通過此測試!')
	else:
		print('奇怪 為何您會開過車?')
elif driving == '沒有':
	if age >=18:
		print('您已到可以考駕照的年齡了!')
	else:
		print('等到18歲您就可以去考駕照了!')
		