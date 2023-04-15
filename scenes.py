import disp
import data


############################################################
def intro(): 

  name = input("What is your name? ")
  print("\nHello, {}.".format(name))
  input()
  
  while True:

    option_list = ["The Moosetaur Knight!", "The Goblin Thief!", "The Elvish Wizard!"]
  
    disp.wrap("Who are you?")
    disp.options(option_list)
    prompt_chosen = disp.prompt(option_list)
  
    if prompt_chosen == "The Moosetaur Knight!":
      data.set_data("job", 1)
      disp.wrap(
        "  Royal Paladins are masters of the righteous art of melee. With their keen combat sense and unrivaled strength, these warriors make their presence felt on any battlefield. Protectors of the realm, destroyers of blasphemy, lifters of heavy things."
      )
      input()
      disp.wrap(
        "  You, {}, were once one of these honorable Paladins, sworn to serve the queendom with nobility and valor. After an embarrassing event that would be better left unmentioned, you were stripped of your Royal rank. Now, you are a Knight Errant, searching the realm for an opportunity to prove yourself once more. Hefty steel armor grounds you to the earth. A sturdy warhammer is strapped to your rippling back beneath an even sturdier shield. Your scuffed antlers have seen plenty of blows, both given and received.".format(name)
      )
      input()
      disp.wrap(
        "  Before *the accident*, your former cohorts would have described you as loyal, practical, and very very tall. You faced problems head-on, and might not have hesitated to use zealous force to achieve your goals. You were the Law. It is up to you what that means to you now."
      )
      input()
      disp.wrap(
        "Today, you have taken it upon yourself to investigate a Wizard's tower on the Stainless Coast. The crown has placed a bounty on such *tricksters*. Should you find evidence of heresy, blasphemy, or any other sign of unorthodoxy, you're certain this conjurer's head would earn you your former rank."
      )
      input()
  
    elif prompt_chosen == "The Goblin Thief!":
      data.set_data("job", 2)
      disp.wrap(
        """  Thieves are masters of stealth and subterfuge. With pinpoint perception and dexterity without equal, the secretive "Busker's Guild" has shaped the queendom from the shadows for generations. The guild is also known to perform at public venues occasionally. Purveyors of priceless artifacts, executors of Her Majesty's secret will, doers of filthy acts at a reasonable price."""
      )
      input()
      disp.wrap(
        "  You, {}, are a master burglar, and a Goblin. For the past decade you have honed your abilities to a bleeding edge. No high-security prison can hold you. No hidden doors elude your notice. No safe is... safe. A long line of pilfered pockets and purses trails behind you. Metaphorically, that is; you are a professional, and *never* leave a trace.".format(name)
      )
      input()
      disp.wrap(
        """  Your Guildmates have described you as "tricksy", "surprisingly charismatic", and "that horrible little Goblin." The dark shroud draped around your nimble form hides custom, studded leather armor. You are replete with well-hidden daggers, mostly used as tools for cutting and threatening. You tend to approach problems carefully and from all angles, using visual calculus and creative reasoning to rob people of all their shiny goodies."""
      )
      input()
      disp.wrap(
        "  When not contracted through the Guild, you are free to pursue your own interests. Today, those interests lie inside a Wizard's tower on the Stainless Coast. It appeared two days ago, and the queendom has been abuzz ever since. Everyone knows Wizards are *utterly flush*, and you intend to make the most of this situation. That tower's got *treasure* in it."
      )
      input()
  
    elif prompt_chosen == "The Elvish Wizard!":
      data.set_data("job", 3)
      disp.wrap(
        """  Wizards are masters of mind and matter. With universally robust intelligence and a general disregard for the so-called "laws" of physics, Wizards have an unmatched control of the world around them. Virtuosos of the fabric of the universe, invaluable advisors to royalty, riders of *lightning.*"""
      )
      input()
      disp.wrap(
        """  You, {}, are a Wizard of immense power. Through decades of intense study and dedication you have laid bare to yourself the blueprints of reality. You possess a deep understanding of the natural and unnatural planes, and harness the expertise to act upon them. You are a member of an elite, educated stratum of society. Very few people have any idea what it is Wizards really do.""".format(name)
      )
      input()
      disp.wrap(
        """  If you had any friends (you don't), they would describe you as inquisitive, calculating, and obsessive. You're a bit of a know-it-all, and not particularly good at parties. Until, that is, you set someone's hat on fire. That always gets the people going.""")
      input()
      disp.wrap(
        """  Today, you are visiting and old friend. You are headed to a camouflaged tower on the coast to see Gwynevere DeKell, a Wizard of no small reknown. She was your dorm mate at the University, and you have kept in touch via monthly letters. Until, that is, two days ago. Her letter is late, and a Wizard is *never* late.""")
      input()

    option_list = ["Yes! Let's go!", "No, wait, let me think about it first."]
    disp.wrap("Are you sure this is who you want to be?")
    disp.options(option_list)
    prompt_chosen = disp.prompt(option_list)
  
    if prompt_chosen == "Yes! Let's go!":
      return

############################################################
def cliffside():
  
  disp.wrap(disp.job(data.get_data("job"), [
    """ Climbing up a seaside cliff with your bare hands is no easy task.  With jagged rocks and slippery handholds, the freezing stone saps your fuzzy fingers of feeling.  Thickets of thorny flowers tug nastily on your fur as you grasp for support.""",
    """  Scaling a seaside cliff is manageable for someone with your skillset, but still irritating. As you methodically sink a series of iron pitons into cracks in the crag, you grumble to yourself ruefully. Would it kill a Wizard to consider accessibility for once?""",
    "  Ascending a seaside cliff is a trivial task. Through the shimmering sphere surrounding your body, you watch a wall of stone glide silently downward before you. Glancing downward between your finely crafted slippers, a circle of children stare up at you in amazement. The stones they were previously ploinking off your magical bubble no longer reach."
  ]))

  option_list = disp.job(data.get_data("job"), [["Continue climbing.", "Stop to smell the flowers.", "Give up. Go home, maybe curl some dumbbells."], ["Continue climbing.", "Stop to smell the flowers.", "Give up. Go home, maybe curl up with the newest issue of Locksmith's Digest."], ["Continue ascending.", "Stop to smell the flowers.", "Give up. Go home, maybe curl up with a book.", "What was that about a bubble spell?"]])

  
  while True:

    #TODO add flag-based options.
    
    disp.options(option_list)
    prompt_chosen = disp.prompt(option_list)
  
    if prompt_chosen == "Stop to smell the flowers.":
      if data.get_data("job") == 3:
        disp.wrap("""  All you can detect is a faint scent of stale air and ozone. Magic almost always smells like ozone.""")
        input()
      
      elif data.get_data("job") == 1 or 2:
        if data.get_data("job") == 1:
          disp.wrap("""  The muscles in your forearms work overtime as you momentarily relax the rest of your upper body. Your horseshoes find purchase on a big mossy stone, providing a welcome hoofhold.""")
          input()
        elif data.get_data("job") == 2:
          disp.wrap("""  The muscles in your forearms work overtime as you momentarily relax the rest of your upper body. Your boots find purchase on a big mossy stone, providing a welcome foothold.""")           
          input()      
        
        disp.wrap("""  On the way up, your nervous system had dulled itself to the world. To protect you. This rest, while needed, is slowly allowing *feeling* back into your body.""")
        input()
        
        disp.wrap("""  Confident that you won't plummet to your death, you lean towards the wildflowers and inhale deeply.""")
        input()
        
        disp.wrap(
          """  The delicate floral fragrance contrasts the harsh burning in your muscles and lungs. A cool breeze off the ocean carries the briny smell of salt and seaweed. You hear from above you seagulls crying out balefully. From below come the roar and hiss of waves attacking the shore."""
        )
        input()
        
        if data.get_data("flowers_smelled") == False:
          option_list.append("Look around. Take in your surroundings.")
          data.set_data("flowers_smelled", True)
  
    elif prompt_chosen == "Continue climbing." or "Continue ascending.":
      if data.get_data("flowers_smelled") == False:
        disp.wrap("""  No time for flowers. You'll get plenty of flowers when you're dead. Hopefully. Onward and upward!""")
        input()
      if data.get_data("job") == 1 or 2:
        disp.wrap("""
        The sun is blocked out by the tower which looms closer with each passing minute, casting a variety of long shadows. Sweat beads on your forehead, but with a deep breath and a tight grip, you march onward.
        """)
      else:
        disp.wrap("""
        The sun is blocked out by the tower which looms closer with each passing second, casting a variety of long shadows. You magic away some grime from beneath a fingernail as you float gently skyward.
        """)
      input()
      break  # PROGRESS
  
    elif prompt_chosen == "Give up. Go home, maybe curl some dumbbells." or "Give up. Go home, maybe curl up with the newest issue of Locksmith's Digest." or "Give up. Go home, maybe curl up with a book.": #TODO
      if data.get_data("job") == 1: # Knight text
        disp.wrap("""
        That's it. You're done. What kind of *heresy* could that dusty old wizard's tower really contain, anyway? Dark Magicks? Malevolent blood-daemons? Political literature!?
        """)
        input()
        disp.wrap("""
      Nah, you say. To heck with this. You're going home to whittle soft woods and live the *good* life.
  
      [GOOD END.]
      """)
        
      elif data.get_data("job") == 2: # Thief text
        disp.wrap("""
      That's it. You're done. What kind of *treasure* could that dusty old wizard's tower really contain, anyway? Priceless artifacts? Precious gemstones? Rare, immensely valuable books!?
      """)
        input()
        disp.wrap("""
       Nah, you say. To heck with this. You're going home to pick pockets and live the *good* life.
  
      [GOOD END.]
      """)
      
      elif data.get_data("job") == 3: # Wizard text
        disp.wrap("""
      That's it. You're done. What kind of *mysteries* could that dusty old wizard's tower really contain, anyway? Ancient mystical tomes? Esoteric libraries? Portals to bizarre, otherworldly planes of existence!?
      """)
        input()
        disp.wrap("""
       Nah, you say. To heck with this. You're going home to read dusty tomes and live the *good* life.
  
      [GOOD END.]
      """)
        
      exit() # GAME END.
  
    elif prompt_chosen == "Look around. Take in your surroundings.":
      disp.wrap(
        """  During a long climb, pausing for too long can be deadly. The view, you decide, will be worth the risk. You tighten your grip on a dependable-looking root vine and turn away from the stone wall."""
      )
      input()
      disp.wrap(
        """  Your eye follows a pair of white seagulls soaring gracefully through blue skies. Glimmering sunshine on the sea's surface makes you squint. The water is so clear you can make out schools of brightly colored fish dancing beneath the surface."""
      )
      input()
      disp.wrap(
        """  In the far distance, a lighthouse stands tall and proud by a busy harbor. When the pounding in your ears subsides, you can distinguish the deep call of foghorns."""
      )
      input()
      disp.wrap(
        """  Closer, a fishing village squats on the pristine shore below you. Dark, shiny planks accented with pale gnarly driftwood give the structures a sort of rustic beauty. Humanoid shapes are visible at this range. Fishers mend nets. Children chase each other through narrow alleys."""
      )
      input()
      disp.wrap(
        """  Outlying huts brace the cliffside directly below you. When you shift your weight, a stone tumbles downward, tinking off a tin chimney cover. A nearby orc notices you and shakes her fist."""
      )
      input()
      disp.wrap(
        """  You crane your neck away from the cool stone to peer up at your goal. Thorny brambles peer back from the top of the cliff. Through them, you spot a wooden add-on extending from the side of a round, whitewashed structure."""
      )
      input()
  
    elif prompt_chosen == "Hold on, what was that about a bubble spell?":
      disp.wrap("""  Alastair's Bubble? What, the elevator spell? It's not particularly exciting. Surely you would rather hear about one of the *cool* spells. Like Fireball, perhaps?""")
      input()
      while True:
        
        option_list = ["Nuh uh. Bubble spell please.", ]
        
        disp.wrap()
      
  # NEXT SCENE
  disp.wrap("moving on SUCCESS")