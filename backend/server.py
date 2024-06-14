from flask import Flask, jsonify
from flask_cors import CORS

import random

app = Flask(__name__)
app.secret_key = 'dev'

CORS(app)  # Enable CORS for all routes

# global variables for the summon routes

# all 5 stars up to 1st half of 2.2 with Robin
FiveStars = {
    "Seele": 'https://www.prydwen.gg/static/d9e381f3ee8c3eb7ea55b4e53757cb9d/cf6d0/13_full.webp',
    "Robin": 'https://www.prydwen.gg/static/97724870b40ece6cf174ced4fe3a086c/e0b44/robin_full.webp',
    "Huohuo": 'https://www.prydwen.gg/static/621dc2b9f734b488c234c15dc4304695/cf6d0/40_full.webp',
    'Acheron': 'https://www.prydwen.gg/static/1f79fb5988de1afb4d4cad2fbff2c434/67ded/acheron_full.webp',
    'Argenti': 'https://www.prydwen.gg/static/33404e7b6681e4aaaf8a1c9732074959/cf6d0/41_full.webp',
    'Adventurine': 'https://www.prydwen.gg/static/31fe18957cd5719c1b422c3fe3d4c785/67ded/aventurine_full.webp',
    'Black Swan': 'https://www.prydwen.gg/static/6558cd04ec8f4ee3f197b7c2ed9541bc/3cd29/black_full.webp',
    'Blade': 'https://www.prydwen.gg/static/ffb817323f50964ed3080989eb4f29c6/cf6d0/28_full_1_.webp',
    'Dan Heng * Imbibitor Lunae': 'https://www.prydwen.gg/static/a43d2917251884719f7944ac86dfe574/cf6d0/34_full.webp',
    'Dr. Ratio': 'https://www.prydwen.gg/static/49fc4d53179099c7bd05efca2d3830a9/cf6d0/ratio_full.webp',
    'Fu Xuan': 'https://www.prydwen.gg/static/ec68111d7da8a88f806d76a52328be50/cf6d0/29_full.webp',
    'Jing Yuan': 'https://www.prydwen.gg/static/4991dfe383d39280c2c6b87d80ef1b09/cf6d0/22_full.webp',
    'Jingliu': 'https://www.prydwen.gg/static/2530fc295a5e41a948bb8424c434d5e4/cf6d0/36_full.webp',
    'Kafka': 'https://www.prydwen.gg/static/951a54972ba6eee96d7ace270d717932/cf6d0/7_full.webp',
    'Luocha': 'https://www.prydwen.gg/static/bd765e53a8d5b55f5fd6d518fd1188c0/cf6d0/21_full.webp',
    'Ruan Mei': 'https://www.prydwen.gg/static/5d8db934a5036f2c3f2e0ba1e3f22638/cf6d0/43_full.webp',
    'Silver Wolf': 'https://www.prydwen.gg/static/72d7425c64d044e81ff078ecdb4aec2f/cf6d0/8_full.webp',
    'Sparkle': 'https://www.prydwen.gg/static/9ef94f3d28f4efdba73111d123f989fe/3cd29/sparkle_full.webp',
    'Topaz & Numby': 'https://www.prydwen.gg/static/747ff59c7c844f6d2dfbb3a46a98e532/cf6d0/38_full.webp'
}

# order: Bailu, Bronya, Clara, Gepard, Himeko, Welt, Yanqing
StandardFiveStars = [
    'https://www.prydwen.gg/static/932172867d7ad8c7310d8f7dff276f86/cf6d0/24_full.webp',
    'https://www.prydwen.gg/static/8c261f865fa22aa63036ed6b19976de7/cf6d0/12_full.webp',
    'https://www.prydwen.gg/static/bd1576553e127b3a8fec52169fc95db5/cf6d0/18_full.webp',
    'https://www.prydwen.gg/static/5fbe8fa8ee817229dc54c6649bfc0510/cf6d0/15_full.webp',
    'https://www.prydwen.gg/static/5229eb21c45b43d25493197f19055345/cf6d0/5_full.webp',
    'https://www.prydwen.gg/static/1011c44a635593aa22a41b18519b1e36/cf6d0/6_full.webp',
    'https://www.prydwen.gg/static/0572234e9a22eede4e5d39d1063e91d0/cf6d0/23_full.webp'
]

FourStars = [
    # march
    "https://www.prydwen.gg/static/66dfd6e26da58c08aa94315dbb288c5c/cf6d0/3_full.webp",
    # lynx
    "https://www.prydwen.gg/static/d86542a5b2616b6fea58248b618cebf1/cf6d0/35_full_1_.webp",
    # sampo
    "https://www.prydwen.gg/static/f8e75db831bcfe66b9f02dd44474cf01/cf6d0/19_full.webp",
    # tingyun
    "https://www.prydwen.gg/static/fa18172a868f8fe5268af86ae17f34cb/cf6d0/25_full.webp",
    # asta
    "https://www.prydwen.gg/static/6c5362dea19b62160a3d8a776bfff37e/cf6d0/10_full.webp",
    # arlan
    "https://www.prydwen.gg/static/ecef0bbb16cd6aba72101a795fe08e93/cf6d0/9_full.webp",
    # dan heng
    'https://www.prydwen.gg/static/78a6404252106144837fb74ad3774a9b/cf6d0/4_full.webp',
    # gallagher
    'https://www.prydwen.gg/static/7f9fce0eccac66a56a9281f99dea1dd5/67ded/gallagher_full.webp',
    # guinaifen
    'https://www.prydwen.gg/static/79fb0db28d9a9c09885fd17b6750b182/cf6d0/39_full.webp',
    # hanya
    'https://www.prydwen.gg/static/a580e4702533cc229d84f431d9d00c1c/cf6d0/42_full.webp',
    # herta
    'https://www.prydwen.gg/static/0306d4fb2ede9beb1e30758bfe56b547/cf6d0/11_full.webp',
    # hook
    'https://www.prydwen.gg/static/e5b622282805dd45bb9750710edec470/cf6d0/20_full.webp',
    # luka
    'https://www.prydwen.gg/static/86320b88a38b4f9b75cdbd031239b4b5/cf6d0/33_full.webp',
    # misha
    'https://www.prydwen.gg/static/affc3a063636436e3517bad868564247/3cd29/misha_full.webp',
    # natasha
    'https://www.prydwen.gg/static/190848d53bcb3cba93f8bf8092af5be3/cf6d0/16_full.webp',
    # pela
    'https://www.prydwen.gg/static/b2e816a75e4a878058f8d806a2ad495b/cf6d0/17_full.webp',
    # qingque
    'https://www.prydwen.gg/static/0c88f2d12bce359881fe49b9261624de/cf6d0/26_full.webp',
    # serval
    'https://www.prydwen.gg/static/4e292baa485bd7f7ec570b0a00605acd/cf6d0/14_full.webp',
    # sushang
    'https://www.prydwen.gg/static/b6f5ff92c1a26b3502d65edf9a037869/cf6d0/27_full.webp',
    # xueyi
    'https://www.prydwen.gg/static/6e4083969f942e9348fe9391a3eb3382/cf6d0/xu_full.webp',
    # yukong
    'https://www.prydwen.gg/static/2e12841a3cf37202ac046bcf6951b60d/cf6d0/32_full.webp'
]

pulls = 0
max_pulls = 90
guarantee = 0
chance = 0.6

@app.route('/summon/<fiveStar>', methods=['GET'])
def summon(fiveStar):

    global pulls, guarantee, chance

    summon = gacha(fiveStar)
    return jsonify({
        "summon": summon
    })

@app.route('/summons/<fiveStar>', methods=['GET'])
def summons(fiveStar):

    global pulls, guarantee, chance
    summons = [gacha(fiveStar) for _ in range(10)]
    return jsonify({"summons": summons})

def gacha(fiveStar):
    # added by ChatGPT
    global pulls, guarantee, chance

    pulls += 1

    # to track the pity count and whether you're at guarantee on the python terminal if you desire
    # print('Pity is: ' + str(pulls))
    # print('Guarantee is: ' + str(guarantee))

    if pulls < max_pulls:
        # RanNum is chance, 5% for user to hit the 5 star
        RanNum = random.randrange(1, 1001) / 10

        # user hits the 5 star
        if RanNum < chance:
            # reset pull count
            chance = 0.6
            pulls = 0
            if guarantee == 0:
                RanNum = random.randrange(1, 3)
                if RanNum == 1:
                    return FiveStars[fiveStar]
                else:
                    # if missed limited 5 star, next 5 star is limited character guaranteed
                    guarantee = 1
                    # selects a random item from the list
                    return random.choice(StandardFiveStars)
            else:
                guarantee = 0
                return FiveStars[fiveStar]
        else:
            if pulls >= 74:
                # increases chance via soft pity at pulls 74 and beyond if user has not gotten a 5 star yet
                chance += 6
            return random.choice(FourStars)
    # hit max pity
    else:
        # reset pull count
        pulls = 0
        # reset chance for 5 star
        chance = 0.6
        if guarantee == 0:
            # 50% chance of the limited Five Star
            RanNum = random.randrange(1, 3)
            if RanNum == 1:
                return FiveStars[fiveStar]
            else:
                # if missed limited 5 star, next 5 star is limited character guaranteed
                guarantee = 1
                return random.choice(StandardFiveStars)
        else:
            guarantee = 0
            return FiveStars[fiveStar]
    
if __name__ == "__main__":
#    app.env = "development"
    app.run(debug = True, port = 5000)