#Schritt-für-Schritt
#Erstelle eine Liste tasks = [].
#Zeige dem Nutzer ein Menü (z. B. „1 = Hinzufügen“, „2 = Anzeigen“,
#  "3. Aufgabe löschen", "4. Beenden", du kannst so viele einbauen wie du willst).
#Reagiere auf Eingaben mit if-Bedingungen.
#Speichere Aufgaben in einer Datei („tasks.txt“), 
# damit sie beim Neustart nicht verloren gehen.

tasklist = []

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
      Fertig = True
   else:
     print("Nochmal eintippen!")
  
    # noch zu machen: Text datei speichern und ändern können, case sensitivity machen
    #und mit zahlen auch auswählen können

