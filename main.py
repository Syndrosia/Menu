index = [["chips", 1.10], ["fish", 3.10], ["burger", 7.10], ["rice", 4.10]]
run, mult, crList = True, 1, []

while run:
   main = input("Enter food: ").lower()

   if main == "end":
      print(crList)
      run = False
   elif main.find("-") != -1:  # quantity handler
      mult = int(main[main.find("-") + 1:])

   if main != "end":
      for i in range(len(index)):
         if not main.find(index[i][0]):
            crList.append(index[i][1] * mult)
            print(f"Successfully added {index[i][0]}! Total = £{round(sum(crList), 2)}")
