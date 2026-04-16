""" 
Dictionaries for multiple semantic and linguistic variants of activity descriptions.
Each activity includes alternative textual descriptions for embedding experiments,
including short, medium, specific, noisy, unrelated, technical, and long-form versions.
"""


original_descriptions_fadi = {
    1: "The person drinks water from a glass or bottle to quench thirst, usually done in a kitchen or dining area. The person lifts the container to their mouth and tilts it to let the water flow in, feeling refreshed afterwards.",
    2: "The person eats a meal with utensils such as a fork and knife, often sitting at a dining table. The person uses the utensils to cut and bring food to their mouth, enjoying the taste and satisfying their hunger.",
    3: "The person opens a plastic bottle by unscrewing the cap, typically to drink or pour the contents. This involves gripping the bottle with one hand and twisting the cap with the other, sometimes hearing a popping sound as the seal breaks.",
    4: "The person opens a cardboard box to retrieve an item inside, usually by cutting or tearing the tape. This involves pulling open the flaps and reaching inside the box, often feeling a sense of anticipation and curiosity about the contents.",
    5: "The person brushes their teeth with a toothbrush and toothpaste, typically in a bathroom. This involves applying toothpaste to the brush and moving it back and forth against the teeth, aiming to remove plaque and maintain oral hygiene, and often results in a fresh minty taste in their mouth.",
    6: "The person brushes their hair using a hairbrush or a comb, usually in front of a mirror. This involves running the brush or comb through their hair to detangle and smooth it, often making their hair look neat and presentable.",
    7: "The person removes a jacket they are wearing by pulling it off, usually when entering a warm indoor space. This involves unzipping or unbuttoning the jacket and sliding it off their arms, often feeling relief from the heat as they do so.",
    8: "The person puts on a jacket, sliding their arms into the sleeves, typically before going outside. This involves aligning the sleeves with their arms and pulling the jacket onto their shoulders, preparing themselves for colder weather or rain.",
    9: "The person puts on a shoe, sliding their foot into it and tying the laces if necessary. This usually happens near the entrance of a home. The person bends down to adjust and secure the shoe, ensuring a comfortable fit for walking.",
    10: "The person takes off a shoe they are wearing by pulling it off, often when returning home. This involves loosening any laces or straps and sliding the shoe off their foot, often feeling a sense of relief and comfort as their feet are freed.",
    11: "The person puts on glasses to improve their vision, typically done in a well-lit area. This involves lifting the glasses and positioning them on their nose and ears, allowing them to see more clearly and reduce eye strain.",
    12: "The person removes glasses they were wearing to see better, usually to clean them or switch to contact lenses. This involves taking hold of the frames and lifting them off their face, often feeling a temporary blur in their vision.",
    13: "The person sits down on a chair or bench to rest or work, usually in an office, living room, or park. This involves bending their knees and lowering their body onto the seat, often feeling a sense of relaxation or readiness to focus on a task.",
    14: "The person stands up from a sitting position to start moving, often to walk or reach for something. This involves pushing against the chair and straightening their legs, feeling a shift in their center of gravity as they become upright.",
    15: "The person writes notes or a letter using a pen or pencil, typically at a desk or table. This involves holding the writing instrument and making marks on paper, often focusing on conveying thoughts clearly and legibly.",
    16: "The person makes a phone call using a smartphone, usually in a quiet area. This involves dialing a number or selecting a contact and holding the phone to their ear, often engaging in a conversation that requires attention and communication skills.",
    17: "The person types on a keyboard of a computer or laptop, typically sitting at a desk. This involves pressing keys to input text or commands, often focusing on accuracy and speed to complete a task or communicate online.",
    18: "The person waves their hand in a salute or greeting gesture, often done when meeting or leaving someone. This involves raising their hand and moving it side to side, often accompanied by a smile and eye contact to convey friendliness.",
    19: "The person sneezes or coughs into their elbow or a tissue, usually to prevent the spread of germs. This involves quickly covering their mouth and nose with their elbow or a tissue, often followed by disposing of the tissue or washing their hands.",
    20: "The person blows their nose into a tissue to clear nasal passages, often done when having a cold. This involves holding a tissue to their nose and exhaling forcefully, usually followed by a sense of relief and disposing of the used tissue.",
    21: "The person washes their hands with soap and water for hygiene, typically in a bathroom or kitchen. This involves rubbing their hands together with soap under running water, often for at least 20 seconds to ensure cleanliness and reduce the risk of infection.",
    22: "The person dusts surfaces or furniture using a cloth or duster, usually done in a living room or bedroom. This involves wiping surfaces to remove dust and dirt, often leaving the area looking clean and tidy.",
    23: "The person irons clothes using a hot iron to remove wrinkles, often done in a laundry room. This involves moving the iron back and forth over the fabric, often resulting in smooth, wrinkle-free clothes ready to be worn.",
    24: "The person washes dishes in the sink or a dishwasher after a meal, typically in a kitchen. This involves scrubbing dishes with a sponge or loading them into a dishwasher, often ensuring that all food residue is removed and the dishes are clean and ready for future use."
}


short_descriptions = {
    1: "drink water",
    2: "eat meal",
    3: "open bottle",
    4: "open box",
    5: "brush teeth",
    6: "brush hair",
    7: "take off jacket",
    8: "put on jacket",
    9: "put on shoe",
    10: "take off shoe",
    11: "put on glasses",
    12: "take off glasses",
    13: "sit down",
    14: "stand up",
    15: "writing",
    16: "phone call",
    17: "type on keyboard",
    18: "salute (wave hand)",
    19: "sneeze cough",
    20: "blow nose",
    21: "washing hands",
    22: "dusting",
    23: "ironing",
    24: "washing dishes"
}


medium_descriptions = {
    1: "Drinks water from a glass or bottle, lifting it to their mouth and tilting to drink, usually in kitchen/dining area.",
    2: "Eats a meal using fork and knife while seated at a table, cutting food and bringing it to mouth.",
    3: "Unscrews the cap of a plastic bottle to open it, usually to drink or pour.",
    4: "Opens a cardboard box by cutting/tearing tape and lifting the flaps to access contents.",
    5: "Brushes teeth with toothbrush and toothpaste in bathroom, creating fresh, minty feeling.",
    6: "Brushes or combs hair in front of mirror to detangle and smooth it.",
    7: "Removes jacket by unzipping/unbuttoning and sliding it off arms, usually upon entering warm indoor space.",
    8: "Puts on jacket by sliding arms into sleeves and pulling it onto shoulders before going outside.",
    9: "Slips foot into shoe and ties laces if needed, usually near home entrance.",
    10: "Takes off shoe by loosening laces/straps and pulling it from foot, typically when arriving home.",
    11: "Puts on glasses by placing them on nose and ears to improve vision.",
    12: "Removes glasses from face, usually to clean them or switch to contacts.",
    13: "Sits down on chair/bench to rest or work, bending knees and lowering body onto seat.",
    14: "Stands up from seated position by straightening legs and pushing off chair.",
    15: "Writes with pen or pencil on paper, usually at a desk.",
    16: "Makes phone call on smartphone by dialing/selecting contact and holding phone to ear.",
    17: "Types on computer/laptop keyboard, pressing keys to input text or commands.",
    18: "Waves hand in greeting or farewell gesture, usually with smile and eye contact.",
    19: "Sneezes/coughs into elbow or tissue to contain germs.",
    20: "Blows nose into tissue to clear nasal passages, usually during cold.",
    21: "Washes hands thoroughly with soap and water for at least 20 seconds.",
    22: "Dusts furniture/surfaces with cloth or duster to remove dust.",
    23: "Irons clothes with hot iron to smooth out wrinkles.",
    24: "Washes dishes by hand in sink or loads them into dishwasher after meal."
}


specific_descriptions = {
    1: "Lifting a glass or water bottle to the lips and tilting it backward to drink in a kitchen or at a dining table.",
    2: "Cutting pieces of food with knife and fork then transporting each bite to the mouth while seated at a dining table.",
    3: "Twisting the plastic cap off a bottle with fingers until a small pop is heard, usually before pouring or drinking.",
    4: "Cutting packing tape with a blade or tearing it by hand, then folding open cardboard box flaps to reach inside.",
    5: "Squeezing a stripe of toothpaste onto toothbrush bristles and brushing teeth in circular or up-down motions over a bathroom sink.",
    6: "Pulling a hairbrush or comb repeatedly through strands in front of a mirror to untangle and smooth hair.",
    7: "Unzipping or unbuttoning a worn jacket, then sliding arms out of sleeves to take it off completely.",
    8: "Pushing arms through jacket sleeves and pulling the garment up over shoulders to put it on before going outdoors.",
    9: "Sliding foot into an open shoe near the entrance door, then bending to tighten and tie laces or fasten straps.",
    10: "Loosening shoe laces or velcro, then pulling the shoe off the foot usually right after entering home.",
    11: "Picking up eyeglasses by the bridge and settling the lenses on nose with temples hooked behind ears.",
    12: "Grasping eyeglass frames near the lenses and lifting them upward off the face to remove them.",
    13: "Bending knees to lower body onto a chair, bench or sofa until fully seated in office, home or park.",
    14: "Pushing upward from armrests or thighs to straighten legs and rise from a seated to standing position.",
    15: "Gripping pen or pencil and moving its tip across paper in lines and curves to form letters and words at a desk.",
    16: "Tapping smartphone screen to select contact or dial digits, then holding device against ear to speak during call.",
    17: "Striking computer keyboard keys rhythmically with fingertips while seated to input text or commands.",
    18: "Raising open palm to shoulder height and oscillating hand left-right in greeting or farewell wave.",
    19: "Rapidly bending elbow to bring forearm across face, covering mouth and nose during a sneeze or cough.",
    20: "Pressing folded tissue firmly against nostrils and exhaling sharply through nose to blow mucus into it.",
    21: "Rubbing soapy palms and fingers together vigorously under running faucet water at bathroom or kitchen sink.",
    22: "Sweeping feather duster or dry cloth across tabletops, shelves and furniture to collect and remove dust.",
    23: "Gliding hot iron slowly back and forth across fabric laid flat on ironing board to press out creases.",
    24: "Scrubbing food residue off plates, bowls and cutlery with soapy sponge under kitchen sink tap water."
}


noisy_descriptions = {
    1: "The persn drink watter from glas or botle to quensh thurst, usally in kitchn or dining area lol. Lift container to mout and tilt it, water flow in and feel refreash afters.",
    2: "Person eat meal wif utinsils like fork & knive, sitting at tabel. Use them to cut food and bringg to mouth, enjoyin the tastee and satisfy hungar yo.",
    3: "Opens plastc botle by unsrewing cap, usualy to drinkk or pour stuff. Grip botle one hand twist cap other, somtimes pop sound when seal breakks haha.",
    4: "Person open cardbord box to get item inside, usualy by cuting or teering tape. Pull open flaps reach insde, feel exited and curius whats in theree.",
    5: "Brushs teeth with tothbrush & toothpast, in bathrom mostly. Put paste on brus and move back & forth on teef, remove plaq and keep mouth fresh mintyyy.",
    6: "Brush hair using brussh or combb, normaly infront mirror. Run it thru hair to untagle and make smooth, look neat and presentable af.",
    7: "Take of jaket they wearing by puling it of, usully when come in warm place. Unzip or unbuton then slide of arms, feel relif from hotnesss.",
    8: "Put on jaket, slide arms in sleves, before go outsdie. Align sleves pull jacket on sholders, get ready for cold or rainn brrr.",
    9: "Put shoe on, slide foot in and tie lacess if need. Usualy near door. Bend down ajust shoe make sure comfy for walkin.",
    10: "Take shoe of by puling, often when back home. Loosen lacess or straps slide of foot, feel so goood feet free at lastttt.",
    11: "Put on glasss to see better, in good light place. Lift glasess put on nose & ears, now can see cleaar no more eye strainn.",
    12: "Remove glasess was wearing, to clean or change to contacts. Grab frames lift of face, vision blurry for sec lol oops.",
    13: "Sits down chair or bench to restt or work, in office livingroom or park. Bend knees lower body on seat, feel relax or ready focuss.",
    14: "Stand up from siting to start move, often to walk or grab smth. Push chair straight legs, center gravity shift now uprite.",
    15: "Write notes or letter with pen or pencill, at desk or table. Hold thing make marks on paper, try make it clear & legablee.",
    16: "Make phone call on smartphon, in quiet area usualy. Dial number pick contact hold to ear, talk talk need pay atention.",
    17: "Type on keybord computer or laptop, sitting desk. Press keys input text or comand, focus accuracy & speeddd.",
    18: "Wave hand like salut or greeting, when meet or leave someone. Raise hand move side side, smile eye contact be friendlyy.",
    19: "Sneze or cough in elbow or tissu to not spread germss. Quick cover mouth nose with elbow, then throw tissu or wash handss.",
    20: "Blow nose in tissu to clear it, when have cold mostly. Hold tissu nose blow hard, feel better after then trash it.",
    21: "Wash hands soap & water for hygene, bathrom or kitchn. Rub hands soap under water like 20sec min, stay cleann no sick.",
    22: "Dust surfces furniture with cloth or duster, livingroom bedroom etc. Wipe wipe remove dust dirt, look clean & tidy noww.",
    23: "Iron cloths with hot iron take out wrinkless, laundry room. Move iron back forth on fabric, end up smooth clothes ready wear.",
    24: "Wash dishes sink or dishwashr after eat, in kitchen obv. Scrub sponge or load machine, get rid food bits clean for nexttt use."
}


random_unrelated_descriptions = {
    1: "Heavy cumulonimbus clouds release intense bursts of lightning across the evening sky during a summer thunderstorm.",
    2: "In 1453 the Ottoman army under Mehmed II breached the Theodosian Walls and captured Constantinople after a 53-day siege.",
    3: "The aurora borealis appears as shimmering green and purple curtains of light dancing above the Arctic Circle.",
    4: "Volcanic eruptions on the island of Krakatoa in 1883 produced the loudest sound ever recorded by humans.",
    5: "Giant sequoia trees in California can reach over 100 meters in height and live for more than 3,000 years.",
    6: "The Hubble Space Telescope captured an image known as the Pillars of Creation inside the Eagle Nebula.",
    7: "Polar bears rely on sea ice to hunt ringed seals and can swim continuously for more than 100 kilometers.",
    8: "Ancient Egyptian scribes used reed pens and black ink made from soot to write hieroglyphs on papyrus scrolls.",
    9: "The Great Barrier Reef stretches over 2,300 kilometers along the northeast coast of Australia.",
    10: "Quantum entanglement allows two particles to instantaneously influence each other regardless of distance.",
    11: "In Norse mythology Odin sacrificed one eye to gain wisdom from the well of Mímir.",
    12: "The invention of the movable-type printing press by Johannes Gutenberg around 1440 revolutionized book production.",
    13: "Mount Everest's summit reaches 8,848.86 meters above sea level in the Himalayan mountain range.",
    14: "Photosynthesis in plant leaves converts sunlight, carbon dioxide and water into glucose and oxygen.",
    15: "The Roman Colosseum hosted gladiatorial contests and wild animal hunts for nearly 400 years.",
    16: "Hummingbirds can flap their wings up to 80 times per second during rapid forward flight.",
    17: "Coffee was first cultivated in the highlands of Ethiopia before spreading across the Arabian Peninsula.",
    18: "Black holes warp spacetime so strongly that not even light can escape their event horizon.",
    19: "The migration of monarch butterflies covers up to 4,800 kilometers from Canada to central Mexico each autumn.",
    20: "In 1969 Apollo 11 astronauts left the first human footprints on the surface of the Moon.",
    21: "The Fibonacci sequence appears repeatedly in the spiral patterns of pinecones, sunflowers and nautilus shells.",
    22: "Antarctica holds approximately 60% of the planet's fresh water locked in its massive ice sheet.",
    23: "The shortest war in history lasted 38 minutes between Britain and Zanzibar on August 27, 1896.",
    24: "Octopuses possess three hearts, blue copper-based blood, and the ability to change color for camouflage."
}


detailed_technical_descriptions = {
    1: "The individual elevates a cylindrical vessel containing H2O to the oral cavity, initiating a controlled tilt to facilitate fluid ingestion via pharyngeal swallowing, primarily engaging deltoid and biceps brachii muscles in a domestic hydration zone.",
    2: "Seated at a horizontal surface, the subject manipulates bifurcated and bladed utensils to section edible substrates, then conveys portions to the buccal cavity for mastication and deglutition, involving forearm pronation and wrist flexion.",
    3: "Employing manual torque, the operator rotates the threaded polymer closure counterclockwise on a cylindrical container, disrupting the hermetic seal with auditory feedback, utilizing opponens pollicis and flexor digitorum muscles.",
    4: "The handler incises adhesive polymer strips on a cuboid cellulose enclosure using a sharpened implement or manual tension, subsequently deploying the superior panels to access internal contents via shoulder abduction and finger extension.",
    5: "In a sanitation facility, the user extrudes a fluoridated paste onto a bristle array, then applies oscillatory friction to dental enamel surfaces to dislodge biofilm, engaging masseter and orbicularis oris muscles for oral prophylaxis.",
    6: "Positioned before a reflective surface, the individual draws a multi-tined implement through cranial follicles to resolve entanglements, involving repetitive scapular retraction and elbow extension for follicular alignment.",
    7: "The wearer disengages a linear fastener on an upper torso garment, then extracts upper limbs from tubular extensions via shoulder external rotation and elbow straightening, achieving garment removal.",
    8: "Inserting upper extremities into fabric conduits of an insulating garment, the subject elevates the structure over the trapezius region via bilateral arm abduction, securing it for environmental adaptation.",
    9: "Adjacent to an ingress point, the foot is advanced into a pedal enclosure, followed by manual adjustment of tensile cords or fasteners via knee flexion and digital manipulation for secure encasement.",
    10: "Releasing tensile elements on a pedal sheath, the limb is withdrawn posteriorly through heel elevation and ankle dorsiflexion, completing disencasement upon domicile re-entry.",
    11: "Grasping an optical corrective frame, the user aligns nasal bridge support and auricular hooks via fine motor control of intrinsic hand muscles, enhancing visual acuity.",
    12: "Securing the temporal arms of an optical device, the individual elevates it superiorly from the facial plane through wrist supination, temporarily altering refractive correction.",
    13: "Initiating knee and hip flexion, the body mass is lowered onto a supportive platform via quadriceps eccentric contraction, achieving a seated posture in varied environments.",
    14: "From a flexed lower limb position, concentric contraction of gluteus maximus and quadriceps propels the torso vertically, restoring erect bipedal stance.",
    15: "Clasping a graphite or ink delivery stylus, the digits trace alphanumeric symbols on a planar medium via precision grip and wrist radial deviation at an elevated workstation.",
    16: "Activating a portable telecommunication device by digital input, the apparatus is approximated to the auditory canal via shoulder internal rotation for vocal transmission.",
    17: "Engaging bilateral phalanges on an alphanumeric input array, sequential depressions encode data through repetitive finger flexion at a computational interface.",
    18: "Elevating the upper limb to acromial level, oscillatory metacarpophalangeal motion generates a distal signal for interpersonal acknowledgment.",
    19: "Rapid cubital flexion positions the antebrachium across the nasal-oral region to contain aerosol expulsion during sternutation or tussive events.",
    20: "Compressing a fibrous absorbent against nares, forced nasal exhalation evacuates mucous secretions via diaphragmatic contraction.",
    21: "Under laminar fluid flow, interdigital friction with surfactant disperses contaminants via palmar emulsification in a hygienic basin.",
    22: "Traversing planar substrates with a microfiber or electrostatic collector, particulate matter is aggregated through surface adhesion in interior spaces.",
    23: "Applying thermal conduction from a metallic plate to textile fibers on a stabilized platform, systematic translation eliminates creases via molecular realignment.",
    24: "Submerging ceramic and metallic implements in an aqueous detergent solution, abrasive oscillation removes adherent residues in a culinary sanitation area."
}


very_long_narrative_descriptions = {
    1: "In the cozy confines of a sunlit kitchen or a warmly lit dining area, where the faint aroma of freshly brewed coffee lingers in the air and the hum of a refrigerator provides a subtle background noise, the person feels the parched dryness in their throat signaling an urgent need to quench their thirst. They reach for a clear glass or a chilled plastic bottle filled with cool, refreshing water, the condensation on its surface leaving a slight dampness on their fingertips as they grasp it firmly. With deliberate care, they lift the container slowly towards their lips, feeling the weight shift as the liquid inside sloshes gently against the sides. Tilting their head back slightly, they angle the rim to their mouth, allowing the crisp, pure water to flow in a steady stream over their tongue, tasting its neutral, revitalizing essence that instantly soothes the dryness. As they swallow, a wave of coolness travels down their esophagus, spreading a sense of hydration throughout their body. Lowering the container, they exhale softly, feeling the immediate relief and a renewed energy, perhaps wiping away a stray droplet from their chin with the back of their hand, the overall experience leaving them invigorated and ready to continue their day.",
    2: "Seated comfortably at a polished wooden dining table in a well-appointed dining room, surrounded by the comforting scents of savory herbs, steaming vegetables, and perhaps a hint of garlic wafting from the kitchen, the person prepares to satisfy their growing hunger after a long day of activities. They pick up a shiny silver fork in one hand and a sharp knife in the other, the cool metal handles fitting snugly into their palms as they survey the colorful plate before them—maybe a juicy steak, tender potatoes, and vibrant greens. With precise movements, they position the knife against the food, applying gentle pressure to slice through it, hearing the soft scraping sound of the blade against the plate and feeling the resistance give way as the piece separates. Lifting the fork-speared morsel to their mouth, they inhale the appetizing aroma up close before parting their lips to take a bite, the flavors exploding on their taste buds in a delightful mix of textures: the chewiness of meat, the creaminess of sauce, and the crunch of vegetables. Chewing slowly to savor each nuance, they continue this rhythmic process—cut, lift, chew, swallow—until their plate is cleared, their hunger fully appeased, and a warm satisfaction settles in their stomach, often accompanied by a contented sigh as they lean back in their chair.",
    3: "Standing in a brightly lit kitchen or perhaps outdoors on a sunny patio where the air is filled with the distant chirping of birds and the subtle rustle of leaves, the person holds a sleek plastic bottle containing a clear beverage, its label crinkling slightly under their grip as they prepare to access its contents to slake their thirst or pour it into a glass. They wrap their dominant hand around the textured cap, feeling the ridges dig into their skin for better traction, while their other hand steadies the smooth, cylindrical body of the bottle, which might be cool to the touch if recently refrigerated. With a firm twist counterclockwise, they apply torque, sensing the initial resistance from the safety seal before it yields with a satisfying 'pop' or 'crack' sound that echoes faintly, releasing a brief hiss of escaping pressure if the liquid is carbonated. As the cap comes free, they might catch a whiff of the beverage's scent—fresh citrus if it's soda, or nothing distinct if it's plain water—before setting the cap aside on a nearby counter, the bottle now open and ready for use, evoking a small sense of accomplishment in this everyday ritual.",
    4: "In the quiet excitement of a living room or home office, where natural light streams through windows casting soft shadows on the floor and the faint scent of cardboard mingles with the room's ambient air, the person approaches a sealed cardboard box that has just arrived via delivery, their curiosity piqued by the mystery of its contents, perhaps a long-awaited package from an online order. They first examine the box's exterior, running their fingers over the smooth, brown surface and noting any labels or tape securing the flaps. Grabbing a pair of scissors or a box cutter from a nearby drawer, they carefully slice through the adhesive tape, hearing the sharp tearing sound as it gives way and feeling the slight vibration in their hand from the tool's movement. With the tape severed, they grip the top flaps—rough and slightly fibrous to the touch—and pull them apart, sometimes encountering a puff of packing material like bubble wrap or foam peanuts that rustle softly as they shift. Reaching inside, their hands brush against protective wrapping, unwrapping it layer by layer to reveal the item, the anticipation building until the object is fully exposed, often accompanied by a smile of delight or surprise at the discovery.",
    5: "In the brightly illuminated bathroom, where the mirror reflects the soft glow of overhead lights and the air carries the fresh, invigorating scent of mint from an open toothpaste tube, the person stands before the sink, motivated by the routine of maintaining oral health after a meal or before bed, feeling the slight residue on their teeth that prompts this hygienic act. They first squeeze a pea-sized amount of creamy, white toothpaste onto the soft bristles of their toothbrush, hearing the subtle squish as it dispenses and smelling the strong, cooling mint aroma that promises freshness. Turning on the faucet, they wet the brush under the stream of warm water, which splashes gently against the sink basin, then bring it to their mouth. Parting their lips, they insert the brush and begin moving it in circular motions and back-and-forth strokes across their teeth, gums, and tongue, feeling the gentle abrasion removing plaque and food particles while the foam builds up, creating a bubbly sensation. After about two minutes, they spit out the frothy mixture, rinsing their mouth with a swish of water that leaves a clean, tingling coolness, and finally, they rinse the brush, emerging with a bright smile and a refreshed feeling that boosts their confidence.",
    6: "Positioned in front of a large, framed mirror in a bedroom or bathroom, where the soft morning light filters through curtains and the room holds a faint scent of shampoo or conditioner from recent use, the person picks up a wide-toothed comb or a sturdy hairbrush with smooth bristles, driven by the need to detangle knots formed overnight or from a windy day outside, aiming for a polished appearance. They section their hair if it's long, grasping a portion with one hand while the other holds the tool firmly, its handle ergonomic and cool against their palm. Starting from the ends, they gently pull the comb or brush through the strands, hearing the soft rasping sound as it encounters resistance and feeling the tug that loosens tangles without pulling too hard on the scalp. Working upwards towards the roots in methodical sub-steps, they smooth out each section, perhaps applying a light mist of detangling spray that adds a floral or fruity fragrance to the air. Once complete, they run their fingers through the now silky, flowing hair, admiring the neat, shiny result in the mirror, which enhances their self-image and prepares them for the day ahead with a sense of order and grooming.",
    7: "Upon entering a toasty indoor space like a welcoming home foyer or a heated office lobby, where the air is filled with the comforting warmth from a radiator and perhaps the subtle aroma of fresh-baked goods or coffee nearby, the person feels the immediate contrast of the indoor heat against their skin, prompting them to shed their outer layer to avoid overheating after coming in from the chilly outdoors. They first reach for the zipper or buttons at the front of their jacket, their fingers—still slightly numb from the cold—fumbling slightly as they undo the fastenings, hearing the soft zip or click with each release. Sliding one arm out of the sleeve, they feel the fabric brush against their clothing underneath, then repeat with the other arm, the jacket now dangling from their shoulders before they shrug it off completely. As it comes free, a rush of cooler air circulates around their torso, providing instant relief from the trapped warmth, and they might shake out the jacket to remove any lingering raindrops or snow, folding it over their arm or hanging it on a nearby hook, the action marking a transition from the external world to a more relaxed indoor environment.",
    8: "Standing near the front door of their home or in a cloakroom, where the air carries a slight chill from drafts seeping under the door and the scent of rain or fresh outdoor air lingers, the person anticipates stepping into cooler or wetter weather outside, motivating them to don a protective jacket for comfort and preparedness. They pick up the garment from a hook or chair, feeling its weight and the texture of the fabric—perhaps waterproof nylon or soft wool—against their hands as they hold it open. Aligning one sleeve with their arm, they slide it in smoothly, sensing the lining glide over their shirt sleeve, then repeat with the other arm, pulling the jacket up onto their shoulders with a gentle tug. Reaching for the zipper or buttons, they fasten it up, hearing the satisfying click or zip as it secures, enclosing them in a layer of warmth that immediately shields against the impending cold. Adjusting the collar or cuffs for a snug fit, they feel ready and protected, the sub-steps culminating in a sense of security as they prepare to venture out into the elements.",
    9: "In the entryway of their home, where shoes are neatly lined up on a mat and the floor tiles feel cool underfoot, with perhaps the distant sound of traffic outside signaling the start of a journey, the person bends down to put on a shoe, ensuring proper footwear for walking, running errands, or heading to work. They first loosen any laces or straps, their fingers deftly pulling them apart with a soft rustling sound, then position their foot—sock-clad for comfort—at the opening, sliding it in gradually and feeling the interior padding conform to their toes and heel. If laces are present, they cross them over in a familiar pattern, pulling tight at each loop to secure the fit, sensing the pressure evenly distributed without being too constricting. Standing up, they test the shoe by wiggling their toes and taking a step, adjusting if needed for optimal comfort, the entire process repeated for the other foot, leaving them grounded and ready to move with stability and support.",
    10: "Returning to the familiar warmth of home after a day out, in the foyer where the air smells of home-cooked meals and the floor welcomes bare feet, the person feels the fatigue in their legs and the desire for relaxation, prompting them to remove their shoes for comfort and to keep the indoors clean. Sitting on a nearby bench or leaning against the wall for balance, they first untie any laces, their fingers working the knots loose with a gentle pull, hearing the faint swish of the strings. Gripping the heel of the shoe with one hand and the toe with the other, they tug it off, feeling the release as their foot slides out, perhaps accompanied by a soft thud as the shoe drops to the floor. Wiggling their toes to enjoy the freedom, they repeat the process for the other shoe, often massaging their feet briefly to relieve any pressure points, the action symbolizing the end of external obligations and the embrace of domestic ease.",
    11: "In a well-lit room such as a study or living area, where sunlight or lamp light reduces shadows and highlights details, the person experiences blurred vision or eye strain from reading or screen time, leading them to reach for their glasses to enhance clarity. They pick up the lightweight frames from a table or case, feeling the smooth plastic or metal temples between their fingers as they unfold them with a subtle click. Lifting the glasses towards their face, they carefully position the nose pads on the bridge of their nose, adjusting for a secure yet comfortable fit, then hook the temples over their ears, sensing the slight pressure that holds them in place. As the lenses align with their eyes, the world sharpens into focus—the text on a page becomes crisp, distant objects clear—relieving the strain and allowing them to proceed with tasks more efficiently, often with a subtle nod of satisfaction at the improved sight.",
    12: "Perhaps in a bathroom or at a desk where cleaning supplies or contact lens solutions are at hand, under bright lighting that reveals smudges on the lenses, the person decides to remove their glasses to wipe them clean, rest their eyes, or switch to alternatives, feeling the temporary need to adjust their vision aids. They grasp the frames gently with both hands, one on each temple, feeling the warmth from prolonged wear as they lift them off, the world immediately softening into a blur that requires squinting. Folding the temples inward with a soft snap, they set the glasses down carefully, perhaps blowing on the lenses or using a microfiber cloth to polish away fingerprints, the sub-steps ensuring the glasses remain in good condition while their eyes adapt to the uncorrected view, often followed by a brief moment of disorientation before proceeding.",
    13: "In an office cubicle, a cozy living room corner, or a serene park bench where the environment invites rest or productivity—with background sounds like typing colleagues, soft music, or birdsong—the person feels the pull of gravity on their standing body or the need to engage in seated activities, prompting them to lower themselves onto a chair or bench. Approaching the seat, they turn their body to align with it, bending at the knees and hips while keeping their back straight, feeling the muscles in their legs engage as they control the descent. Their hands might grip the armrests for support, the cool wood or fabric providing stability, until their buttocks make contact with the cushion, sinking slightly into its softness with a faint creak from the chair. Adjusting their posture for comfort—shifting weight, crossing legs—they settle in, experiencing a wave of relaxation wash over them or a focused mindset emerging, ready for conversation, work, or simple repose.",
    14: "Seated in a chair during a meeting, meal, or rest period in settings like a conference room, dining area, or lounge, where the air might carry scents of food or office supplies, the person senses the need to move, reach for something, or transition to standing, initiating the upward motion. Placing their hands on the armrests or thighs for leverage, they push downward while straightening their legs, feeling the quadriceps contract and the shift in balance as their center of gravity rises. Their back extends from the seated curve to an upright position, perhaps with a subtle stretch that relieves any stiffness, accompanied by a soft exhale. Once fully standing, they might shake out their limbs to circulate blood, the action invigorating them and preparing for walking or the next task, marking a dynamic change in their physical state.",
    15: "At a sturdy desk or table in a quiet study or bustling cafe, where the surface is cluttered with papers, books, or a laptop and the air holds the faint ink scent of fresh pages, the person gathers their thoughts—perhaps ideas for a project, reminders, or a heartfelt letter—motivated to capture them in writing for clarity or communication. They select a smooth-writing pen or sharpened pencil, feeling its balanced weight in their hand as they uncap it with a click or sharpen if needed. Positioning a blank sheet of paper or notebook, they press the tip to the surface, sensing the slight friction as they form letters and words in flowing cursive or precise print, hearing the soft scratch of the instrument against the fiber. Pausing occasionally to reflect or erase errors, they build sentences step by step, ensuring legibility and coherence, until the page is filled, often concluding with a satisfied review and a sense of accomplishment in expressing their mind tangibly.",
    16: "In a relatively quiet space like a home office, bedroom, or even a parked car where ambient noise is minimal to ensure clear communication, the person thinks of someone they need to contact—perhaps for business, catching up, or assistance—and picks up their sleek smartphone, its screen lighting up with a soft glow upon touch. Unlocking the device with a fingerprint or code, they navigate to the contacts app, scrolling through names until finding the right one, or dialing manually with taps on the virtual keypad, hearing subtle beeps for each digit. Pressing the call button, they hold the phone to their ear, feeling its warmth against their skin as the ringing tone pulses—once, twice—until the connection is made with a click, and a voice greets them. Engaging in conversation, they listen intently, respond thoughtfully, perhaps pacing the room for better reception, the exchange requiring active listening, empathy, and articulation until they wrap up with goodbyes and hang up, often feeling connected or resolved.",
    17: "Seated ergonomically at a desk in an office or home workspace, where the hum of the computer fan and the click-clack of keys create a rhythmic backdrop, illuminated by a monitor's blue light, the person focuses on inputting data, writing emails, or coding, driven by deadlines or creative flow. They position their hands over the keyboard, fingers hovering above the familiar QWERTY layout, feeling the textured keys under their fingertips. With practiced speed, they press down on each key, sensing the tactile feedback of the switches—mechanical clicks if it's a gaming keyboard or soft thuds on a laptop—building words and commands letter by letter. Monitoring the screen for accuracy, they correct typos with backspace, perhaps using shortcuts like Ctrl+C for efficiency, continuing this fluid process until the task is complete, often stretching their fingers afterward to relieve any strain, the activity honing their digital communication skills.",
    18: "In social settings like a crowded street, a formal event hall, or a casual park gathering, where voices chatter and laughter fills the air, the person spots an acquaintance or friend approaching or departing, inspiring a friendly gesture to acknowledge them. Raising their arm smoothly from their side, they extend their hand—palm facing outward—with fingers together or slightly spread, then move it side to side in a gentle arc, the motion creating a subtle whoosh through the air. Accompanying this with a warm smile that crinkles their eyes and direct eye contact to convey sincerity, they might vocalize a 'hello' or 'goodbye,' the wave serving as a non-verbal bridge of connection. As the recipient responds in kind, the person lowers their arm, feeling a spark of positivity from the brief interaction that fosters social bonds.",
    19: "Suddenly overcome by an irritant like dust or a virus in environments ranging from a dusty attic to a public transit where allergens abound, the person feels a tickle in their nose or throat building to an inevitable sneeze or cough, prioritizing hygiene to avoid spreading germs. Quickly raising their elbow to their face or grabbing a soft tissue from a pocket or box, they cover their mouth and nose just in time, feeling the forceful expulsion of air and particles against the barrier. The sneeze erupts with a loud 'achoo' or the cough with a deep rumble, their body jerking slightly from the reflex, followed by a momentary dizziness or relief. Disposing of the tissue immediately in a trash bin if used, or wiping their elbow if that's the cover, they then wash their hands with soap and water, the sub-steps ensuring personal and public health safety in this involuntary act.",
    20: "Dealing with congestion from a cold or allergies in a private bathroom or at a desk with tissues handy, where the air might be stuffy and the need for relief is pressing, the person reaches for a clean, soft tissue from a box, its gentle pull accompanied by a faint rustle. Folding it if needed, they hold it firmly to both nostrils, pinching slightly for a seal, then inhale deeply through their mouth before exhaling forcefully through their nose, feeling the pressure clear the passages with a honking sound that echoes slightly. Repeating as necessary until the nasal cavities feel open, they experience a rush of fresh air intake, alleviating the stuffiness. Carefully folding the used tissue to contain the contents, they dispose of it promptly in a waste bin, often following up with hand washing to maintain hygiene, the process restoring comfortable breathing.",
    21: "Standing at a sink in a bathroom or kitchen, motivated by recent contact with germs—after using public transport, handling food, or sneezing—the person turns on the faucet, adjusting to a comfortable warm temperature as water cascades down with a steady rush. Dispensing a dollop of fragrant liquid soap onto their palms, they rub their hands together vigorously, creating a rich lather that feels slippery and bubbly, spreading it between fingers, over backs, under nails, and around wrists in methodical circles for at least 20 seconds, perhaps humming a tune to time it. The scent of lavender or citrus fills the air, enhancing the cleansing ritual. Rinsing under the stream, they feel the suds wash away, leaving skin clean and slightly taut, then dry with a towel or air dryer, the thorough sub-steps reducing infection risk and instilling a sense of purity.",
    22: "In a living room or bedroom where sunlight highlights floating dust particles and the air feels slightly musty from accumulated grime, the person equips themselves with a soft microfiber cloth or feather duster, aiming to restore cleanliness and freshness to surfaces like shelves, tables, or furniture. Starting with higher areas to let dust fall downward, they swipe the tool gently across the wood or glass, feeling the light resistance as it collects fine particles, hearing a faint swish with each pass. Watching the dust lift and settle elsewhere or cling to the duster, they methodically cover every nook—under lamps, around ornaments—shaking out the tool periodically over a trash bin to release captured debris. Upon completion, the surfaces gleam dust-free, the room smells fresher, and they feel a tidy satisfaction from the improved environment.",
    23: "In a dedicated laundry room or on an ironing board set up in a spare space, where the air warms from the appliance and carries the scent of fabric softener from clean clothes, the person plugs in the hot iron, waiting for it to heat up with a soft hum and indicator light. Selecting a wrinkled garment from a basket, they lay it flat on the padded board, smoothing it with their hands first. Spraying a light mist of water or starch if needed, which hisses upon contact with the hot soleplate, they glide the iron back and forth in steady strokes, feeling the weight press out creases and hearing the steam release. Section by section—collar, sleeves, body—they transform the fabric from rumpled to crisp, hanging it up immediately to prevent new wrinkles, the process yielding professional-looking attire ready for wear.",
    24: "After a satisfying meal in the kitchen, where counters are scattered with used utensils and the sink area smells of lingering food aromas mixed with dish soap, the person rolls up their sleeves to tackle the pile of dirty dishes, ensuring sanitation for future use. Filling the sink with hot, soapy water that bubbles up with a fresh lemon scent, they submerge plates and cutlery, letting them soak briefly to loosen residue. Grabbing a sponge or brush, they scrub each item methodically—circular motions on plates, back-and-forth on forks—feeling the grime give way under pressure and rinsing under clear water to reveal spotless surfaces. For tougher spots, they apply more elbow grease, then either drain and dry with a towel or load into a dishwasher with a clatter, starting the cycle with a button press and hum. The kitchen emerges orderly, the task fostering a sense of completion and hygiene."
}


DESCRIPTION_TYPES = {
    "original_fadi": original_descriptions_fadi,
    "short": short_descriptions,
    "medium": medium_descriptions,
    "specific": specific_descriptions,
    "noisy": noisy_descriptions,
    "random_unrelated": random_unrelated_descriptions,
    "detailed_technical": detailed_technical_descriptions,
    "very_long": very_long_narrative_descriptions
}


def get_descriptions(desc_type="original_fadi"):
    """Return the activity-description dictionary for the requested description variant."""
    if desc_type not in DESCRIPTION_TYPES:
        raise ValueError(f"Unknown description type: {desc_type}. Choose from {list(DESCRIPTION_TYPES.keys())}")
    return DESCRIPTION_TYPES[desc_type]