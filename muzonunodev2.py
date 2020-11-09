cocuklar = [
{
"studentid": "101",
"name": "ahmet",
"midterm": 70,
"final": 85,
},
{
"studentid": "102",
"name": "ezgi",
"midterm": 85,
"final": 100,
},
{
"studentid": "103",
"name": "fatih",
"midterm": 65,
"final": 45,
},
{
"studentid": "104",
"name": "murat",
"midterm": 45,
"final": 55,
},
{
"studentid": "105",
"name": "hande",
"midterm": 50,
"final": 60,
},
{
"studentid": "106",
"name": "rok",
"midterm": 35,
"final": 75,
},
{
"studentid": "107",
"name": "deniz gezmiş",
"midterm": 90,
"final": 70,
}]
ortalama = cocuklar[0]["midterm"]*4/10 + cocuklar[0]["final"]*6/10
ortalama1 = cocuklar[1]["midterm"]*4/10 + cocuklar[1]["final"]*6/10
ortalama2 = cocuklar[2]["midterm"]*4/10 + cocuklar[2]["final"]*6/10
print(cocuklar[0]["name"], "scored ",cocuklar[0]["midterm"], "from the midterm and ", cocuklar[0]["final"], "from the final.His end of term grade is calculated as ", int(ortalama))
print(cocuklar[1]["name"], "scored ",cocuklar[1]["midterm"], "from the midterm and ", cocuklar[1]["final"], "from the final.His end of term grade is calculated as ", int(ortalama1))
print(cocuklar[2]["name"], "scored ",cocuklar[2]["midterm"], "from the midterm and ", cocuklar[2]["final"], "from the final.His end of term grade is calculated as ", int(ortalama2))
# for x in cocuklar:
#     ortalama = x["midterm"]*4/10 + x["final"]*6/10
#     if ortalama < 70:
#         continue
#     print(x["name"], "scored ",x["midterm"], "from the midterm and ", x["final"], "from the final.His end of term grade is calculated as ", int(ortalama))
