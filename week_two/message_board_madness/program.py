def author_rankings(threads):
    rankDict = {}
    
    for thread in threads:
        for post in thread["posts"]:
            if not post["author"] in rankDict:
                rankDict[post["author"]] = 0
            rankDict[post["author"]] += post["upvotes"]
    
    rankList = []
    for author in rankDict:
        if rankDict[author] == 0:
            comment = "Insignificantly Evil"
        elif rankDict[author] < 20:
            comment = "Cautiously Evil"
        elif rankDict[author] < 100:
            comment = "Justifiably Evil"
        elif rankDict[author] < 500:
            comment = "Wickedly Evil"
        else:
            comment = "Diabolically Evil"
        rankList.append((author, rankDict[author], comment))
    
    rankList.sort(key=lambda x: (1-x[1], x[0]))
    
    return rankList
    

if __name__ == '__main__':
    # Example calls to your function.
    print(author_rankings([
        {
            'title': 'Invade Manhatten, anyone?',
            'tags': ['world-domination', 'hangout'],
            'posts': [
                {
                    'author': 'Mr. Sinister',
                    'content': "I'm thinking 9 pm?",
                    'upvotes': 2,
                },
                {
                    'author': 'Mystique',
                    'content': "Sounds fun!",
                    'upvotes': 0,
                },
                {
                    'author': 'Magneto',
                    'content': "I'm in!",
                    'upvotes': 0,
                },
            ],
        }
    ]))