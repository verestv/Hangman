import pickle
def choose_topic(x):
    with open('pickle.dat','rb') as words:
        dictionary = pickle.load(words)    

    if x =='f':

        return dictionary.get('food')
    if x =='g':

        return dictionary.get('geog')
    if x == 'c':

        return dictionary.get('cars')
    if x =='a':

        return dictionary.get('animals')
    if x == 'cl':

        return dictionary.get('clothes')
    if x == 'r':

        random = dictionary.get('food') + dictionary.get('geog') + dictionary.get('cars') + dictionary.get('animals') + dictionary.get('clothes')
        return random
    else:
        pass
    #set_of_words = {'food' : ['lasaghna','kebab','pizza','burger','sushi','cake','onion','cucumber','potato','tomato','borsch','barbeque','apple','pineapple'],

    #'geog' : ['seul','columbia','odessa','london','ottava','kiyv','lviv','paris','dnipro','herson','boryspil','Monaco','Spain','australia'],

    #'cars' : ['bmw','audi','volkswagen','honda','chevrolet','citroen','mercedes','skoda','kia','ford','jeep','porsche','lamborghini','ferrari'],

    #'animals' : ['elephant','pig','rabbit','tiger','bear','goat','horse','dog','cat','chicken','geeraf','goose','fish','worm','mouse','bird'],

    #'clothes' : ['shirt','jeens','sweater','t-shirt','bandana','socks','sneakers','cap','jacket','hat','mask','shorts','hoodie','pants','glasses']}
    
#with open('pickle.dat','wb') as pickle_file:
    #pickle.dump(set_of_words,pickle_file) 


  