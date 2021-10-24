
## TODO: Add the Needed imports Here ##
from model import Model


def predict(sentences):
    model = Model()
    '''
    Arguments
    This Function takes LIST of sentences as an argument (List of Strings) -> ["sent1", "sent2", "sent3"] 

    Returns 
    List of Numeric Prediction Aka ClassNumber as Given Example [1, 3, 5, 12, ...etc] 
    '''
    
    predictions = [model.predict(sentence) for sentence in sentences]
    


    ## ToDo: Write Your Code HERE! ##

    return predictions

### DON'T WORRY ABOUT IT :) ###
## Machathon Technical Team Send their regards