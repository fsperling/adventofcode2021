file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

data = data.replace('\n','')
values = data.split(",")

fishes = [0] * 9
for value in values:
    fishes[int(value)] += 1

daysleft = 256
while(daysleft):
   nextday = [0] * 9
   for i in range(0, len(fishes)):
       if(i == 6):
           nextday[6] = fishes[0]
       if(i == 8):
           nextday[8] = fishes[0]
       else:
           nextday[i] += fishes[i+1]

   fishes = nextday.copy()
   daysleft -= 1

print(f'number of fishes: {sum(fishes)}')
