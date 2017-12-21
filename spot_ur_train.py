import requests
from bs4 import BeautifulSoup

chakra = True
trial = 5

# train_no = 22104
train_no = int(input("Enter the train no."))
days = int(
    input("enter the starting day number..('0' for today, '1' for yesterday, 2 for day before yesterday and so "
          "on...)")) * -1
# days = -1

while chakra and trial >= 0:
    try:
        sc = requests.get("http://spoturtrain.com/status.php?tno=" + str(train_no) + "&date=+" + str(days))
        soup = BeautifulSoup(sc.text, 'lxml')
        tr = soup.find_all("tr")
        for td in tr[1].find_all("font"):
            print(td.getText().strip("\t").strip("\n") + "\n")
        print("-----------------------------------------------------------------------------------\n\n")
        print("Station -> ETA")
        print("--------------")
        for i in range(3, len(tr)):
            rows = tr[i]
            str = ""
            flag = True
            for td in rows.find_all("td"):
                str = str + td.getText().strip('\n') + " "
                if flag:
                    str = str + "-> "
                    flag = False
            print(str)
        chakra = False
        trial -= 1
    except:
        trial -= 1
        print("Kuch toh locha hai... reattempting")
if chakra:
    print("Successfully Failed... Please try again")