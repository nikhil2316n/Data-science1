#18/09/25
#set
#sets are not odered
# cities_={"tokya","Belin","Paris","London"}
# cities_.add("Nikil")
# UnicodeEncodeErrorintersection
# difference
# subset
# disjointset


surv_1={"EMP_5","EMP_1","EMP_3","EMP_2","EMP_0","EMP_4"}

surv_2={"EMP_8","EMP_7","EMP_3","EMP_4","EMP_5","EMP_6"}

print(surv_1.union(surv_2))#AUB
print(surv_1.intersection(surv_2))#A^B
print(surv_1.difference(surv_2))#A-B
print(surv_1.symmetric_difference(surv_2))#(A-B)U(B-A)
print(surv_1.isdisjoint(surv_2))#Return true or false
print(surv_1.issubset(surv_2))#Return True or False

