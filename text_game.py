import random 

def battle_axe():
    axe = r"""
                        ____________
                      .~      ,   . ~.
                     /                \
                    /      /~\/~\   ,  \
                   |   .   \    /   '   |
                   |         \/         |
          XX       |  /~~\        /~~\  |       XX
        XX  X      | |  o  \    /  o  | |      X  XX
      XX     X     |  \____/    \____/  |     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     |           '  |     @%%;;@  X       X
X      X     @%%;;@   |. ` ; ; ; ;  ,|   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@
                          @@@  @@@
    """
    print(axe)

battle_axe()


print()
print("#############################")
print("#############################")
print("##                         ##")
print("##       WINTERFROST       ##")
print("##            BY           ##")
print("##      Eric  Johnson      ##")
print("##                         ##")
print("#############################")
print("#############################")

print()
print()
print("The wind howled a mournful dirge, a blackened symphony echoing through the skeletal branches of the deadwood.  Snow, sharp as shattered glass, lashed against Marduk’s face, stinging his eyes even through the thick furs. He pressed onward, his breath pluming out in ragged, frozen clouds.  The air itself seemed to crackle with a malevolent energy, a palpable dread that clung to him like the frost clinging to his beard.  He could feel the weight of his village, nestled far behind him in the shadow of the encroaching Dark Forest, a constant, gnawing ache in his heart.")
print()
print("They were simple folk, his people.  Fishermen, trappers, weavers… not warriors.  They were lambs, and the Dark Forest trolls, with their guttural roars echoing on the wind like some monstrous, distorted black metal shanty, were wolves.  Their hunger was a gnawing, insatiable thing, and the whispers of their depravity, tales of bone-charms and flesh-feasts, were enough to freeze the blood in even the bravest heart.  Marduk wasn't brave, not in the way bards sang of.  He was… desperate.")
print()
print("His hand tightened around the hilt of the ancestral axe, *Frostfang*, its steel as cold as the grave.  It was a family heirloom, passed down through generations of Marduks, though none had ever needed to use it.  Until now.  He was no warrior, but he was all they had.")
print()
print("He trudged on, his boots crunching through the knee-deep snow. The path, barely more than a game trail, wound its way towards the jagged peaks of the Spine of the World, where, legend whispered, the ancient Ice Wizard dwelt in isolation, a being of immense power, as cold and unforgiving as the winter itself.  Some said he was a myth, a story to frighten children.  Marduk prayed he wasn't.  His village, his *people*, were depending on him.  He had to find the wizard.  He *had* to.  Even if it meant facing the frozen wasteland, the howling winds, and the very real possibility that he would become just another frozen corpse on the mountain, a grim offering to the unforgiving gods of winter.  He was their last hope, a lone figure against the encroaching darkness, a solitary scream against the deafening silence of a world gripped by Winterfrost.")
print()
intro_question = ["The wind carries whispers of your name, Marduk. The spirits of the frozen north await your coming. Is your path clear, or does doubt still cloud your vision? Are you ready to walk the path laid out before you?", "The stars themselves have aligned, Marduk, marking this as the time for your journey. Destiny beckons. Will you answer its call, or will you cower in the face of the coming darkness? Is your heart prepared for the trials ahead?", "Alright, Marduk. You've sharpened your axe, you've mumbled your prayers. Time to put up or shut up. Ready to go freeze your nuts off on that mountain?", "Marduk, the clock's ticking. Those troll bastards aren't going to wait for a formal invitation. You in or out?", "Marduk, the fate of your village hangs in the balance. Does your spirit yet burn with the fire of resolve, or has the winter's chill frozen your heart? Are you prepared to face the Spine of the World and seek the Ice Wizard's aid?", "The whispers of despair reach us even here. The trolls grow bolder with each passing night. Marduk, son of Burzum, do you stand ready to answer the call of your people and embark on this perilous quest?", "Marduk, are you ready to begin your journey?", "Ready to go, Marduk?"]

def rand_intro():
    intro_question = ["The wind carries whispers of your name, Marduk. The spirits of the frozen north await your coming. Is your path clear, or does doubt still cloud your vision? Are you ready to walk the path laid out before you?", "The stars themselves have aligned, Marduk, marking this as the time for your journey. Destiny beckons. Will you answer its call, or will you cower in the face of the coming darkness? Is your heart prepared for the trials ahead?", "Alright, Marduk. You've sharpened your axe, you've mumbled your prayers. Time to put up or shut up. Ready to go freeze your nuts off on that mountain?", "Marduk, the clock's ticking. Those troll bastards aren't going to wait for a formal invitation. You in or out?", "Marduk, the fate of your village hangs in the balance. Does your spirit yet burn with the fire of resolve, or has the winter's chill frozen your heart? Are you prepared to face the Spine of the World and seek the Ice Wizard's aid?", "The whispers of despair reach us even here. The trolls grow bolder with each passing night. Marduk, son of Burzum, do you stand ready to answer the call of your people and embark on this perilous quest?", "Marduk, are you ready to begin your journey?", "Ready to go, Marduk?"]
    return random.choice(intro_question)

run = True
while run:
    
    print()
    print(rand_intro())
    print()
    
    a = "A: I am ready."
    b = "B: I need a moment to prepare."
    c = "C: I am afraid."
    print(a)
    print(b)
    print(c)
    
    print()
    intro_choice = input("Type a, b, or c: ").strip().lower()
    print()
    
    if intro_choice == "a":
        print("The spirits of our ancestors watch over you, Marduk.  May your axe strike true, and may your heart remain strong against the biting winds and the darkness that dwells in the mountains. Take this [item - e.g., family amulet, map etched on bone, enchanted compass]. It will guide you. The path is perilous, but our hope goes with you. Go now, and may the Ice Wizard hear your plea.")
        print()
        print("The weight of the village rests on my shoulders.  Fear is a cold companion, but duty is a stronger fire. I will not fail them. I will not fail her [mention a loved one if applicable]. The mountains await.  Frostfang is thirsty.")
        run = False
    elif intro_choice == "b":
        print("The trolls grow bolder with each passing sunset, Marduk. Time is a luxury we no longer possess. But even in haste, a warrior must be prepared. What do you need?")
        print()
        print("My hands tremble, my heart pounds like a war drum. I need to focus. I need to… [mention a specific thing - sharpen the axe, pray to the gods, remember a piece of advice].  A moment's pause may mean the difference between life and death, for me and for them.")
        # This opens up the opportunity for the player to perhaps gather supplies, talk to other villagers for information, or practice combat if the game allows it.
    elif intro_choice == "c":
        print( "Fear is a natural thing, Marduk. It is the shadow that walks beside courage. But fear must not paralyze you. Remember why you are doing this. Remember the faces of those you love, the laughter of children, the warmth of the hearth fire. These are the things the trolls would steal from us. Let that fear fuel your resolve, not extinguish it.  Take this [item]. It is a reminder of what you fight for. Now, go.  We believe in you.")
        print()
        print( "The cold seeps into my bones, a mirror of the fear that grips my heart.  But they are more afraid than I am. They are weak, huddled in the darkness. I am their shield, however flawed.  I will channel this fear. I will make it my strength. For them, I will face the darkness.")
        run = False
    else:
        print("You must make a choice: a, b, or c")

quit()
        
    
    
    
    
# The air grew heavy, the playful flurries of snow intensifying into a blinding white curtain.  The wind, no longer content to whisper, now howled like a banshee, clawing at Marduk's furs and threatening to rip him from the precarious mountain path.  The sun, a distant memory now swallowed by the encroaching storm, left the world in a twilight gloom, the only light the ghostly shimmer of the snow and the faint, ethereal glow emanating from the *Frostfang* axe in his hand.  The temperature plummeted, biting through his thickest layers, and a shiver, deeper than any cold he'd ever felt, ran down his spine.  He knew, with a certainty that chilled him to the bone, that this was no ordinary blizzard.  This was something else.  Something ancient and malevolent.  He pressed onward, each step a struggle against the growing tempest, the path ahead now almost completely obscured, his heart pounding a frantic rhythm against the rising crescendo of the storm. The mountains themselves seemed to watch him, silent, impassive giants shrouded in the swirling white chaos, as if waiting to see if he would survive the night.
