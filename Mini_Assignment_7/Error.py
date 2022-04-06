class Error(Exception):
	pass
class FormulaError(Error):
	pass
ip="3 + 1"
try:
	vals=ip.split()
	if len(vals)==3:
		if vals[1] not in ['+','-']:
			raise FormulaError
		else:
			try:
				val1=float(vals[0])
				val2=float(vals[2])
				if vals[1]=='+':
					print(val1+val2)
				elif vals[1]=='-':
					print(val1-val2)
			except:
				raise FormulaError
	else:
		raise FormulaError
except FormulaError:
	print("FormulaError Occured")