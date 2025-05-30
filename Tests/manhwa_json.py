import json
from pathlib import Path

if __name__ == '__main__':
    data = {
        'types':[
            {
                'title': 'Best Action Fantasy Manhwa',
                'desc': 'Action fantasy manhwa is one of the most-read manhwa of all time. Its popularity has elevated due to adaptations of popular manhwas like Solo Leveling and Tower of God. Moreover, its extraordinary characters and top-tier illustrations, in particular, never fail to amaze the readers.',
                'list': [
                    {
                        'title': '1. Solo Leveling',
                        'img_name': 'solo-leveling.webp',
                        'points': [
                            'Writer: Chugong',
                            'Art: Redice Studio',
                            'Reads: 2.5B'
                        ],
                        'desc': 'One of the best action fantasy manhwa and the most talked about adaptation in recent times is undoubtedly Solo Leveling. It is set in a world where humans have discovered supernatural skills,while our protagonist, Sung Jin-Woo, is a nobody with his E-Rank hunting skills. Things will takean interesting turn for him when he becomes the sole survivor of a dungeon raid. Awakened withstrange new powers, Sung Jin-Woo will level up from being the weakest Hunter and eventually becomethe most powerful entity in the universe.'
                    },
                    {
                        'title': '2. Tower of God',
                        'img_name': 'tower-of-god.webp',
                        'points': [
                            'Creator: SIU (Lee Jong Hui)',
                            'Release: 2010 - Present',
                            'Episode: 197',
                            'Reads: 1.2B'
                        ],
                        'desc': 'Even if you are not a manhwa fan, you must have heard of Tower of God. This action fantasy manhwa became especially popular after its anime adaptation. Tower of God focuses on Twenty-Fifth Bam, the young protagonist of the manhwa, who is determined to climb a mysterious Tower to find his friend Rachel. It is to be noted that the titular tower has different floors, and each floor has different obstacles. His quest is not going to be an easy one, and whether or not he will be able to meet his friend remains to be seen. Tower of God Season 2 has also been recently released.'
                    },
                    {
                        'title': '3. Hardcore Leveling Warrior',
                        'img_name': 'hard-levelign-warrior.webp',
                        'points': [
                            'Creator: Sehoon Kim',
                            'Episode: 14',
                            'Status: Completed',
                            'Reads: 233.3M'
                        ],
                        'desc': 'Gong Won-Ho is the top player of Lucid Adventure because he uses his alias, Hardcore Leveling Warrior, to stay on top. However, one day, the unimaginable happens - he gets defeated, and now he has to get back on the top from the bottom. The most fascinating aspect of this action fantasy manhwa is how he climbed his way to the top in the first place.'
                    }
                ]
            },
            {
                'title': 'Best Romance Fantasy Manhwa',
                'desc': 'Nothing engages a reader more than a good romance tale with a unique narrative and amazing main characters. If you are looking for the best fantasy romance manhwa recommendations, you are at the right place. From rags to riches to an unexpected reincarnation, romance manhwa has everything that will compel you to keep scrolling. We recommend these 23 best romance fantasy manhwa.',
                'list': [
                    {
                        'title': '1. Lore Olympus',
                        'img_name': 'lore-olympus.webp',
                        'points': [
                            'Creator: Rachel Smythe',
                            'Episode: 280',
                            'Status: Every Sunday',
                            'Reads: 1.4B'
                        ],
                        'desc': 'We can\'t talk about the best fantasy manhwa and not mention Lore Olympus. Have you ever read Greek Mythology? Do you find it interesting? Well, a lot of people certainly do. However, the storyline and the order of events can be a little too difficult for most people to remember or even understand. \'Lore Olympus\' is such a webtoon based on Greek mythology, with an easy-to-understand plot that uses modern-day events and lifestyle. The plot is primarily based on Hades and Persephone\'s love story. Moreover, it also covers the lifestyle of all the gods surrounding them and the events of great importance.'
                    },
                    {
                        'title': '2. The Remarried Empress',
                        'img_name': 'Remarried-Empress.webp',
                        'points': [
                            'Writer: Alphatart', 
                            'Art: Sumpul', 
                            'Episode: 178', 
                            'Status: Every Sunday', 
                            'Reads: 436M'
                        ],
                        'desc': 'Navier, the empress of the Eastern Empire, was shattered in front of her when her husband Sovieshu, Emperor of the Eastern Empire, wanted to divorce her because she couldn\'t give him an heir. He cast her aside when she couldn\'t bear him a child, even though they groomed her to become the perfect empress ever since her childhood. Read The Remarried Empress to find out more about her struggles and dilemmas when an unexpected variable appeared in her life.'
                    },
                    {
                        'title': '3. Leveling Up My Husband to the Max',
                        'img_name': 'Leveling-up-my-husband-to-the-max.webp',
                        'points': [
                            'Creator: Uginon, Nuova, Curlin', 
                            'Episode: 117', 
                            'Status: Completed', 
                            'Reads: 83.1M'],
                        'desc': 'The central character of Leveling Up My Husband to the Max, Amber, is in turmoil with her controlling mother-in-law and cruel husband. Following the time-travel theme, Amber is sent back 10 years into the past, and she confronts her husband, who now adores her. With her knowledge of the potential future, she tries to change her husband, navigate the complexities of the past, and create a new narrative for herself.'
                    }
                ]
            },
            {
                'title': 'Best Adventure Fantasy Manhwa',
                'desc': 'With exceptional worldbuilding and extraordinary main characters, adventure fantasy manhwa will plunge you into the world of manhwa\'s beautiful storytelling and intense drama. Here are the 14 best adventure fantasy manhwa that you must read.',
                'list': [
                    {
                        'title': '1. A Returner\'s Magic Should Be Special',
                        'img_name': 'A-Returners-Magic-Should-Be-Special.webp',
                        'points': [
                            'Creator: Usonan', 
                            'Release: 2018 - Present', 
                            'Episode: 263', 
                            'Reads: 1.3B'],
                        'desc': 'This adventure fantasy manhwa is a story about the apocalypse and human destruction through the eyes of Desir Arman. Being one of the six surviving humans of the destruction, Desir thinks there is nothing left but to die. And just at his death, he finds himself transported back thirteen years ago. Now, having this second opportunity, Desire is determined to alter the past. Read A Returner\'s Magic Should Be Special to taste the blend of action, dark, and adventure fantasy manhwa.'
                    },
                    {
                        'title': '2. Omniscient Reader\'s Viewpoint',
                        'img_name': 'omniscient-reader.webp',
                        'points': [
                            'Writer: Alphatart', 
                            'Art: Sumpul',
                            'Episode: 178',
                            'Status: Every Sunday',
                            'Reads: 436M'],
                        'desc': 'Omniscient Reader\'s Viewpoint delivers a post-apocalyptic experience filled with legendary and mythical lore. This dark fantasy manhwa focuses on Kim Dokja, who derives pleasure only from a particular book that he manages to finish. In a shocking turn of events, his life turns upside down when the fictional book becomes reality. Being the only one with complete knowledge of this world, he becomes the center of attraction of a lethal game.'
                    },
                    {
                        'title': '3. The World After The Fall',
                        'img_name': 'world-after.webp',
                        'points': [
                            'Author: Sing N Song, Undead Gamja', 
                            'Episode: 119', 
                            'Status: Every Monday',
                            'Reads: 52.8M'],
                        'desc': 'The apocalyptic adventure fantasy Manhwa The World After the Fall explores the fictional destruction of humanity in a world of supernatural powers. However, unlike an Isekai fantasy, this manhwa explores the possibilities beyond the destruction of humanity. It focuses on Jaehwan, who, like others, was summoned as Walkers into the Tower of Nightmares. Humanity\'s hope and the chance to return in time now depend on him and what he will witness at the top of the Tower.'
                    }
                ]
            }
        ]
    }

    curr_path = Path(__file__).parent.resolve()

    with open(curr_path / 'manhwa.json', 'w') as f:
        json.dump(data, f)