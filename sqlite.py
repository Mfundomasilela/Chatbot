# Database Setup(SQlite)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qa.db'
db = SQLAlchemy(app)

class QA(db.model):
    id = db.column(db.Integer, primary_key=True)
    question =  db.column(db.String(500), nullable=False)
    answer = db.column(db.String(500), nullable=False)

    db.create_all()

    @app.route('/add_aq', methods=['POST'])
    def get_qa():
        data = request.get_json()
        new_qa = QA(question=data['question'], answer=data['answer'])
        db.session.add(new_qa)
        db.session.commit()
        return jsonify({"message": "QA added successfully"})


    @app.route('/add_aq', methods=['GET'])
    def get_qa():
        qa = QA.query.all()
        result = ({"question": qa.question, "answer": qa_answer} for qa in qas)
        return jsonify(result)
    
if __name__ == '__main__':
    app.run(debug=True)