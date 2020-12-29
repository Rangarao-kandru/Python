def getRatios(vect1, vect2):

  def getRatios(vect1,vect2):

    ratio=[]

    for i in range(0,len(vect1)):

        try:

            ratio.append(vect1[i]/(vect2[i]))

        except :

            ratio.append("invalid")

    return ratio

ratio1=[4,4,6]

ratio2=[2,2,2]

res=getRatios(ratio1,ratio2)

print(res)
