def health_calculator(age, milk, cigrate_smoked):
    answer = (100 - age) + (milk * 3.5) - (cigrate_smoked * 3)
    print(answer)

health_calculator(25,1,10)

angad = [25,10,3]
health_calculator(angad[0],angad[1],angad[2])
health_calculator(*angad)
