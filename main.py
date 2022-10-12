import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from csv import reader
from csv import DictReader
import time

# get tmdb id function
def get_tmdb_id():
    # series names
    series = ["Batwoman", "Chicago PD", "FBI", "FBI most wanted", "LOKI", "Legacies", "Lucifer", "Hanna", "Seal Team",
              "Succession", "Yellowstone", "911", "The Great", "S.W.A.T", "Blade Runner Black Lotus", "Money Heist",
              "The Walking Dead;World Beyond", "Squid Game", "Queen Of The South", "NCIS", "Bob Hearts Abishola",
              "NCIS Hawaii", "THE Big Leap", "Emily in Paris", "4400", "Insecure", "Nancy Drew", "The Morning Show",
              "The Neighbourhood", "Riverdale", "The Flash", "The Resident", "chucky", "Alex Rider", "Invasion",
              "Superman and Lois", "Magnum Pi", "Blue Bloods", "See", "CSI Vegas", "Lost In Space", "The Box",
              "The Sex Lives Of College Girls", "The Rookie", "Landscapers", "Sex Education", "Kevin Can Fuck Himself",
              "Sex Life", "Never Have I Ever", "And Just Like That", "The oval", "Hawkeye", "Queens", "Rick and Morty",
              "Tom and Jerry in New York", "Lie With Me", "Star Trek Discovery", "The Witcher", "Big Sky", "MacGruber",
              "The Expanse", "Ragdoll", "Station Eleven", "Firebite", "Nikita", "Welcome To Earth",
              "Fast & Furios spy Racers", "Yellowjackets", "Power Book II Ghost", "Dexter", "Day Of The Dead",
              "Godfather Of Harlem", "Blood And Water", "Cursed", "1883", "Demon Slayer Kimetsu No Yaiba", "La Brea",
              "What If", "Strike Back", "supergirl", "The Blacklist", "You", "Dynasty", "Station 19", "Tyler Perrys Sistas",
              "Arrow", "Wu Assassins", "Daredevil", "Into The Badlands", "Greys' Anatomy", "The Good Doctor", "Lupin",
              "Hightown", "Outer Banks", "Game of Thrones", "The 100", "Utopia", "DC's Legends of Tomorrow",
              "Designated Survivor", "The Last Ship", "11.22.63", "Letterkenny", "Vikings", "911 Lone Star", "Kenan",
              "Cobra Kai", "Young Justice", "Around The World In 80 Days", "The Equilizer", "F Is For Family", "Family Guy",
              "ELITE", "Stay Close", "The Cleaning Lady", "The Tourist", "This Is Us", "FBI International", "Chicago Med",
              "MacGyver", "The Conners", "Gossip Girl", "The Outpost", "The Big Theory", "Bodyguard", "Deadly Class",
              "Blackish", "Chicago Fire", "Hawaii Five 0", "Coroner", "Star Trek Pridogy", "Bull", "Young Sheldon", "Naomi",
              "A Discovery of Witches", "Screw", "68 Whiskey", "Altered Carbon", "American Crime Story", "Dark", "Banshee",
              "Spartacus", "A Million Little Things", "Wolf Like Me", "Archive 81", "Peacemaker", "Euphoria", "After Life",
              "Attack On Titan", "New Amsterdam", "How I Met Your Father", "The Book Of Boba Fett", "Good Sam",
              "Shannara Chronicles", "Ozark", "Jaguar", "The Hardy Boys", "The Flight Attendant", "The Mandalorian",
              "Dracula", "Soulmates", "Equinox", "Paranormal", "Billions", "The Righteous Gemstones", "Trigger point",
              "The Gilded Age", "Ghosts", "Locked Up (Vis a vis)", "Snowpiercer", "Two Sentence Horror Stories",
              "In From The Cold", "All Of Us Are Dead", "The Afterparty", "The Responder",
              "The Woman in the House Across the Street from the Girl in the Window", "Resident Alien", "Pam and Tommy",
              "Raising Dion", "Reacher", "Skam", "Servant", "Raised By Wolves", "Power Book IV: Force", "Murderville",
              "Love, Death & Robots", "Chloe", "Jane The Virgin", "Abbott Elementary", "Astrid And Lilly Save The World",
              "Neymar: The Perfect Chaos", "Women Of Movement", "Single Drunk Female", "Promised Land", "Super Crooks",
              "Suspicion", "Somebody Somewhere", "Person of Interest", "Dollface", "Inventing Anna", "Bel-Air",
              "The Last Kingdom", "Scandal", "Space Force", "Snowdrop", "Young Wallander", "Severance",
              "The Marvelous Mrs. Maisel", "The Walking Dead", "Scream", "Treadstone", "Beauty and the Beast", "From",
              "Super Pumped", "Vikings: Valhalla", "Black Lightning", "The Endgame", "Star Trek Picard", "The Dropout",
              "Kung-Fu", "Good Trouble", "Theodosia", "Snowfall", "The Last Days Of Ptolemy Grey",
              "Formula 1: Drive to Survive", "Walker", "The Office", "Charmed", "B Positive", "Peaky Blinders",
              "All American: Homecoming", "All American", "Minx", "DMZ", "Our Flag Means Death", "We Crashed",
              "Law & Order: Organized Crime", "Life and Beth", "That Dirty Black Bag", "Bridgerton", "Pachinko", "Halo",
              "Marvel Studios Assembled", "Pieces of Her", "Parallels", "Atlanta", "Killing Eve",
              "The Girl from Plainville", "Better Things", "Moon Knight", "Young Rock", "Lethal Weapon",
              "The Vampire Diaries", "Tomorrow", "Slow Horses", "Shining Vale", "Tokyo Vice", "61st Street",
              "Gentleman Jack", "Fear The Walking Dead: Dead In The Water", "Ice Age: Scrat Tales", "The Queen's Gambit",
              "Derry Girls", "The Boarding School Las Cumbres", "The Originals", "Roar", "Outer Range",
              "Anatomy Of A Scandal", "Why Didnt They Ask Evans?", "Fear The Walking Dead", "Swimming With Sharks",
              "The First Lady", "Russian Doll", "Pacific Rim: The Black", "My Brilliant Friend", "Icarly", "Julia",
              "the Rising", "Heartstopper", "Sanditon", "The Man Who Fell To Earth", "Gaslit", "Hilda", "Billy The Kid",
              "Outlander", "Mai: A Mother's Rage", "Under The Banner Of Heaven", "We Own This City", "Barry", "The Offer",
              "Undone", "Manifest", "Shining Girls", "Winning Time: The Rise of the Lakers Dynasty", "The Baby",
              "Welcome to Eden", "Clark", "Dragons: The Nine Realms", "The Pentaverate", "Blood Sisters", "Bosch Legacy",
              "Made for Love", "The Sound of Magic", "The Wilds", "Star Trek: Lower Decks", "Candy", "Better Call Saul",
              "The Lincoln Lawyer", "Games People Play", "The Time Traveler", "Hacks", "The Staircase",
              "Star Trek: Strange New Worlds", "Love, Death & Robots", "Night Sky", "The Essex Serpent", "Heroes",
              "P-Valley", "Hannibal", "Obi-Wan Kenobi\n", "Tehran", "Prehistoric Planet", "Stranger Things", "Atlantis",
              "Angelyne", "Duncanville", "Good Omens", "Tacoma FD", "The Affair", "Gomorrah", "Bosch", "ShadowHunters",
              "13 Reasons Why", "Iron Fist", "The Defenders", "Shooter", "Pistol", "Breeders", "Mayans M.C", "The Boys",
              "Physical", "Roswell, New Mexico", "Irma Vep", "In The Dark", "Warrior Nun", "All Rise",
              "Once Upon a Time in Londongrad", "The Orville", "Intelligence", "For All Mankind", "First Kill",
              "Conversations with Friends", "Des", "Disenchantment", "George Carlins American Dream", "Evil", "Intimacy",
              "Becoming Elizabeth", "Dark Winds", "Top Gear", "Love Victor", "Ms. Marvel", "Sherwood",
              "God's Favorite Idiot", "Tom Swift", "America's Got Talent", "The Old Man", "The Lazarus Project",
              "Dead End: Paranormal Park", "Better Call Saul Presents: Slippin' Jimmy", "Goliath", "The Orbital Children",
              "Motherland: Fort Salem", "Money Heist: Korea ", "Man vs. Bee", "The Chi", "The Summer I Turned Pretty",
              "The Umbrella Academy", "Loot", "Who Killed Sara?", "So You Think You Can Dance", "The Lake",
              "Only Murders in the Building", "Animal Kingdom", "Westworld", "The Outlaws", "Prison Break",
              "The Terminal List", "Baymax", "Aoashi", "Bad Sport", "Last Chance U: Basketball", "The Undeclared War",
              "Troppo", "They Call Me Magic", "The Croods: Family Tree", "Spy X Family", "Rutherford Falls",
              "Power Book III: Raising Kanan", "Transporter: The Series", "Black Bird", "Moonhaven",
              "Marvel Studios: Legends", "Control Z", "Boo, Bi-tch", "Fatma", "Invicible", "Them", "Hit-Monkey",
              "Santa Inc.", "The Nevers", "The Falcon and the Winter Soldier", "Stargirl", "Gangs of London", "Spy City",
              "Ragnarok", "Mind Over Murder", "Inhumans", "Big Mouth", "Big Little Lies", "Taboo", "American Gods",
              "Godless", "The Sinner", "What We Do in the Shadows", "Solar Opposites", "D.B. Cooper: Where Are You?!",
              "Resident Evil", "Kung Fu Panda: The Dragon Knight", "Farzar", "Blood And Treasure", "Bucchigire!",
              "Boruto: Naruto Next Generations", "Grown-ish", "Virgin River", "Jurassic World: Camp Cretaceous",
              "Standup and Away! with Brian Regan", "The Last Movie Stars", "Primal", "Miss Scarlet and the Duke", "Trying",
              "The Rehearsal", "James May: Our Man in Italy", "Jane Eyre", "Uncoupled", "Are You Afraid of the Dark?",
              "Paper Girls", "Players", "Surface", "Black Spot", "Keep Breathing", "The Resort",
              "Pretty Little Liars: Original Sin", "American Horror Stories", "Snake in the Grass",
              "The Most Hated Man On The Internet", "Tuca & Bertie", "City On A Hill", "Harley Quinn",
              "All the Same... or Not", "Industry", "Reservation Dogs", "Uncle From Another World",
              "All or Nothing: Arsenal", "Yasuke", "Trese", "Sweet Tooth", "The Silent Sea", "Power", "Locke & Key",
              "Star Wars; Rebels", "Bridge and Tunnel", "The Anarchists", "I Am Groot", "Surviving Escobar: Alias JJ",
              "The Sandman", "High School Musical: The Musical - The Series", "Shoot! Goal to the Future", "Colosseum",
              "UFO", "School Tales the Series", "Dota: Dragon’s Blood", "Beavis and Butt-Head", "13: The Musical",
              "This Fool", "Password", "Everything", "Five Days at Memorial", "Flatbush Misdemeanors",
              "Running Wild With Bear Grylls: The Challenge", "A League of Their Own", "Tales of the Walking Dead",
              "Legacy: The True Story of the LA Lakers", "Rabbids Invasion", "Family Law", "A Model Family",
              "The Knights of Castelcorvo", "After The Verdict", "Aftermath", "Again My Life", "Agatha Christie's Marple",
              "Agatha Raisin", "Hotties", "Bunnicula", "Hamster & Gretel", "Halston", "Halt and Catch Fire", "Inside Pixar",
              "Children of the Underground", "American House Wife", "Knightfall", "Castle", "Castle Rock", "Imposters",
              "She-Hulk: Attorney at Law", "Tekken: Bloodline", "He-Man and the Masters of the Universe", "Selena + Chef",
              "Shetland", "Bad Sisters", "Echoes", "Rap Sh!t", "The Girl in the Mirror", "Schulz Saves America", "Sprung",
              "Code Black", "1000 Ways to Die", "Criminal Minds", "House of the Dragon", "Kleo", "The Cuphead Show!",
              "Special OPS", "Below Deck Mediterranean", "Beat Shazam", "Angels in America", "Fleabag",
              "Goblin: The Lonely and Great God", "Horace and Pete", "LEGO Star Wars: The Freemaker Adventures",
              "LEGO Star Wars: The Resistance Rises", "Luke Cage", "Man With A Plan", "Medici: Masters of Florence",
              "Preacher", "Private Eyes", "Archer", "Lost Ollie", "Delhi Crime", "Chad & JT Go Deep", "Mo", "The Twelve",
              "Mike", "The Crown", "The Girlfriend Experience", "The Grand Tour", "Van Helsing", "Kidding", "My Mister",
              "Interrogation Raw", "Welcome to Wrexham", "Little Demon", "Partner Track", "The Patient",
              "The Lord of the Rings: The Rings of Power", "The Ipcress File", "Pantheon", "The Capture",
              "The Rising of the Shield Hero(Tate no Y?sha no Nariagari)"]

    # series = ['The Rising of the Shield Hero(Tate no Y?sha no Nariagari)', 'The Capture', 'Pantheon', 'The Ipcress File', 'The Lord of the Rings: The Rings of Power']
    # Create top_items as empty list
    all_products = []
    # unavailable = []
    all_products2 = []
    # loop through series
    for s in series:
        # Make a request
        page = requests.get(
            "https://www.themoviedb.org/search?query=" + s)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Extract and store in top_items according to instructions on the left
        products = soup.select('div.details')
        if not products:
            # unavailable_series from tmdb
            if all_products2.append({
                "name": s,
                "tmdb": "unavailable"

            }):
                print("No results found for " + s)
        else:
            for product in products:
                name = product.find('h2').get_text()

                # description = product.find('p').get_text()
                price = product.find('a')['href']
                # reviews = product.select('div.ratings')[0].text.strip()
                # image = product.find('img.poster')

                # check the first characters before 2nd /  /tv/ /movie/
                res1 = price.partition('/')[-1]
                res = res1.partition('/')[0]
                # print(res)

                # check if serie isn't available
                if name == s and res == 'tv':
                    all_products.append({
                        "name": name,
                        # "description": description,
                        "TMDB_ID": price,
                        # "reviews": reviews,
                        # "image": image
                    })
                else:
                    # print(f"Serie not available on TMDB: {s}")
                    pass

    # available series from tmdb
    keys = all_products[0].keys()
    # unavailable series from tmdb
    keys2 = all_products2[0].keys()

    # write available series to csv
    with open('products.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_products)

    # write unavailable series to csv
    with open('unavailable.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys2)
        dict_writer.writeheader()
        dict_writer.writerows(all_products2)


# reworked function
def reworked():
    start = time.time()
    all_products = []
    # unavailable = []
    all_products2 = []

    all_products2.append({
        "id": "placeholder",
        "name": "placeholder",
        "tmdb": "placeholder",
        "year": "placeholder",
    })
    # iterate over each line as a ordered dictionary and print only few column by column name
    counter = 0
    with open('col33all.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            # print(row['a_id'], row['s_name'])

            # get tmdb id
            page = requests.get('https://www.themoviedb.org/search?query=' + row['s_name'])
            soup = BeautifulSoup(page.content, 'html.parser')
            # Extract and store in top_items according to instructions on the left
            products = soup.select('div.details')
            if not products:
                # unavailable_series from tmdb
                if all_products2.append({
                    "id": row['a_id'],
                    "name": row['s_name'],
                    "tmdb": "unavailable",

                }):
                    print("No results found for " + row['s_name'])
            else:
                for product in products:
                    name = product.find('h2').get_text()
                    price = product.find('a')['href']
                    year1 = product.find('span', class_='release_date')
                    strvalue1 = "".join(str(year1))
                    strvalue2 = strvalue1.replace('"', '')
                    strvalue = strvalue2.replace(',', 'x')
                    after1 = strvalue.partition('x')[2]
                    after = after1.replace('</span>', '')
                    year = after

                    # check the first characters before 2nd /  /tv/ /movie/
                    res1 = price.partition('/')[-1]
                    res = res1.partition('/')[0]
                    # print(res)

                    #test print
                    # print(name)
                    # # print(price)
                    # print(year)
                    # print(res)
                    # check if serie isn't available
                    if name.lower() == row['s_name'].lower() and res == 'tv' or year == row['realese_yr']:
                        print(counter)
                        all_products.append({
                            "id": row['a_id'],
                            "name": name,
                            "TMDB_ID": price,
                            "year": year,
                            # "id": "dsd",
                            # "name": "name",
                            # "TMDB_ID":" price",
                            # "year": "year",
                        })
                        counter += 1
                    else:
                        # print(f"Serie not available on TMDB: {s}")and year == row['realese_yr']
                        # check if id already in list
                        idn = 0
                        for lst in all_products:
                            # print(lst['id'])
                            if row['a_id'] in lst['id']:
                                # print("id already in list")
                                idn = row['a_id']
                        if res == 'tv' and row['a_id'] != idn:
                            all_products2.append({
                                "id": row['a_id'],
                                "name": row['s_name'],
                                "tmdb": price,
                                "year": year,
                            })


# available series from tmdb
    keys = all_products[0].keys()
    # unavailable series from tmdb
    keys2 = all_products2[0].keys()

    # write available series to csv
    with open('products33all.csv', 'w', newline='', encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_products)

    # write unavailable series to csv
    with open('unavailable33all.csv', 'w', newline='', encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys2)
        dict_writer.writeheader()
        dict_writer.writerows(all_products2)


    end = time.time()
    print(f"Time of execution = {end - start}")




# test function
def test():
    filename = 'unavailable.csv'
    df = pd.read_csv(filename)

    for index, row in df.iterrows():
        # print(row['name'])
        # print(row['name']
        i=7
        # print(row)

        # get tmdb id
        series  = ['The Rising of the Shield Hero(Tate no Y?sha no Nariagari)', 'The Capture', 'Pantheon', 'The Ipcress File', 'The Lord of the Rings: The Rings of Power']

        all_products = []
        for s in series:
            page = requests.get("https://www.themoviedb.org/search?query=" + s)
            soup = BeautifulSoup(page.content, 'html.parser')
            products = soup.select('div.details')
            if not products:
                print("No results found for " + s)
            else:
                for product in products:
                    name = product.find('h2').get_text()
                    price = product.find('a')['href']
                    year1 = product.find('span', class_='release_date')
                    # print(year)

                    # strValue = '<span class="release_date">September  3, 2019</span>'
                    strvalue1 = "".join(str(year1))
                    #remove "" from string
                    strvalue2 = strvalue1.replace('"', '')
                    #replace , with x
                    strvalue = strvalue2.replace(',', 'x')
                    # print(strvalue)
                    # # # Remove all characters before the character '-' from string
                    # before, sep, after = strvalue.partition(',')
                    after1 = strvalue.partition('x')[2]
                    after = after1.replace('</span>', '')
                    # if len(after) > 0:
                    #     strValue = after
                    # # # print(strValue.replace('</span>', ''))
                    # year = after.replace('</span>', '')
                    year = after
                    print(F"year ==========> {year}")

                    # check the first characters before 2nd /  /tv/ /movie/
                    res1 = price.partition('/')[-1]
                    res = res1.partition('/')[0]
                    # print(res)
                    # check if serie isn't available
                    if name == s and res == 'tv':
                        all_products.append({
                            "name": name,
                            "TMDB_ID": price,
                            "year": year,
                        })
                    else:
                        # print(f"Serie not available on TMDB: {s}")
                        pass

                print(all_products)


# get genre function
def get_genre():
    start = time.time()
    filename = 'products33all.csv'
    df = pd.read_csv(filename)
    # store all genres in list
    all_genres = []

    # execute 10 queries test
    i = 0
    for index, row in df.iterrows():
        # if i < 3:
        # print(row['name'])
        # print(row['TMDB_ID'])
        tv_id = row['TMDB_ID']
        # get remote data
        page = requests.get("https://www.themoviedb.org" + tv_id)
        soup = BeautifulSoup(page.content, 'html.parser')
        # extract genre
        genre1 = soup.find('span', class_='genres').text
        # replace ",&nbsp;" with ""
        genre2 = genre1.replace(",&nbsp;", "")
        # replace " " with ""
        genre = genre2.replace("\n", "")
        # replace .0 in year with ""
        year = int(row['year'])
        # print(genre)
        # store genre in list
        all_genres.append({
            "id": row['id'],
            "name": row['name'],
            "TMDB_ID": row['TMDB_ID'],
            "year": year,
            "genre": genre,
        })

        i += 1
        print(i)

    # print(all_genres)
    # write to genres csv
    key = all_genres[0].keys()
    with open('genres.csv', 'w', newline='', encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, key)
        dict_writer.writeheader()
        dict_writer.writerows(all_genres)

    end = time.time()
    print(f"Time of execution = {end - start}")
    # write to csv
    # csv_input = pd.read_csv('unavailable.csv')
    # csv_input['Genres'] = csv_input['name']
    # csv_input.to_csv('unavailable2adds.csv', index=False)


# clean csv function
def clean_csv():
    count = 1
    missing = []
    with open('products33all.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            if row['id'] != count:
                missing.append({
                    "id": count,
                    "name": row['id'],
                })
            count += 1

    print(count)
    print(missing)

# call main function
if __name__ == "__main__":
    # test()
    # test()
    get_genre()
    # reworked()
    # clean_csv()