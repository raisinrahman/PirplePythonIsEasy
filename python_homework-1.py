# Python Is Easy homework. All about variales

# Favorite Song
song = "Golden Days"
artist = "Pan!c at the Disco"
genre = "alternative pop-rock"
leadSinger = "Brendon Uri"
bandHomeTown = "Las Vegas Neveda"
daysInTop40 = 50
daysInTop10 = 18
album = "Death of a Bachelor"
backFlipsByBrendon = 2
concerts = 5.5
# song and album
albumAndSong = album + " " + song



print(song)
print(artist)
print(genre)
print(leadSinger)
print(bandHomeTown)
print(daysInTop40)
print(daysInTop10)
print(album)
print(backFlipsByBrendon)


"""
Total number of days
Golden Days was on billboard
"""
totalDays = daysInTop10 + daysInTop40

print(albumAndSong)
print(totalDays)

"""
Number of concerts I have been to
that Brendon has not a back flip
"""
noFlips = concerts - backFlipsByBrendon
print(noFlips)

"""
Percentage of back flips per
concert
"""
flipPercentage = (backFlipsByBrendon / concerts) * 100
print(flipPercentage)

