import os
from flask_cors import CORS, cross_origin
from urllib.parse import quote_plus
from flask_migrate import Migrate
from flask import Flask, jsonify, redirect, render_template, request, url_for, abort
from flask_sqlalchemy import SQLAlchemy
import psycopg2
app = Flask(__name__)


passw = quote_plus("gerardo17")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://brdoaemuvtyvxw:ab1900c5e3420c6c5cc1e1b0bbb19f907618f19f39f7e9a5a4e27418fb5d7104@ec2-52-45-83-163.compute-1.amazonaws.com:5432/d93483t3uc2j0m'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app) 

CORS(app, resources={r"/api/*": {"origin": "*"}})   #Préciser le domaine authoriser à interroger une api

migrate = Migrate(app,db)

#creation de la classe

class Categorie(db.Model):
    __tablename__="categorie"
    id = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(50), nullable=False)
    livres=db.relationship('Livre',backref='categorie',lazy=True)

    def __init__(self,libelle_categorie):
        self.libelle_categorie = libelle_categorie

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'libelle_categorie': self.libelle_categorie,
            
        }

db.create_all()
class Livre(db.Model):
    __tablename__ = "livres"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(50), nullable=False)
    titre = db.Column(db.String(255), nullable=False)
    date_publication = db.Column(db.Date(), nullable=False)
    auteur = db.Column(db.String(50), nullable=False)
    editeur = db.Column(db.String(50),nullable=False)
    categorie_id=db.Column(db.Integer,db.ForeignKey('categorie.id'), nullable=False)


    def __init__(self,isbn, titre, date_publication,auteur,editeur,categorie_id) :
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.categorie_id = categorie_id 

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'titre': self.titre,
            'date_publication': self.date_publication,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'categorie_id': self.categorie_id,

        }


db.create_all()

def paginate(request):
    items = [item.format() for item in request]
    return items

#This route get all list of foods

@app.route('/livres')
def get_livres():
    livres = Livre.query.all()
    livres = paginate(livres)
    return jsonify({
        'success': True,
        'livre': livres,
        'total_livres': len(livres)
    })

@app.route('/categories')
def get_categories():
    categories =Categorie.query.all()
    categories= paginate(categories)
    return jsonify({
        'success': True,
        'categories': categories,
        'total_categorie':len(categories),
    })


# creation des routes

@app.route('/livres/<int:id>')
def get_livre(id):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return livre.format()

@app.route('/livres/categories/<int:id>')
def livres_category(id):
    try:
        categories=Categorie.query.get(id)
        livres =Livre.query.filter_by(categorie_id=id).all()
        livres= paginate(livres)

        return jsonify({
            'success': True,
            'class':categories.format(),
            'livre': livres
        })

    except:
        abort(400)
    finally:
        db.session.close()


@app.route('/categories/<int:id>')
def get_categorie(id):
    categories=Categorie.query.get(id)
    if categories is None:
        abort(404)
    else:
        return categories.format()

# la route path 

@app.route('/livres/<int:id>', methods=['DELETE'])
def del_livre(id):
    livre = Livre.query.get(id)
    livre.delete()
    return jsonify({
        'success': True,
        'delete successfully': id,
    })

@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_categore(id):
    categories=Categorie.query.get(id)
    categories.delete()
    return jsonify({
        'success': True,
        'delete successfully':id
    })




@app.route('/livres/<int:id>', methods=['PATCH'])
def update_livre(id):
    request_data = request.get_json()
    query = Livre.query.get(id)
    if 'id' in request_data:
        query.isbn = request_data['isbn']
        query.titre = request_data['titre']
        query.date_publication= request_data['date_publication']
        query.editeur= request_data['editeur']
        query.id= request_data['id']
        query.auteur= request_data['auteur']
        query.categorie_id= request_data['categorie_id']
    query.update()
    return jsonify({
        'success modify': True,
        'livre': query.format(),
    })

"""
@app.route('/categories/<int:id>', methods=['PATCH'])
def categories_update(id):
    request_data= request.get_json()
    query =Categorie.query.get(id)
    if 'libelle_categorie' in request_data:
        query.libelle_categorie = request_data['libelle_categorie']
        query.update()
    return jsonify({

        'success': True,
        'categories': query.format
    })"""
    
@app.route('/categories/<int:id>',methods=['PATCH'] )
def update_categorie(id):
    data = request.get_json()
    categorie= Categorie.query.get(id)
    if 'libelle_categorie' in data:
        categorie.libelle_categorie = data['libelle_categorie']
        #query.libelle_categorie = input()
        categorie.update()
    return jsonify({
        'success modify': True,
        'categorie': categorie.format(),
    })

# We can add food with this route

@app.route('/livres', methods=['POST'])
def add_livre():
    request_data = request.get_json()
    new_isbn = request_data['isbn']
    new_titre = request_data['titre']
    new_date_publication = request_data['date_publication']
    new_auteur = request_data['auteur']
    new_edteur = request_data['editeur']
    new_categorie_id = request_data['categorie_id']
    livre = Livre(isbn=new_isbn, titre=new_titre, date_publication=new_date_publication,
                auteur=new_auteur, editeur=new_edteur, categorie_id=new_categorie_id)
    livre.insert()
    count = Livre.query.count()
    return jsonify({
        'success': True,
        'ajouté': livre.format(),
        'total_livres': count,
    })


@app.route('/categorie', methods=['POST'])
def add_categories():
    request_data= request.get_json()
    new_libelle_categorie = request_data['libelle_categorie']
    categorie=Categorie(libelle_categorie=new_libelle_categorie)
    categorie.insert()
    count=Categorie.query.count()
    return jsonify({
        'success': True,
        'ajouté':categorie.format(),
        'total_categories': count,

    })



if __name__ == '__main__':
    app.run(debug=True)
    print('API lancé avec succes')
