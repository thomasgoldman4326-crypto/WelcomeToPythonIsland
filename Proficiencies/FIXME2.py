name = "Bob"
instrument = "guitar"
skill_level = 75
has_ticket = False

print(f"Verifying if {name} can join the concert...")

if instrument == "guitar":
    print("You are a guitarist!")
    if skill_level >= 80:
        print("Your skills are amazing, welcome to the orchestra!")
        bonus = 10
        skill_level += bonus
        print(f"Your final skill level is {skill_level}.")
    else:
        print("You can join as a trainee.")
        fee = 5
        skill_level = skill_level - fee
        print(f"After paying the trainee fee, your skill is {skill_level}.")
        penalty = 2
        skill_level = skill_level - penalty
        print("Additional penalty applied.")   
else:
    if has_ticket:
        print("You can enter the concert as a guest.")
        seat = "Balcony"
        print(f"Your seat is in the {seat}.")
    else:
        print("You cannot join, and you don't even have a ticket.")
        print("Come back with at least a ticket!")              