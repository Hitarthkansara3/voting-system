# online Voting System

from itertools import count


candidates = ["Narendra", "Rahul", "Arvind", "Manmohan"]
votes = {candidate : 0 for candidate in candidates}

num_voters = int(input("Enter number of voters: "))

for i in range(num_voters):
    print(f"\n voter {i+1}")
    print("candidates :", ", ".join(candidates))

    vote = input("Cast your vote by typing candidate's name: ")

    if vote in votes:
        votes[vote] += 1
        print(f"Vote cast successfully for {vote} !")

    else:
        print("Invalid candidate. vote is not counted.")

print("\n ---Voting Results---")
for candidate, count in votes.items():
    print(f"{candidate} : {count} votes")

max_votes = max(votes.values())

winners = [name for name, count in votes.items() if count == max_votes]
if(len(winners) ==1 ):
    print(f"Winners: {winners[0]} with {max_votes} votes !")

else:
    print(f"It's a tie between : {','.join(winners)} with {max_votes} votes each !")