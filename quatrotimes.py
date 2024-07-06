time1 = input("Digite o nome do primeiro time: \n")
time2 = input("Digite o nome do segundo time: \n")
time3 = input("Digite o nome do terceiro time: \n")
time4 = input("Digite o nome do quarto time: \n"
              
              )
print(f"Os times digitados foram: {time1}, {time2}, {time3}, {time4}.")
gol1 = int(input(f"Digite os gols marcados pelo {time1} \n"))
print(f"Os gols feitos pelo {time1} foram {gol1}")
gol2 = int(input(f"Digite os gols marcados pelo {time2} \n"))
print(f"Os gols feitos pelo {time2} foram {gol2}")
gol3 = int(input(f"Digite os gols marcados pelo {time3} \n"))
print(f"Os gols feitos pelo {time3} foram {gol3}")
gol4 = int(input(f"Digite os gols marcados pelo {time4} \n"))
print(f"Os gols feitos pelo {time4} foram {gol4}")


if gol1 > gol2:
    print(f"O time {time1} foi o vencedor e irá ir para a semi-final.")
elif gol1 == gol2:
    print("Os dois times empataram e foram para os penaltis.")
else:
    print(f"O time {time2} foi o vencedor e irá ir para a semi-final.")    
if gol3 > gol2:
    print(f"O time {time3} foi o vencedor e irá ir para a semi-final.")
elif gol3 == gol2:
    print("Os dois times empataram e foram para os penaltis.")
else: 
    print(f"O time {time4} foi o vencedor e irá ir para a semi-final.")
    for i in range (0, 5):
        penalti1 = int(input(f"Digite 1 ce foi marcado o gol de penalti para o {time1}, e 0 para não \n"))
        penalti2 = int(input(f"Digite 1 ce foi marcado o gol de penalti para o {time2}, e 0 para não \n"))
    if penalti1 > penalti2:
        print(f"O {time1} venceu nos penaltis com {penalti1} gols! É assim passando para a final!! ")
    else:
        print(f"O {time2} venceu nos penaltis com {penalti2} gols! É assim passando para a final!! ")
    for i in range (0, 5):  
        penalti3 = int(input(f"Digite 1 ce foi marcado o gol de penalti para o {time3}, e 0 para não \n"))
        penalti4 = int(input(f"Digite 1 ce foi marcado o gol de penalti para o {time4}, e 0 para não \n"))
    if penalti3 > penalti4:
        print(f"O {time3} venceu nos penaltis com {penalti3} gols! É assim passando para a final!! ")
    else:
        print(f"O {time4} venceu nos penaltis com {penalti4} gols! É assim passando para a final!! ")
        
               



