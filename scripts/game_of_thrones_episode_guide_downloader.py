import sys
import unicodedata

import requests

try:
    OUTFILE = sys.argv[1]
except IndexError:
    OUTFILE = './build/markdown/game-of-thrones-episode-guide.md'

ARTICLE_API = ('https://gameofthrones.fandom.com'
               '/api/v1/Articles/AsSimpleJson?id={}')

SEASONS = []
SEASONS.append(
    [('Winter_Is_Coming', '2670'),
     ('The_Kingsroad', '2674'),
     ('Lord_Snow', '2694'),
     ('Cripples,_Bastards,_and_Broken_Things', '2705'),
     ('The_Wolf_and_the_Lion', '2711'),
     ('A_Golden_Crown', '2713'),
     ('You_Win_or_You_Die', '2714'),
     ('The_Pointy_End', '2696'),
     ('Baelor', '2743'),
     ('Fire_and_Blood', '2744')])
SEASONS.append(
    [('The_North_Remembers', '5397'),
     ('The_Night_Lands', '5499'),
     ('What_Is_Dead_May_Never_Die', '5862'),
     ('Garden_of_Bones', '5900'),
     ('The_Ghost_of_Harrenhal', '5905'),
     ('The_Old_Gods_and_the_New', '5904'),
     ('A_Man_Without_Honor', '5903'),
     ('The_Prince_of_Winterfell', '5902'),
     ('Blackwater', '3336'),
     ('Valar_Morghulis', '5906')])
SEASONS.append(
    [('Valar_Dohaeris', '13504'),
     ('Dark_Wings,_Dark_Words', '13505'),
     ('Walk_of_Punishment', '13500'),
     ('And_Now_His_Watch_Is_Ended', '13506'),
     ('Kissed_by_Fire', '13507'),
     ('The_Climb', '13930'),
     ('The_Bear_and_the_Maiden_Fair_(episode)', '13509'),
     ('Second_Sons_(episode)', '14243'),
     ('The_Rains_of_Castamere_(episode)', '13508'),
     ('Mhysa', '13510')])
SEASONS.append(
    [('Two_Swords', '21619'),
     ('The_Lion_and_the_Rose', '21620'),
     ('Breaker_of_Chains', '21621'),
     ('Oathkeeper', '21622'),
     ('First_of_His_Name', '21757'),
     ('The_Laws_of_Gods_and_Men', '21835'),
     ('Mockingbird', '22007'),
     ('The_Mountain_and_the_Viper', '22117'),
     ('The_Watchers_on_the_Wall', '22118'),
     ('The_Children', '22119')])
SEASONS.append(
    [('The_Wars_To_Come', '30456'),
     ('The_House_of_Black_and_White', '30457'),
     ('High_Sparrow_(episode)', '30458'),
     ('Sons_of_the_Harpy_(episode)', '30462'),
     ('Kill_the_Boy', '30901'),
     ('Unbowed,_Unbent,_Unbroken', '30902'),
     ('The_Gift_(episode)', '30903'),
     ('Hardhome_(episode)', '32193'),
     ('The_Dance_of_Dragons', '32631'),
     ('Mother%27s_Mercy', '33482')])
SEASONS.append(
    [('The_Red_Woman', '40364'),
     ('Home', '40608'),
     ('Oathbreaker', '40609'),
     ('Book_of_the_Stranger', '41124'),
     ('The_Door', '41158'),
     ('Blood_of_My_Blood', '42064'),
     ('The_Broken_Man', '42065'),
     ('No_One', '44158'),
     ('Battle_of_the_Bastards_(episode)', '44463'),
     ('The_Winds_of_Winter', '44464')])
SEASONS.append(
    [('Dragonstone_(episode)', '54256'),
     ('Stormborn', '54257'),
     ('The_Queen%27s_Justice', '54258'),
     ('The_Spoils_of_War', '54912'),
     ('Eastwatch_(episode)', '55428'),
     ('Beyond_the_Wall_(episode)', '55794'),
     ('The_Dragon_and_the_Wolf', '56048')])
SEASONS.append([('Season_8,_Episode_1', '53237')])

with open(OUTFILE, 'w') as f:
    f.write('---\n')
    f.write('title: Game of Thrones Episode Guide\n')
    f.write('author: https://gameofthrones.fandom.com/\n')
    f.write('date: Seasons 1 - 7\n')
    f.write('---\n\n')
    for season_num, season in enumerate(SEASONS, 1):
        f.write('# Season {}\n\n'.format(season_num))
        for ep_num, (ep_slug, ep_id) in enumerate(season, 1):

            r = requests.get(ARTICLE_API.format(ep_id))
            article = r.json()

            for (section_num, section) in enumerate(article['sections']):
                title = section.get('title', '').replace(' (episode)', '')

                # This is a bit janky. In practice, the episode summaries
                # end when one of the following sections appear.
                if title in ('Appearances', 'Production', 'Recap'):
                    break

                if section_num == 0:
                    print 'Writing "Season {} Episode {} - {}"'.format(
                        season_num, ep_num, title)
                    f.write('## Episode {} - {}\n\n'.format(
                        ep_num, title))
                else:
                    indent = int(section['level']) + 1
                    f.write('{} {}\n\n'.format((indent * '#'), title))

                for content in section['content']:
                    text = (
                        unicodedata
                        .normalize('NFKD', content['text'])
                        .encode('ascii', 'ignore')
                    )

                    f.write('{}\n\n'.format(text))
