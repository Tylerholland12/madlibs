import re

model = "<name> went to the store to buy <grocery iterm>'s. <name> saw <friend's name> at the store. The two talked about <object>'s for the rest of the time <he/she/they> was in the store. When <he/she/they> left the store <name> went to <place> for a few hours. While they were there they saw <animal>'s and began to take pictures of it because <he/she/they> had never seen one in person before. Once <name> had all the pictures <he/she/they> wanted <name> went to <place> and started to do <activity> for the rest of the night. <name> started <verb> once <he/she/they> noticed that it wasn't really the night time. <He/She/They> started moving <adverb> when the <he/she/they> realized that the day had really been going in reverese the entire day. When <he/she/they> realized that the day had been moving in reverse <he/she/they> decided to go to <planet> and live there instead. Once <name> got to <planet> <he/she/they> found out that there were already <blue animal, brown animal, yellow animal> living on this planet and decided to <verb2> with the animals."

def paragraph(model):
    print(model)
    fields = sorted(set( re.findall('<[^>]+>', model) ))
    values = input('\nInput a comma-separated list of words to replace the following items' '\n  %s: ' % ','.join(fields)).split(',')
    
    story = model 
    for fi, va in zip(fields, values):
        story = story.replace(fi, va)
        print('\nThe madlib is:\n\n' + story)
paragraph(model)