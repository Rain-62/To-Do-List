
tasklist = [] 
with open ("Text.txt") as f:
  tasklist = [f.read()]

Fertig = False

while Fertig == False:
   print("    ")
   print("1. Add")
   print("2. Show")
   print("3. Delete")
   print("4. Close")
   status = (input("Was möchten Sie machen? "))

   if status == "Add" or status == "1":
     tasklist.append(input("Was möchten Sie hinzufügen? "))
   elif status == "Show" or status == "2": 
     print(tasklist)
   elif status == "Delete" or status == "3": 
     tasklist.remove(input("Was soll gelöscht werden?"))
   elif status == "Close" or status == "4": 
      print("Programm wird beendet!")
      
      liste = ", ".join(tasklist)
      with open ("Text.txt", "w") as f:
        f.write(liste)
      Fertig = True
   else:
     
     print("Nochmal eintippen!")