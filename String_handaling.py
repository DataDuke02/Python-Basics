driver_name = "Thirugnanasambantham S"

mobile = "9999999990"
masked = mobile[:2] + "******" + mobile[-2:]
print(driver_name.lower())
print(masked)


song = "rock star"
artist = "thiru s"
formatted = f"{song.title()} - {artist.title()}"
print(formatted)

location = "chennai central"
fixeded_location = location.replace("chennai central","Thambaram")
print(fixeded_location)

message = "Your uber booking ID is: U21354, please keep it safe" # ':,' are delimiter
booking_id=message.split(":")[1].split(",")[0].strip()
print(booking_id)

promo_message="use zomoto100 to get 100 off on your first order"
if "zomoto100" in promo_message:
    print("offer appiled")


feedback = "the driver was polite and the ride was smooth"
print("position is:", feedback.find("polite"))

name = "tHIRU s"
initials= "".join([word[0].upper() for word in name.split()]) #.join is used for to add ""
print(initials)

dirty_input = "   airport"
clean=dirty_input.strip()
print(clean)

word1="the trip was amazing and the car was clean"
word_count=len(word1.split()) # in empty split the space count as delimiter
print(word_count)
