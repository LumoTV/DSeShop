from flask import Flask, Response

app = Flask(__name__)

# Exemple d'accueil - liste des jeux (format XML simple)
@app.route('/shop/menu.xml')
def shop_menu():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<shop>
  <title>DSi Shop Revival</title>
  <games>
    <game>
      <id>0001</id>
      <name>3DSNAKE</name>
      <price>500</price>
      <image>http://dancingpoilonours.atspace.cc/dseshop/ds-icon.png</image>
    </game>
    <game>
      <id>0002</id>
      <name>Fake Kart Racing</name>
      <price>700</price>
      <image>http://dancingpoilonours.atspace.cc/dseshop/ds-icon.png</image>
    </game>
  </games>
</shop>'''
    return Response(xml, mimetype='application/xml')

# Détail d'un jeu
@app.route('/shop/details/<game_id>.xml')
def game_details(game_id):
    games = {
        "0001": {
            "name": "Super Fake Mario",
            "description": "Un jeu de plateforme incroyable fait maison.",
            "price": 500,
            "image": "http://dancingpoilonours.atspace.cc/dseshop/ds-icon.png"
        },
        "0002": {
            "name": "Fake Kart Racing",
            "description": "Course de karts déjantée pour DSi.",
            "price": 700,
            "image": "http://dancingpoilonours.atspace.cc/dseshop/ds-icon.png"
        }
    }
    game = games.get(game_id)
    if not game:
        return Response("<error>Jeu non trouvé</error>", mimetype='application/xml'), 404

    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<game>
  <id>{game_id}</id>
  <name>{game["name"]}</name>
  <description>{game["description"]}</description>
  <price>{game["price"]}</price>
  <image>{game["image"]}</image>
</game>'''
    return Response(xml, mimetype='application/xml')

# Serveur de test
@app.route('/')
def index():
    return "<h1>Bienvenue sur la fausse Boutique Nintendo DSi</h1><p>Visitez /shop/menu.xml pour la liste des jeux.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
