
candidates = ["A", "B", "C", "D", "E"]


candidate_votes = {candidate: 0 for candidate in candidates}

print("Welcome to the Basic Voting System!")


for candidate in candidates:
    print(candidate)


vote = input("Enter the name of the candidate you want to vote for (or 'exit' to end voting): ").strip()

while vote.lower() != "Exit":
    if vote in candidates:
        candidate_votes[vote] += 1
        print(f"Thank you for voting for {vote}!\n")
    else:
        print("Invalid candidate name. try again.")

   
    vote = input("Enter the name of the candidate you want to vote for (or 'exit' to end voting): ").strip()

print("Voting has ended. Here are the results:")

for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes")


winner = max(candidate_votes, key=candidate_votes.get)
print("The winner is {winner} with {candidate_votes[winner]} votes!")
