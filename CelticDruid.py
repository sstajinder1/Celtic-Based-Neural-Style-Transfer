# https://horoscopes.astro-seek.com/celtic-tree-zodiac-horoscope
"""
* Note: Celtic Druids did not determine Sign based on the actual date of birth but rather by the date of conception. For example, if you were born three weeks before the scheduled date, you need to add these three weeks to the actual date of birth, in order to figure out the appropriate Sign. 
"""

from datetime import date
from dateutil.parser import parse
"""
dic = {
 "Apple":["Love","Creativity","Magic","Youthful","Immortality","Splendor","Sensitive","Sentimental","Divine","Petite","Attractive","Charming","Warmhearted","Unselfish","Guideless","Light-headed","Intelligent","Savvy","Logical","Curious","Mystic","Monotonous","Flawless","Tedious","Free-spirited"],
 "Ash":["Massive","Wide","Tall","Self-Answered","Overconfident","Pampered","Straightforward","Selfish","Not Greedy","Not Shy","Needy","Demanding","Happy"],
 "Beech":["Beauty","Liveliness","Flexibility","Creativity","Compromise","Independent","Romantic","Straightforward","Impatient","Value money","Prefer Health"],
 "Birch":["Purity","Rebirth","Cleansing","Healing","Flexible","Easy-going","Soothing","Calm","Tactful","Considerate","Consistent","Soft","Gentle","Glamorous","Lazy","Sentimental","Happy","Quiet","Peaceful","Creative","Talented","Extraordinary"],
 "Cedar":["Strong","Magnificient","Aromatic wood","Unmistakable","Silhouette","Healing","Cleansing","Protection","Beautiful","Self-Reliant","Find solutions to toughest problems","Tyrant","Trustworthy","Modesty","Shyness","Lack of self-confidence","Self-Assured","Unbeatable","Extreme Optimists"],
 "Chestnut":["Fertility","Abundance","Longevity","Invigoration","Rejuvenation","Honest","Straight-forward","Great Potential","Wise","Extra cautious","Not Stubborn","Moody","Intellectual","Courageous","Down to earth","Organized"],
 "Cypress":["Role of sacrifice","Mourning","Death","Despair","Hope","Slender","Strong","Stern and Wild","Adaptable","Low-Maintenance","Easily adjust","Find Happiness","Mature","Independent","Not Sentimental","A bit rude","But Sensiitve","Harsh yet calm","Radiate tranquility and they can be quite pleasant","Dreamers","Flexible","Loyal","Faithful"],
 "Elm":["Dense","Strong","Big","Slender","Beautiful","Sentimental","Reserved","Simple","Laid-back","Calm","Even-tempered","Sluggish","Annoying","Generous","Open","Straightforward","Discrete","Very Responsible","Supporting","Protecting","Passionate","Fervid","Amazing","Skilled","Quite Pleasant","Stress free"],
 "Fig":["Lovely","Trustworthy","Lazy","Fight their idleness","Hardworking","Very efficient","Energetic","Very Sensitive","Vulnerable Creatures","Fragile","Doubtful","Never Demanding or unreasonable"],
 "Fir":["High esteem","Dull","Friendship","Resilience","Perceptiveness","Longevity & Honesty","Very Sensory oriented","Capricious","Lonely","Demanding","Can't Negotiate","Intellectual","Scrupulousness","Oustanding","Ethical","Noble","Optimistic","Provide"],
 "Hazel":["Creativity","Awareness","Amazing","Insights","Imagination","Calm","Quiet","Charming","Full of virtue","Skillfull","Adapt","Warm-Hearted","Kind","Wise","Wrathful","Irrational","Emotional","Passionate","Very careful","Compassionate"],
 "Hornbeam":["Straightforwardness","Strength","Determination","Growth","Warmth","Ethics","Loyalty","Pretty","Lacks leadership","Accurate","Precise","Inefficient","Emotional","Harmonious"],
 "Jasmine":["Fragile","Sociable","Amiable","Delicate","Cheerful","Carefree","Not materialistic","Workaholics","Pessimists","Faithful","Comfortable"],
 "Linden":["Exceptionally good","Sacred","Divine","Luck","Very pleasant","Amiable","Charming","Joyful","Carefree","Lazy","Comforting","Powerful","Responsible","High self-esteem","Self respect","Suspicious","Jealous"],
 "Maple":["Success","Prosperity","Positive","Pleasant","Cheerful","Joyful","Active","Dynamic","Adventurous","Gorgeous","Outrageous","Outstanding","Daring","Irrespressible Energy","Restless","Courageous","Trustworthy","Logical","Quite cyncial","Attention seeker"],
 "Mountain Ash":["Pleasant","Charming","Even-tempered","Friendliness","Independent","Self-centered","Over thinkers","Lack simplicity","Very Attentive","Beautiful","Long for perfection","Honest","Loyal","Reliable","Perfectionists","Extremely generous","Demanding"],
 "Nutwood":["Adaptable","Interesting","Quite Contradictory","Very Friendly","Self-centered","Egoist","Unpredictable","Aggressive","Lovey-dovey","Indifferent","Confident","Meaners","Dominating","Endearment","Considerate","Modest","Independent"],
 "Oak":["Endurance","Nobility","Strength","Energy","Beauty","Flexibility","Brave","Courageous","Forgiving","Strong willpower","Self-control","Sense of compromise","Independent","Capable","Conservative","Orderly","Ambitious","Hardworker"],
 "Olive":["Symbolically","Famously","Strength","Pursification","Fruitfulness","Pretty","Laidback","Non aggressive personality","Indifferent","Considerate","Tactful","Amiable","Fair","Calm","Easy-going","Very Passionate","Analytical Mind","Leaver","Very generous","Positive Disposition"],
 "Pine":["Creativity","Longevity","Hope","Pity","Boldness","Imoortality","Beautiful","Healthy","Very Pleasant","Very Persistent","Goal oriented","Intelligent","Sophisticated","Picky","Fickle","Extremely profound","Accurate","Thoughtful","Efficient","Very Generous","Carefree","Nostalgic"],
 "Poplar":["Hope","Beautiful","Slender","Elegant","Troublesome","Self conscious","Positive","Careful","Fragile","Very brave","Courageous","Cheerful","Laid back","Not materialistic","Quite attruistic","Concerned","Sensitive","Critical","Astute"],
 "Willow":["Supple","Graceful","Beautiful","Calming","Attractive","Inexplicable charm","Highly intuitive","Powerful","Fragile","Emotional","Tough","Determined","Quite Reserved","Persistent","Straightforward","Dull","Exaggeration","Masochists"]
}
"""

dic = {
 "Apple":["love","Creativity","Magic","Youthful","Immortality","Splendor","Sensitive","Sentimental","Divine","Petite","Attractive","Charming","Warmhearted","Unselfish","Guideless","Delirious","Intelligent","Savvy","Logical","Curious","Mystic","Monotonous","Flawless","Tedious"],
 "Ash":["Massive","Wide","Tall","Hypophora","Overconfident","Pampered","Straightforward","Selfish","Temperate","Bold","Needy","Demanding","Happy"],
 "Beech":["Beauty","Liveliness","Flexibility","Creativity","Compromise","Independent","Romantic","Straightforward","Impatient","Worth"],
 "Birch":["Purity","Rebirth","Cleansing","Healing","Flexible","Carefree","Soothing","Calm","Tactful","Considerate","Consistent","Soft","Gentle","Glamorous","Lazy","Sentimental","Happy","Quiet","Peaceful","Creative","Talented","Extraordinary"],
 "Cedar":["Strong","Magnificient","Odoriferous","Unmistakable","Silhouette","Healing","Cleansing","Protection","Beautiful","Independent","Engineer","Tyrant","Trustworthy","Modesty","Shyness","Diffidence","Assurance","Unbeatable","Optimist"],
 "Chestnut":["Fertility","Abundance","Longevity","Invigoration","Rejuvenation","Honest","Simple","Wise","Compliant","Moody","Intellectual","Courageous","Liberal","Organized"],
 "Cypress":["Sacrificing","Mourning","Death","Despair","Hope","Slender","Strong","Arrogance","Adaptable","Untroublesome","Adjustable","Mature","Independent","Practical","Rude","Sensitive","Harsh","Radiance","Tranquil","Pleasant","Dreamers","Flexible","Loyal","Faithful"],
 "Elm":["Dense","Strong","Big","Slender","Beautiful","Sentimental","Reserved","Simple","Relaxed","Calm","Composed","Sluggish","Annoying","Generous","Open","Straightforward","Discrete","Responsible","Supporting","Protecting","Passionate","Fervid","Amazing","Skilled","Soothing","Unstressed"],
 "Fig":["Lovely","Trustworthy","Lazy","Hardworking","efficient","Energetic","Sensitive","Vulnerable","Fragile","Doubtful","Unreasonable"],
 "Fir":["Esteemed","Dull","Friendship","Resilient","Perceptiveness","Longevous","Honest","Reflexous","Capricious","Lonely","Demanding","Unbendable","Intellectual","Scrupulousness","Oustanding","Ethical","Noble","Optimistic","Provide"],
 "Hazel":["Creativity","Awareness","Amazing","Insights","Imagination","Calm","Quiet","Charming","Ethical","Skillfull","Adapt","Humane","Kind","Wise","Wrathful","Irrational","Emotional","Passionate","careful","Compassionate"],
 "Hornbeam":["Straightforwardness","Strength","Determination","Growth","Warmth","Ethics","Loyalty","Pretty","Subservience","Accurate","Precise","Inefficient","Emotional","Harmonious"],
 "Jasmine":["Fragile","Sociable","Amiable","Delicate","Cheerful","Carefree","Spiritual","Workaholics","Pessimists","Faithful","Comfortable"],
 "Linden":["Excellent","Sacred","Divine","Luck","pleasant","Amiable","Charming","Joyful","Carefree","Lazy","Comforting","Powerful","Responsible","Pride","Dignified","Suspicious","Jealous"],
 "Maple":["Success","Prosperity","Positive","Pleasant","Cheerful","Joyful","Active","Dynamic","Adventurous","Gorgeous","Outrageous","Outstanding","Daring","Energetic","Restless","Courageous","Trustworthy","Logical","cyncial","Ostentatious"],
 "Mountain Ash":["Pleasant","Charming","Friendliness","Independent","Thinkers","Complicated","Attentive","Beautiful","Perfectionist","Honest","Loyal","Reliable","Perfectionists","Generous","Demanding"],
 "Nutwood":["Adaptable","Interesting","Contradictory","Friendly","Selfish","Egoist","Unpredictable","Aggressive","Fervent","Indifferent","Confident","Meaners","Dominating","Endearment","Considerate","Modest","Independent"],
 "Oak":["Endurance","Nobility","Strength","Energy","Beauty","Flexibility","Brave","Courageous","Forgiving","Determined","Restraint","Compromising","Independent","Capable","Conservative","Orderly","Ambitious","Hardworker"],
 "Olive":["Symbolically","Famously","Strength","Pursification","Fruitfulness","Pretty","Laidback","Shy","Indifferent","Considerate","Tactful","Amiable","Fair","Calm","Unworied","Passionate","Analytical","Leaver","Generous","Apathetic"],
 "Pine":["Creativity","Longevity","Hope","Pity","Boldness","Imoortality","Beautiful","Healthy","Pleasant","Persistent","Energetic","Intelligent","Sophisticated","Picky","Fickle","Intense","Accurate","Thoughtful","Efficient","Generous","Carefree","Nostalgic"],
 "Poplar":["Hope","Beautiful","Slender","Elegant","Troublesome","Nervous","Positive","Careful","Fragile","brave","Courageous","Cheerful","Unexcited","Intellectual","Altruistic","Concerned","Sensitive","Critical","Astute"],
 "Willow":["Supple","Graceful","Beautiful","Calming","Attractive","Charming","Intuitive","Powerful","Fragile","Emotional","Tough","Determined","Reserved","Persistent","Straightforward","Dull","Exaggeration","Masochists"]
}


def Celtic(d1):
    y = (d1.year)
    ret = ""
    if((date(y,1,2)<=d1<=date(y,1,11))or(date(y,7,3)<=d1<=date(y,7,13))):
        ret = "Fir"
    elif((date(y,1,12)<=d1<=date(y,1,22))or(date(y,7,14)<=d1<=date(y,7,24))):
        ret = "Elm"
    elif((date(y,1,23)<=d1<=date(y,1,31))or(date(y,7,25)<=d1<=date(y,8,4))):
        ret = "Cypress"
    elif((date(y,2,1)<=d1<=date(y,2,10))or(date(y,8,5)<=d1<=date(y,8,14))):
        ret = "Poplar"
    elif((date(y,2,11)<=d1<=date(y,2,20))or(date(y,8,15)<=d1<=date(y,8,24))):
        ret = "Cedar" #"Larch"
    elif((date(y,2,21)<=d1<=date(y,3,2))or(date(y,8,25)<=d1<=date(y,9,3))):
        ret = "Pine"
    elif((date(y,3,3)<=d1<=date(y,3,12))or(date(y,9,4)<=d1<=date(y,9,13))):
        ret = "Willow"
    elif((date(y,3,13)<=d1<=date(y,3,20))or(date(y,9,14)<=d1<=date(y,9,22))):
        ret = "Linden" #"Lime"
    # Spring Equinox
    elif(date(y,3,21) == d1):
        ret = "Oak"
    # Autumnal Equinox
    elif(date(y,9,23) == d1):
        ret = "Olive" #"Alder"
    elif((date(y,3,22)<=d1<=date(y,3,31))or(date(y,9,24)<=d1<=date(y,10,2))):
        ret = "Hazel"
    elif((date(y,4,1)<=d1<=date(y,4,10))or(date(y,10,3)<=d1<=date(y,10,11))):
        ret = "Mountain Ash" #"Rowan"
    elif((date(y,4,11)<=d1<=date(y,4,20))or(date(y,10,12)<=d1<=date(y,10,21))):
        ret = "Maple"
    elif((date(y,4,21)<=d1<=date(y,4,30))or(date(y,10,22)<=d1<=date(y,10,31))):
        ret = "Nutwood" #"Walnut"
    elif((date(y,5,1)<=d1<=date(y,5,10))or(date(y,11,1)<=d1<=date(y,11,10))):
        ret = "Jasmine" #"Poplar"
    elif((date(y,5,11)<=d1<=date(y,5,20))or(date(y,11,11)<=d1<=date(y,11,20))):
        ret = "Chestnut"
    elif((date(y,5,21)<=d1<=date(y,5,30))or(date(y,11,21)<=d1<=date(y,11,30))):
        ret = "Ash"
    elif((date(y,5,31)<=d1<=date(y,6,10))or(date(y,12,1)<=d1<=date(y,12,10))):
        ret = "Hornbeam"
    elif((date(y,6,11)<=d1<=date(y,6,20))or(date(y,12,11)<=d1<=date(y,12,20))):
        ret = "Fig" #"Aspen"
    # Summer Solstice
    elif(date(y,6,21) == d1):
        ret = "Birch"
    # Winter Solstice
    elif(date(y,12,21) == d1):
        ret = "Beech"
    elif((date(y,6,22)<=d1<=date(y,7,2))or(date(y,12,21)<=d1<=date(y,12,31))or(date(y,1,1)==d1)):
        ret = "Apple"
    else:
        ret = "e"
    return ret

def Druid(strn):
    try:
        d1 = (parse(strn,dayfirst=True).date())
        return(Celtic(d1))
    except ValueError:
        raise ValueError("Incorrect Date")
    except:
        print("Incorrect Format")

"""
while(True):
    inp = str(input("\n Enter DOB in DD/MM/YYYY format :- "))
    print(Druid(inp))
"""

def CelticDruid(st):
    ki = Druid(st)
    return (ki, dic[ki])
