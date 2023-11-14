n = int(input("amount of invs: "))
invitations =  set(input() for _ in range(n))

while True:
    invites = input()
    if invites == "END":
        break
    invitations.discard(invites)

print(len(invitations))
for invitation in invitations:
    print(invitation)
