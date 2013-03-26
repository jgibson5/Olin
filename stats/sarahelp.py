import Pmf

def levene(l1, l2):
	p1 = Pmf.MakePmfFromList(l1)
	p2 = Pmf.MakePmfFromList(l2)
	v1 = p1.Var()
	v2 = p2.Var()
	return v1/v2


x1 = [23.5, 12, 21, 22, 19.125, 21.5, 22.125, 20.375, 18.25, 21.625, 23.25, 21, 22.125, 23, 12]
x2 = [17.375, 20.375, 20, 20, 18.375, 18.625, 18.625, 15.25, 16.5, 18, 16.25, 18, 12.75, 15.5, 18]

print levene(x1, x2)
