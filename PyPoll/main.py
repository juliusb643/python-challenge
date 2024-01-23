import csv
import os

election_data_csv = os.path.join("PyPoll\Resources", "election_data.csv")
# Total Votes Counter
total_number_votes = 0

# candidate Options and vote count
candidate = []
voting_percentages_per_candidate =[]
candidate_options = []
votes_per_candidate = {}

# winning candidate and winning count tracker
winning_candidate = ""
winner_count = 0

with open(election_data_csv) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    for row in reader:
        total_number_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            votes_per_candidate[candidate_name] = 1
        else: 
            votes_per_candidate[candidate_name] += 1


output = os.path.join("PyPoll\Resources", "election.txt")

with open(output, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_number_votes}\n"
        f"--------------------\n"
    )

    print(election_results, end="")

    txt_file.write(election_results)

    for candidate in votes_per_candidate:
        vote = votes_per_candidate.get(candidate)
        vote_percentage = float(vote)/ float(total_number_votes) * 100

        if (vote > winner_count):
            winner_count = vote
            winning_candidate = candidate

        vote_output = f"{candidate}: {vote_percentage:.3f}% ({vote})\n"
        print(vote_output, end ="")

        txt_file.write(vote_output)


    winner_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------\n")

    txt_file.write(winner_summary)


print(winner_summary)