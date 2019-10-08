#3.4 Guest List 
guest_list = ["Mike", "Rayan", "Rakshak"]
message = "Hi " + guest_list[0].title() + ", I'd like invite you to dinner"
print(message)
#3.5 Changing Guest List
guest_list[2] = "Jamie"
print(guest_list)
#3.6 Adding Guests
guest_list.insert(0, "Rasmus")
guest_list.append("Asif")
print(guest_list)
#3.7 Removing Guests
print("I can only invite two people to dinner")
removed_guest = guest_list.pop()
sorry_message = "Sorry " + removed_guest + ", I cannot invite you to dinner"
print(sorry_message)
removed_guest = guest_list.pop()
sorry_message = "Sorry " + removed_guest + ", I cannot invite you to dinner"
print(sorry_message)
removed_guest = guest_list.pop()
sorry_message = "Sorry " + removed_guest + ", I cannot invite you to dinner"
print(sorry_message)
still_invited = "Hi " + guest_list[0] + " and " + guest_list[1] + ", you are still invited to dinner"
print(still_invited)
del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)
